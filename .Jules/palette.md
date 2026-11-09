# Palette's Journal - Critical UX & Accessibility Learnings

## 2026-10-20 - Skip Link & Focus Rings in Dark Fixed-Nav Interfaces
**Learning:** In single-page dark executive portfolios with fixed/sticky headers (`position: fixed`), keyboard and screen reader users are trapped tabbing through repetitive navigation links unless a dedicated skip link is placed as the first interactive element. Furthermore, default dark browser outlines are invisible against dark slate/onyx backgrounds (`#08090C`), requiring explicit `:focus-visible` rings with high-contrast accent colors (`var(--accent-cyan)`) and adequate offset.
**Action:** When working on dark single-page portfolios with sticky navigation, always provide a `.skip-to-content` link positioned off-screen until focused, and declare a global `:focus-visible` rule using the accent palette.
