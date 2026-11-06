# Palette's Journal - Critical UX Learnings

## 2026-11-06 - Accessible Navigation & Fixed Header Focus
**Learning:** Single-page executive landing pages with fixed/sticky headers often lack keyboard access to jump past repeated navigation bars, and anchor jumps often obscure section headings without `scroll-margin-top`. Providing an accessible skip link alongside consistent `:focus-visible` styling dramatically boosts keyboard usability while matching dark-theme aesthetics.
**Action:** When working on fixed-navigation landing pages, always ensure a skip-to-content link exists, offset scroll targets to avoid sticky-header clipping, and style interactive `:focus-visible` rings using high-contrast design tokens.
