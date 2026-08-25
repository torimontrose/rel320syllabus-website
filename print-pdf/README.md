# Print PDF syllabus generator

Generates the magazine-style print PDF from the exact text on the live site
(re-transcribed by hand into `rel320_data.py` / `build_rel320.py` — if the
live site's `index.html` changes, these files need to be updated to match).

## Regenerate the PDF

```
python3 build_rel320.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-margins \
  --print-to-pdf="REL320-Syllabus.pdf" --print-to-pdf-no-header \
  "file://$(pwd)/rel320-syllabus.html"
```

Output: `REL320-Syllabus.pdf`, plus `rel320-syllabus.html` (intermediate,
safe to ignore/delete and regenerate).

## Files

- `print-system.css` — shared component library (also used by FYW 1323 and
  REL 224's generators; identical copy in each repo, not linked)
- `gen_schedule.py` — shared schedule-table HTML generator
- `build_rel320.py` — page layout/content for this course
- `rel320_data.py` — schedule row data, transcribed verbatim from the site
- `rel320-cover.jpeg` — cover image (from
  `~/Desktop/1 REL320 Sexuality and Gender in Buddhism/naga kings daughter.jpeg`)

## Rules this must follow (see project memory for full detail)

- White page background (ink-saving for printing) — small dark accent
  blocks (cover hero, schedule title bar, unit dividers) are fine to keep.
- Every line of prose/schedule content must match the live site **exactly**
  — no paraphrasing, no cuts.
- After any rebuild, verify every page's rendered content against the site
  text programmatically (extract PDF text via PyMuPDF, check for expected
  phrases + check no page's content exceeds ~780pt of the 792pt page height)
  before treating it as done.
