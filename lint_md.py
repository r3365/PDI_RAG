import os
import re
from pathlib import Path


MD_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\md'

CLOSING_NUMBER_RE = re.compile(r'^\s*-\s*\(\d+\)\s*$')
CLOSING_LETTER_RE = re.compile(r'^\s*-\s*\([a-z]\)\s*$')
CLOSING_ROMAN_RE = re.compile(r'^\s*-\s*\((?:iv|iii?|vi{0,3})\)\s*$')
EMPTY_CLAUSE_RE = re.compile(r'^\s*-\s*\([a-z0-9]+\)\s*$')

IMG_PLACEHOLDER_RE = re.compile(
    r'^\s*\*\*==> picture \[\d+ x \d+\] intentionally omitted <==\*\*\s*$'
)
PAGE_NUM_RE = re.compile(r'^\s*Page \d+\s*$')

STANDALONE_BOLD_RE = re.compile(r'^\*\*[^*]+\*\*$')

BR_LINE_RE = re.compile(r'^\s*<br>\s*$')

TOC_DOTS_RE = re.compile(r'\.{4,}\s*\d+\s*$')

SUSPICIOUS_PATTERNS = [
    (r'^\s*CL<br>', 'OCR remnant (CL<br>)'),
    (r'�', 'Unicode replacement character'),
    (r'^\s*•\s*$', 'Empty bullet point'),
]


HEADER_FOOTER_LINES = {
    "ABCB Housing Provisions Standard 2025",
    "NCC 2025 Volume Two - Building Code of Australia",
    "Livable Housing Design Standard 2025",
    "Livable Housing Design",
    "Front matter",
}


def lint_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []
    filename = os.path.basename(filepath)

    for i, raw in enumerate(lines):
        line = raw.rstrip('\n')
        stripped = line.strip()
        lineno = i + 1

        # --- Empty clause markers ---
        if EMPTY_CLAUSE_RE.match(line):
            issues.append((lineno, 'empty_clause',
                           f"Empty clause marker: {stripped}"))

        # --- Image placeholders ---
        if IMG_PLACEHOLDER_RE.match(line):
            issues.append((lineno, 'image_placeholder', stripped))

        # --- Page numbers ---
        if PAGE_NUM_RE.match(line):
            issues.append((lineno, 'page_number', stripped))

        # --- Header / footer known lines ---
        if stripped in HEADER_FOOTER_LINES:
            issues.append((lineno, 'header_footer', stripped))

        # --- Standalone bold that is NOT a heading ---
        if STANDALONE_BOLD_RE.match(stripped) and not stripped.startswith('#'):
            issues.append((lineno, 'standalone_bold', stripped))

        # --- <br> lines ---
        if BR_LINE_RE.match(line):
            issues.append((lineno, 'br_artifact', stripped))

        # --- TOC dots ---
        if TOC_DOTS_RE.search(line) and not stripped.startswith('#'):
            issues.append((lineno, 'toc_dots',
                           f"TOC dots + page num: {stripped[:80]}"))

        # --- Suspicious patterns ---
        for pat, label in SUSPICIOUS_PATTERNS:
            if re.search(pat, line):
                issues.append((lineno, 'suspicious', f"[{label}] {stripped[:100]}"))

        # --- Orphaned content heuristics ---
        # Content lines that start mid-sentence (lowercase) after a blank line
        # might be orphaned clause content
        if i >= 2:
            prev_line = lines[i - 1].rstrip('\n').strip()
            prev_prev = lines[i - 2].rstrip('\n').strip()
            if (not prev_line
                    and prev_prev.endswith(('-', '—', '–'))
                    and stripped
                    and stripped[0].islower()):
                issues.append((lineno, 'orphan_content',
                               f"Possibly orphaned content: {stripped[:100]}"))

    return issues


def report(issues_by_file):
    total_issues = 0
    print("=" * 80)
    print("  MD QUALITY LINT REPORT")
    print("=" * 80)

    for filename in sorted(issues_by_file.keys()):
        issues = issues_by_file[filename]
        if not issues:
            print(f"\n  {filename}: CLEAN")
            continue

        total_issues += len(issues)
        print(f"\n  {filename}: {len(issues)} issue(s)")
        print(f"  {'-' * 60}")

        cats = {}
        for lineno, cat, msg in issues:
            cats.setdefault(cat, []).append((lineno, msg))

        for cat, items in sorted(cats.items()):
            print(f"\n    [{cat}] ({len(items)} occurrences)")
            for lineno, msg in items[:5]:
                safe = msg.encode('ascii', 'replace').decode('ascii')
                print(f"      L{lineno}: {safe}")
            if len(items) > 5:
                print(f"      ... and {len(items) - 5} more")

    print(f"\n{'=' * 80}")
    print(f"  Total issues: {total_issues}")
    print("=" * 80)
    return total_issues


def main():
    md_files = sorted(Path(MD_DIR).glob('*.md'))
    if not md_files:
        print(f"No .md files found in {MD_DIR}")
        return

    issues_by_file = {}
    for md_path in md_files:
        print(f"  Linting: {md_path.name}")
        issues = lint_file(str(md_path))
        issues_by_file[md_path.name] = issues

    report(issues_by_file)


if __name__ == '__main__':
    main()
