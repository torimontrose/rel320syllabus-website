# REL 320 Syllabus Website — Editing Guide

This is a plain HTML/CSS/JavaScript website. There's no build step, no
installs, and no command line needed to edit it — just open the file in a
text editor, change the text, save, and refresh your browser.

## Files

```
syllabus website/
├── index.html      ← all the syllabus content lives here
├── css/styles.css   ← colors, fonts, spacing (rarely needs editing)
├── js/tabs.js        ← makes the tabs work (you shouldn't need to touch this)
└── README.md         ← this file
```

**You will do almost all of your editing inside `index.html`.**

## How to edit the content

1. Open `index.html` in any text editor (TextEdit in plain-text mode,
   VS Code, Notepad, etc.).
2. Use Find (Cmd+F / Ctrl+F) to search for `EDIT:` — every spot that still
   needs your attention has an `<!-- EDIT: ... -->` comment above or next
   to it.
3. Save the file, then open `index.html` in your browser (double-click it,
   or drag it into a browser window) to see your changes.

### Things still marked for your attention

- **Meeting time**: carried over from Fall 2025 (Tue/Thu 8:30–9:45 AM) —
  confirm this is still correct for Fall 2026.
- **Final quiz date/time/location** (Graded Elements tab and Weekly
  Schedule tab): Furman's Fall 2026 final exam period is Dec 10–16, but
  the specific slot for this class's meeting time needs to be confirmed.
- **Field trip date** (Weekly Schedule tab): the Great Tree Women's Zen
  Temple field trip date is a placeholder pending the temple's
  availability — confirm and update.
- **"Wellness Day"** (Weekly Schedule tab): last year's schedule canceled
  a class for a university Wellness Day. The Fall 2026 date wasn't
  available when this site was built — add it if/when announced.
- **Bhikkuni Ordination Game**: this game's rules, roles, paper prompt,
  and rubric weren't finalized in the source syllabus yet. It's a
  placeholder in the Graded Elements tab (and its rubric slot on the
  Rubrics tab) — fill both in once details are set.

### Editing a table (grading breakdown, schedule, rubric)

Tables are built from repeating blocks that look like this:

```html
<tr><td>1</td><td>Tue. 8/25</td><td>Framing Gender and Buddhism</td><td>...</td><td></td></tr>
```

Each `<tr>...</tr>` is one row. Each `<td>...</td>` inside it is one cell.
To edit a class session, find its row (search the date) and edit the text
inside the `<td>` tags.

### Editing a policy block

Policies live in blocks like this — just edit the text between the tags:

```html
<div class="policy-block">
  <h3>Course Activity Recordings</h3>
  <p>Your policy text goes here.</p>
</div>
```

## Publishing the site

This site is static, so you can host it almost anywhere for free:

- **GitHub Pages** — push this folder to a GitHub repo and enable Pages in
  the repo settings (same process used for the FYW 1323 and REL 224
  syllabus sites).
- **Your university's web space** — many schools give faculty a personal
  web folder (ask your IT department).
- **Netlify / Vercel** — drag-and-drop the folder onto their dashboard.

You can also just email students the `index.html` file, or post it to your
LMS (Moodle) as a file — it will open correctly in any browser without
needing to be "hosted" anywhere.

## Accessibility notes (please keep these intact)

This site was built to meet WCAG accessibility guidelines for students
with disabilities:

- Tabs work with keyboard navigation (arrow keys, Home/End) and are
  announced correctly by screen readers.
- There's a "Skip to main content" link for keyboard users.
- Color contrast between text and backgrounds meets AA standards.
- Tables use proper header cells (`<th scope="col">`) so screen readers
  can announce column headers with each cell.
- The print stylesheet forces black-on-white text for anyone who prints
  the syllabus.
- The decorative lotus background is marked `aria-hidden="true"` so
  screen readers skip over it entirely — it's purely visual.

## Changing colors or fonts

Open `css/styles.css` and look at the top of the file, inside the `:root {
... }` block. Every color used on the site is defined there once — change
a value there (e.g. `--copper: #c98a4b;`) and it updates everywhere that
color is used.
