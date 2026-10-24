# Claude PPT Master 

## Installation (Claude Desktop / Claude Code)
1. Install Python 3.10+ and ensure `python` is available in your terminal.
2. Extract this folder into your Claude skills directory. For Claude Code, use `~/.claude/skills/claude-ppt-master/` (Windows: `%USERPROFILE%\.claude\skills\claude-ppt-master\`). Keep `SKILL.md` at the root of that folder.
3. In a terminal in the extracted folder, run `python -m pip install -r requirements.txt`.
4. Restart Claude Code or start a new conversation. Ask Claude: "Use claude-ppt-master to create an 8-slide presentation about DuckDB."
5. Claude must have access to a local Python execution environment and write permissions to create PPTX files. Uploading SKILL.md alone into a chat without code execution will not run the generator.

## Test manually
`python scripts/generate_ppt.py example-deck.json test.pptx`
`python scripts/validate_slides.py test.pptx`

## Optional visual preview
Install LibreOffice, then run `python scripts/render_preview.py test.pptx preview` to generate a PDF for manual inspection.

## Claude.ai
In Claude's Skills settings (if available for your plan), upload the packaged skill ZIP and follow the interface instructions. Tool and execution availability vary by Claude environment; if Python execution isn't available, use Claude Code locally instead.

## Limitations
This is a working v1 generator, not a full design agent. It supports nine native slide layouts and editable text/shapes/charts. It does not automatically source images, guarantee pixel-perfect text fitting, or perform image-based visual review. Validation is structural and preview is optional.

## V2: Color psychology + visual pattern intelligence
Read `references/color-psychology.md`, `references/visual-patterns.md`, and `references/llm-evidence.md`. Override the preset palette with a JSON `palette` object containing `dark`, `accent`, and `background` six-digit hex colors. The generator rejects insufficient contrast for primary text on the slide background. The heuristics are not a substitute for a specific book; supply its title/excerpts for faithful book-specific rules.

## V3: Johannes Itten color theory integration
The default reference is Johannes Itten, *The Art of Color*. The skill applies the seven color contrasts (hue, light–dark, cold–warm, complementary, simultaneous, saturation, and extension/proportion) as design heuristics. It records `color_reference` and `color_strategy` in deck specifications. Example palettes are original and are not presented as palettes copied from the book.

This package is self-contained: extract it and use the folder. Do not install by copying only SKILL.md; the reference files and scripts are required.
