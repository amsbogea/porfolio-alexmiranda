# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-11-05 - Accessible Focus Visibility in Dark Executive Theming
**Learning:** In dark executive portfolios with rich dark backgrounds (`#07090E`), custom `:focus-visible` styling is essential because default browser outlines can blend into dark surfaces or clash with custom dark borders. Utilizing the primary accent token (`var(--accent-cyan)`) with a clean `outline-offset: 3px` maintains strong WCAG AAA focus visibility while feeling integrated into the cyber/executive design language.
**Action:** When working on dark theme portfolios, pair a skip-to-content navigation pattern (`.skip-link`) with `:focus-visible` outlines matching the design tokens (`--accent-cyan`) and ensure main content regions have `tabindex="-1"` so programmatic focus jumps directly to content without an unintended permanent outline.
