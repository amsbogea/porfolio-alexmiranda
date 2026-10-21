## 2026-10-21 - Accessible Keyboard Navigation & Skip Link Pattern
**Learning:** Dark executive portfolio themes require explicit high-contrast focus rings (`:focus-visible`) using primary accent colors (`--accent-cyan`) and an off-screen skip link to ensure keyboard navigation accessibility without disrupting the visual layout for mouse users.
**Action:** Always verify keyboard focus states and add a skip link (`.skip-to-content`) targeting `<main id="main-content">` when structuring landing pages or single-page applications.
