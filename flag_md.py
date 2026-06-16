"""
flag_md.py - Audit tool that flags remaining artifacts in MD files
for manual review AFTER running clean_md.py.

Usage:
    python flag_md.py                        # print report to console
    python flag_md.py --save                 # save report to md/clean_report.md
"""

import os
import re
import sys

MD_DIR = r'F:\OneDrive\Documents\20. AI\PDI_RAG\md'

# Patterns that warrant a flag
FLAG_PATTERNS = {
    'unicode_replacement': re.compile(r'\ufffd'),
    'stray_bold_border': re.compile(r'^\|?\s*\*\*[\s*]*\*\*\s*\|?$'),
    'orphan_pipe': re.compile(r'^\s*\|[\s|]*\|?\s*$'),
    'stray_br': re.compile(r'^\s*<br>\s*$'),
    'stray_cc': re.compile(r'^\s*CC<br>\s*$'),
    'image_placeholder': re.compile(
        r'==> picture \[\d+ x \d+\] intentionally omitted'
    ),
    'start_marker': re.compile(r'\*\*----- Start of picture text -----\*\*'),
    'end_marker': re.compile(r'\*\*----- End of picture text -----\*\*'),
    'page_number': re.compile(r'^\s*Page \d+\s*$', re.IGNORECASE),
    'page_roman': re.compile(r'^\s*Page (i|ii|iii|iv|v|vi|vii|viii|ix|x)\s*$', re.IGNORECASE),
}


def flag_file(filepath):
    """Return (filename, list_of_flags) for a given MD file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filename = os.path.basename(filepath)
    flags = []

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip('\n')
        for label, pat in FLAG_PATTERNS.items():
            if pat.search(line):
                flags.append((i, label, line[:120]))
                break  # one flag per line

    return filename, flags


def main():
    if not os.path.isdir(MD_DIR):
        print(f"Error: {MD_DIR} not found")
        return

    md_files = sorted(f for f in os.listdir(MD_DIR) if f.lower().endswith('.md'))

    report_lines = []
    total_files_with_issues = 0
    total_flags = 0

    report_lines.append("=" * 72)
    report_lines.append(" MD CLEAN REPORT - Artifacts needing manual review")
    report_lines.append("=" * 72)
    report_lines.append("")

    for fname in md_files:
        fpath = os.path.join(MD_DIR, fname)
        filename, flags = flag_file(fpath)

        if not flags:
            continue

        total_files_with_issues += 1
        total_flags += len(flags)

        report_lines.append(f"  {filename}")
        report_lines.append(f"  {'-' * len(filename)}")
        # Group by flag type
        from collections import Counter
        type_counts = Counter(label for _, label, _ in flags)
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            report_lines.append(f"    {t}: {c}x")
        # Show first 5 examples
        report_lines.append(f"    (first {min(5, len(flags))} examples:)")
        for idx, (lineno, label, snippet) in enumerate(flags[:5]):
            safe = snippet.replace('\ufffd', '?')
            report_lines.append(f"      L{lineno} [{label}]: {safe}")
        report_lines.append("")

    report_lines.append("=" * 72)
    report_lines.append(
        f" {total_files_with_issues} file(s) with {total_flags} total flag(s)"
    )
    report_lines.append("=" * 72)

    report = '\n'.join(report_lines)
    print(report)

    if '--save' in sys.argv:
        out_path = os.path.abspath(os.path.join(MD_DIR, os.pardir, 'clean_report.md'))
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport saved to: {out_path}")


if __name__ == '__main__':
    main()
