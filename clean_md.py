import os
import re

MD_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\md'

# ---------------------------------------------------------------------------
# Exact-match header/footer lines (remove if entire stripped line matches)
# ---------------------------------------------------------------------------
HEADER_FOOTER_LINES = {
    "ABCB Housing Provisions Standard 2025",
    "NCC 2025 Volume Two - Building Code of Australia",
    "Livable Housing Design Standard 2025",
    "Livable Housing Design",
    "Front matter",
    "Copyright",
    "First published",
    "Published by Standards Australia",
    "This is a free page",
    "STANDARDS AUSTRALIA",
    "STANDARDS NEW ZEALAND",
    "PAEREWHA AOTEAROA",
    "Australian/New Zealand Standard",
    "Originated in Australia, New Zealand",
    "Australian Standard",
    "In Australia",
    "In New Zealand",
    "COPYRIGHT",
    "\u00ae Standards Australia",
    "Standards Australia",
    "Standards New Zealand",
    "ISBN",
    "\u00a9 Standards Australia",
    "This page has been left intentionally blank.",
    "This page has been left intentionally blank",
}

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------
STANDALONE_BOLD_PATT = re.compile(r'^\*\*[^*]+\*\*$')

EMPTY_CLAUSE_RE = re.compile(r'^\s*-\s*\([a-z0-9]+\)\s*$')

BR_LINE_RE = re.compile(r'^\s*<br>\s*$')

CC_LINE_RE = re.compile(r'^\s*CC<br>\s*$')

EMPTY_HEADING_RE = re.compile(r'^#{1,6}\s*$')

IMG_PLACEHOLDER_RE = re.compile(
    r'^\s*\*\*==> picture \[\d+ x \d+\] intentionally omitted <==\*\*\s*$'
)
PAGE_NUM_RE = re.compile(r'^\s*Page \d+\s*$')

PAGE_NUM_ROMAN_RE = re.compile(
    r'^\s*Page (i|ii|iii|iv|v|vi|vii|viii|ix|x|xi|xii|xiii|xiv|xv)\s*$',
    re.IGNORECASE,
)

# Standalone standard reference like "AS 1428.1-2009" or "AS/NZS 3500.1:2018"
STANDARD_REF_RE = re.compile(
    r'^AS(?:\s*/\s*NZS\s*)?[\s/]*\d+(?:\.\d+)*[-:]\s*\d{4}\s*$'
)

# URLs that appear as header/footers
URL_RE = re.compile(
    r'^www\.[a-zA-Z0-9.-]+\.(?:org|com|gov|net|edu)(?:\.au)?(?:\s*/\s*\S+)?\s*$',
    re.IGNORECASE,
)

# "Accessed by UNIVERSITY OF CANBERRA on 16 Apr 2014 ..."
ACCESS_NOTICE_RE = re.compile(
    r'^Accessed by\s+.+on\s+\d+\s+\w+\s+\d{4}',
)

# Standalone bare number (1-3 digits, no decimal) -- page number artifact
BARE_NUMBER_RE = re.compile(r'^\d{1,3}$')

# Orphaned table rows: just pipes and spaces
ORPHAN_PIPE_RE = re.compile(r'^\s*\|[\s|]*\|?\s*$')

START_MARKER = '**----- Start of picture text -----**<br>'
END_MARKER_PATT = re.compile(r'\*\*----- End of picture text -----\*\*(?:<br>)?')

BOLD_CELL_RE = re.compile(r'\|\*\*([^*]+?)\*\*(?=\||$)')

MIN_GIBBERISH_WORDS = 4

# ---------------------------------------------------------------------------
# Boilerplate headings to strip (the Standards Australia intro section)
# ---------------------------------------------------------------------------
BOILERPLATE_HEADINGS = {
    "Standards Australia",
    "Australian Standards\u00ae",
    "Australian Standards\u00ae\u2014",
    "Australian Standards\u00ae \u2014",
    "Australian Standards",
    "International Involvement",
    "Sales and Distribution",
}


def is_gibberish(line: str) -> bool:
    """Detect corrupted OCR/header lines with unusual character patterns."""
    words = line.split()
    if len(words) < MIN_GIBBERISH_WORDS:
        return False
    single_short = sum(1 for w in words if len(w) <= 2 and not w.isalpha())
    prop_short = single_short / len(words)
    mean_word_len = sum(len(w) for w in words) / len(words)
    if prop_short > 0.35:
        return True
    if mean_word_len < 1.8:
        return True
    return False


def clean_bold_table_cells(line):
    if line.startswith('#'):
        return line
    if '|' not in line:
        return line
    return BOLD_CELL_RE.sub(lambda m: '|' + m.group(1), line)


