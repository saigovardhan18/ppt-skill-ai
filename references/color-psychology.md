# Color theory foundation: Johannes Itten — The Art of Color

**Selected primary reference:** Johannes Itten, *The Art of Color* (1961 English-language edition; original German work *Kunst der Farbe*). This is a foundational design/color-theory reference, **not** a clinical or experimentally validated psychology-of-color manual. Do not claim to quote or reproduce the book. These rules are an original operational interpretation of widely documented Itten concepts; consult an authorized copy for precise edition-specific claims.

## Seven color contrasts (Itten framework)
1. **Hue contrast:** Use clearly distinguishable hues for categories, sparingly; do not use arbitrary rainbow palettes.
2. **Light–dark contrast:** Make title, body, and focal elements legible through luminance differences; prioritize accessibility.
3. **Cold–warm contrast:** Use relative temperature to differentiate foreground/background or narrative phases; do not assert universal emotional effects.
4. **Complementary contrast:** Use complementary hues for a *small* focal accent; avoid large high-saturation adjacent fields.
5. **Simultaneous contrast:** Colors change appearance in context; inspect accent on its actual neighboring backgrounds.
6. **Saturation contrast:** Reserve saturated colors for highlights; mute secondary elements to avoid competing focal points.
7. **Extension/proportion contrast:** Balance visually strong colors with their occupied area; 60/30/10 is an optional modern heuristic, **not** an Itten rule.

## Deterministic palette decision process
1. Identify audience, intent, subject, setting, cultural considerations and accessibility needs.
2. Choose a light or dark neutral foundation, with high-contrast foreground.
3. Pick one main accent and optionally one supporting accent using a named contrast strategy from the seven above.
4. Assign semantic roles (background, text, accent, support, warning) and keep them stable.
5. Check WCAG contrast: at least 4.5:1 normal text and 3:1 large text; do not encode meaning using color alone.
6. Check actual neighboring colors for simultaneous contrast and saturation overload.
7. Document `palette_rationale`, `color_strategy`, and `color_reference` in deck spec.

## Example context palettes (original suggestions, not copied from the book)
- Academic: dark `142B49`, accent `117C83`, background `F4F8FA`; light–dark + restrained cold–warm.
- Business: dark `14233C`, accent `2865C7`, background `F5F7FB`; light–dark + saturation contrast.
- Technical: dark `17232E`, accent `087F9C`, background `F1F6F8`; light–dark + hue contrast.
- Creative: dark `40244D`, accent `D15E6E`, background `FBF5F7`; cold–warm + saturation contrast.

## Responsible claims
Do not state blue always creates trust or red always creates urgency. Associations are contextual and culturally variable. Cite the book only for color theory concepts, not unsupported behavioral outcomes. If the user provides legally accessible excerpts, refine these interpretations to match those excerpts.
