---
name: -ppt-master
description: Create polished, editable PowerPoint presentations from topics, notes, documents, or research. Use when asked to make a PPT, slide deck, pitch deck, lecture, research presentation, or technical presentation.
---

#  PPT Master v3 — Itten Color Theory Edition

Create a coherent, accurate, attractive, fully editable PPTX. Use the local Python scripts bundled with this skill. Never claim to have rendered or inspected slides unless the relevant commands succeeded.

## Workflow
1. Read `references/color-psychology.md`, `references/visual-patterns.md`, `references/llm-evidence.md`, then `references/storytelling.md`, `references/design-rules.md`, `references/layouts.md`, and `references/quality-checklist.md`.
2. Extract topic, audience, purpose, slide count, and constraints. When unspecified, choose sensible defaults: 8 slides, 16:9, accessible typography, no unsupported claims. Ask only if a missing detail blocks progress.
3. Create a slide outline: each slide needs one takeaway headline, a purpose, and supporting evidence. Avoid filler and repetitive layouts.
4. Choose a palette using Johannes Itten’s seven color contrasts as interpreted in `references/color-psychology.md`. Select and record a specific contrast strategy. Treat color associations as contextual design heuristics, NOT universal scientific laws. Consider cultural audience, subject, emotional tone, readability, and accessibility. Prefer a deliberate 60/30/10 balance where useful; never sacrifice contrast. Record `palette_rationale`, `design_intent`, `color_strategy`, and `color_reference` (`Johannes Itten — The Art of Color`) in the deck JSON. The JSON can include `palette` with `dark`, `accent`, `background` hex values to override the preset.
5. Choose visual patterns deliberately: contrast, alignment, proximity, repetition, hierarchy, negative space, and progressive disclosure. Match layouts to information shape, not arbitrary decoration.
6. Use LLM-assisted synthesis carefully: extract claims and numbers from provided documents, separate facts from interpretations, tag unverifiable content, never invent sources, and build a claim/evidence table before writing slide text. See `references/llm-evidence.md`.
7. Select a design preset appropriate to context: `academic`, `business`, `technical`, or `creative`. Choose `technical` for architecture and engineering topics; `academic` for teaching/research; `business` for strategy/pitches; `creative` for narrative/portfolio work.
8. Build a UTF-8 JSON deck specification according to `references/deck-schema.md`. Each slide has a supported `layout` and concise content. Do not fabricate statistics, citations, or quotes. Put citations in a sources slide when research is used.
9. Run `python scripts/generate_ppt.py deck.json output.pptx` from this skill directory (or use absolute script paths). Install dependencies from `requirements.txt` first.
10. Run `python scripts/validate_slides.py output.pptx`. Fix reported problems in the JSON and regenerate. If LibreOffice is installed, optionally render using `python scripts/render_preview.py output.pptx preview/` and visually inspect the exported PDF/pages. If not available, state that visual rendering was not performed.
11. Deliver the actual PPTX file and a brief explanation of slide structure. If the runtime cannot execute scripts or attach files, provide the JSON specification and clear instructions instead of claiming generation succeeded.

## Quality constraints
- Editable native text/shapes/charts; no rasterized slide backgrounds.
- One key message per slide. No walls of text; target <= 5 bullets, <= 14 words each.
- Use contrasting text, 28–40pt titles, 18–24pt body where practical.
- Preserve safe margins and alignment; use meaningful layout variation.
- Charts must have units, labeled categories, and truthful numeric values.
- Use `speaker_notes` when more explanation is needed.
- Avoid arbitrary external imagery. V1 prioritizes native shapes, diagrams and charts.
- If an unsupported layout is requested, adapt it to the closest supported one and disclose the limitation.

## Script support
`generate_ppt.py` supports title, bullets, two_column, process, comparison, quote, metrics, chart, and closing layouts. `validate_slides.py` performs structural checks, not pixel-perfect collision detection. Optional LibreOffice rendering supports manual visual QA.

## Color and layout rules
- Default to palette selection informed by context, not rigid mappings such as “blue always means trust.”
- Use a limited palette: background, primary text, accent, and optional neutral/support color.
- Verify contrast: target WCAG 4.5:1 for normal text and 3:1 for large text; never rely on hue alone to communicate meaning.
- Avoid visual pattern overload. Select one dominant composition per slide, consistent grid, and intentional visual rhythm across slides.
- Default color theory reference: Johannes Itten, *The Art of Color*. Apply the seven contrast principles as a practical interpretation; do not claim to have read a full copyrighted edition or invent page citations. If the user supplies authorized excerpts, use those for more specific guidance.
