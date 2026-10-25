## 2026-03-30 - Keyboard Focus & Navigation in Dark Executive Portfolios
**Learning:** In fixed header single-page portfolio layouts with dark themes, default browser focus outlines are often invisible or low contrast against dark backgrounds, and keyboard users are forced to tab through entire fixed navigation bars before reaching main content.
**Action:** Always include a high-contrast skip-to-content link targeted to `<main id="main-content" tabindex="-1">` and define clear `:focus-visible` ring indicators styled with theme accent colors (`--accent-cyan`).
