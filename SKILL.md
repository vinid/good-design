---
name: design-good-figures
description: Design and critique high-quality scientific posters, plots, and publication figures in HTML/SVG. Use when creating or improving research posters, paper figures, SVG charts, benchmark visuals, diagrams, annotated screenshots, or export-ready visual assets. Includes copy-pasteable HTML/SVG templates, Tufte references, export scripts, and contained examples.
---

# Design Good Figures

Design research visuals that survive expert scrutiny, communicate the result quickly, and export cleanly. Use this skill for HTML/SVG posters, paper figures, plots, diagrams, and annotated screenshots.

## Quick Start

Before writing code:

1. State the claim in one sentence.
2. Name the comparison: baseline, human, previous SOTA, condition, or model.
3. Pick the figure type: poster, plot, matrix, small multiple, benchmark chart, diagram, or annotated screenshot.
4. Inventory every value needed for the visual: point estimates, denominators, uncertainty bounds, labels, units, dates, and source text.
5. If any required value is missing, ask the user. Do not infer, estimate, digitize from pixels, or add "approximate" values unless the user explicitly asks for estimation.
6. Choose one visual hierarchy: title, evidence, source.
7. Reserve separate layout lanes for title, subtitle, legend, plot area, value labels, uncertainty marks, annotations, axis labels, and source notes.
8. Build the figure as editable HTML/SVG unless the user explicitly asks for a raster image.

Use numbers in the claim when possible: `$500`, `2x faster`, `1st place`, `16x larger improvement`.

## Which Reference To Load

- `references/poster-templates.md`: fixed-canvas poster shells, typography, and layout patterns.
- `references/figure-shells.md`: publication figure wrappers, SVG card shells, annotated screenshot structure.
- `references/plot-templates.md`: copy-pasteable SVG plot templates: small multiples, outcome matrices, runtime plots, dot plots.
- `references/design-principles.md`: typography, color, Tufte rules, plot selection, copy rules, failure modes.
- `references/tufte-principles.md`: graphical excellence, integrity, data-ink, chartjunk, small multiples, data density.
- `references/analytical-design.md`: analytical design, sparklines, layering, micro/macro design, causality.
- `references/export-recipes.md`: Chrome and Playwright export commands and scripts.
- `references/examples.md`: local files worth copying from.

## Final Review

Before calling a poster or figure done:

- [ ] The main claim is visible in 2 seconds.
- [ ] The exact comparison is visible without reading the caption.
- [ ] The important number is larger, darker, or closer to the title.
- [ ] Baselines and units are clear.
- [ ] Every plotted value, uncertainty mark, denominator, and source note came from the user or a cited source.
- [ ] No missing values were guessed, digitized from pixels, or silently approximated.
- [ ] Labels, legends, value text, whiskers, callouts, badges, and captions do not overlap at the final export size.
- [ ] Color has stable meaning.
- [ ] The figure works in grayscale if color is removed.
- [ ] Text survives export at final size.
- [ ] The output file was checked, not just the browser.
- [ ] No chartjunk, fake precision, or marketing filler.
