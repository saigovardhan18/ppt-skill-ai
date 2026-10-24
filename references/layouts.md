# Layouts
- title: title, subtitle
- bullets: title, bullets (array of strings)
- two_column: title, left_title, right_title, left (array), right (array)
- process: title, steps (array of 2–5 strings)
- comparison: title, left_title, right_title, left (array), right (array)
- quote: title, quote, attribution
- metrics: title, metrics (array of objects {value,label}, 1–4)
- chart: title, categories (array), values (array of numbers), optional chart_title, unit
- closing: title, subtitle
All layouts optionally accept speaker_notes. Prefer short text. The generator uses editable PowerPoint elements.

## Cross-reference: color system
Follow `color-psychology.md` (Johannes Itten, *The Art of Color*): choose a named contrast strategy, keep semantic color roles stable, and verify contrast. Do not infer unsupported psychological effects from hue.
