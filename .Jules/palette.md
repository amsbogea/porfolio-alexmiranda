# Palette's Journal - Critical UX & Accessibility Learnings

## 2026-03-30 - Dark Executive Portfolios Focus Visible Indicators
**Learning:** Dark executive themes often strip default outline styles or lack visible `:focus-visible` ring indicators, making keyboard navigation (Tab key) completely invisible for interactive cards and links.
**Action:** Always provide standard, high-contrast `:focus-visible` outline or ring styles matching the cyan accent palette (`--accent-cyan`) for `a` and `button` elements.