def strip_boilerplate(lines):
    """
    Remove the Standards Australia introductory boilerplate section that
    appears at the start of most Australian Standard documents.

    Detects the first '## Standards Australia' heading and removes everything
    from there until the next non-boilerplate heading is found.
    Returns (new_lines, removed_count) where removed_count tracks how many
    content lines were stripped.
    """
    # Find the '## Standards Australia' heading
    start_idx = None
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped == '## Standards Australia':
            start_idx = i
            break

    if start_idx is None:
        return lines, 0

    # From start_idx forward, find the first heading that is NOT a
    # boilerplate heading -- that's our stop point.
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        raw = lines[i]
        stripped = raw.strip()
        # Look for ## headings
        hm = re.match(r'^##\s+(.+?)(?:\s*\{#.*\})?\s*$', stripped)
        if hm:
            heading_text = hm.group(1).strip()
            if heading_text not in BOILERPLATE_HEADINGS:
                end_idx = i
                break

    removed = end_idx - start_idx
    new_lines = lines[:start_idx] + lines[end_idx:]
    return new_lines, removed


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()

    if not original_lines:
        return None

    # Pre-pass: remove Standards Australia boilerplate
    original_lines, boilerplate_removed = strip_boilerplate(original_lines)

    stats = {
        'image_placeholders': 0,
        'picture_text_starts': 0,
        'picture_text_ends': 0,
        'page_numbers': 0,
        'header_footers': 0,
        'bold_table_cells_cleaned': 0,
        'standalone_bold': 0,
        'empty_clauses': 0,
        'br_removed': 0,
        'gibberish': 0,
        'boilerplate': boilerplate_removed,
        'standard_refs': 0,
        'urls': 0,
        'access_notices': 0,
        'bare_numbers': 0,
        'blank_pages': 0,
    }

    new_lines = []

    for raw_line in original_lines:
        line = raw_line.rstrip('\n')

        if '\ufffd' in line:
            line = line.replace('\ufffd', '')

        if IMG_PLACEHOLDER_RE.match(line):
            stats['image_placeholders'] += 1
            continue

        if START_MARKER in line:
            line = line.replace(START_MARKER, '')
            stats['picture_text_starts'] += 1
        m = END_MARKER_PATT.search(line)
        if m:
            line = line[:m.start()] + line[m.end():]
            stats['picture_text_ends'] += 1

        stripped = line.strip()

        if not stripped:
            new_lines.append(line + '\n')
            continue

        if PAGE_NUM_RE.match(stripped) or PAGE_NUM_ROMAN_RE.match(stripped):
            stats['page_numbers'] += 1
            continue

        if stripped in HEADER_FOOTER_LINES:
            stats['header_footers'] += 1
            continue

        if STANDALONE_BOLD_PATT.match(stripped):
            stats['standalone_bold'] += 1
            continue

        if EMPTY_CLAUSE_RE.match(stripped):
            stats['empty_clauses'] += 1
            continue

        if BR_LINE_RE.match(stripped):
            stats['br_removed'] += 1
            continue

        if CC_LINE_RE.match(stripped):
            stats['br_removed'] += 1
            continue

        if EMPTY_HEADING_RE.match(stripped):
            stats['empty_clauses'] += 1
            continue

        if '....' in line and not line.startswith('#'):
            stats['header_footers'] += 1
            continue

        if STANDARD_REF_RE.match(stripped):
            stats['standard_refs'] += 1
            continue

        if URL_RE.match(stripped):
            stats['urls'] += 1
            continue

        if ACCESS_NOTICE_RE.match(stripped):
            stats['access_notices'] += 1
            continue

        if BARE_NUMBER_RE.match(stripped):
            stats['bare_numbers'] += 1
            continue

        if ORPHAN_PIPE_RE.match(stripped):
            stats['header_footers'] += 1
            continue

        if is_gibberish(stripped):
            stats['gibberish'] += 1
            continue

        new_line = clean_bold_table_cells(line)
        if new_line != line:
            stats['bold_table_cells_cleaned'] += 1
            line = new_line

        new_lines.append(line + '\n')

    combined_new = ''.join(new_lines)
    combined_orig = ''.join(original_lines)

    if combined_new != combined_orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return stats

    return {k: 0 for k in stats}


def main():
    if not os.path.isdir(MD_DIR):
        print(f"Error: directory not found: {MD_DIR}")
        return

    md_files = sorted(f for f in os.listdir(MD_DIR)
                      if f.lower().endswith('.md'))

    if not md_files:
        print(f"No .md files found in {MD_DIR}")
        return

    total = {
        'files_modified': 0,
        'image_placeholders': 0,
        'picture_text_starts': 0,
        'picture_text_ends': 0,
        'page_numbers': 0,
        'header_footers': 0,
        'bold_table_cells_cleaned': 0,
        'standalone_bold': 0,
        'empty_clauses': 0,
        'br_removed': 0,
        'gibberish': 0,
        'boilerplate': 0,
        'standard_refs': 0,
        'urls': 0,
        'access_notices': 0,
        'bare_numbers': 0,
        'blank_pages': 0,
    }

    for filename in md_files:
        filepath = os.path.join(MD_DIR, filename)
        stats = process_file(filepath)
        if stats is None:
            print(f"  {filename}: empty file")
            continue
        if any(v > 0 for v in stats.values()):
            total['files_modified'] += 1
            for k in total:
                if k != 'files_modified':
                    total[k] += stats[k]
            parts = [f"{k.replace('_', ' ').title()}: {v}"
                     for k, v in stats.items() if v > 0]
            print(f"  {filename}: {', '.join(parts)}")
        else:
            print(f"  {filename}: no changes")

    print()
    if total['files_modified'] > 0:
        parts = [f"{k.replace('_', ' ').title()}: {v}"
                 for k, v in total.items()
                 if k != 'files_modified' and v > 0]
        print(f"Modified {total['files_modified']} file(s)")
        print(f"Total: {', '.join(parts)}")
    else:
        print("No files were modified.")


if __name__ == '__main__':
    main()
