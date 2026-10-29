## 2025-05-18 - Visible Focus Rings for Dark Theme Accessibility
**Learning:** Interactive elements in dark-themed web pages require high-contrast focus rings (`:focus-visible` with `outline` and `outline-offset`) to ensure screen reader and keyboard navigation visibility without disrupting mouse click styling.
**Action:** Always define `:focus-visible` with bright theme-accent colors (`var(--accent-cyan)` or high contrast equivalent) and distinct `outline-offset` for interactive elements (`a`, `button`, interactive cards).
