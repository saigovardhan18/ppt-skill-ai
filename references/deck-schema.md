# JSON deck specification
Required top-level: `title` (string), `slides` (array). Optional: `theme` (academic|business|technical|creative), `author`.
Each slide requires `layout` and `title`, with layout-specific fields documented in layouts.md.
Example:
```json
{"title":"How DuckDB Works","theme":"technical","slides":[{"layout":"title","title":"DuckDB","subtitle":"Analytics without a database server"},{"layout":"process","title":"Queries run in-process","steps":["Load DuckDB library","Read local or remote data","Execute vectorized SQL","Return results"]},{"layout":"closing","title":"Key takeaway","subtitle":"Fast analytics with minimal setup"}]}
```
JSON must be valid; no comments or trailing commas. Chart categories and values must have the same nonzero length.

## V3 color theory metadata
Optional root-level fields: `color_reference` (default `Johannes Itten — The Art of Color`), `color_strategy` (one or more of hue, light-dark, cold-warm, complementary, simultaneous, saturation, extension), `palette_rationale` (short justification), and `design_intent`. Metadata documents decisions; it does not replace actual accessibility checks.
