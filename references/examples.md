# Local Examples

Use these files as concrete references when designing new visuals.

## Posters

- `examples/research_poster.html`: dark editorial poster with one large claim and four result tiles.

## Paper Figures

- `examples/outcome_matrix.html`: compact outcome matrix with scenario, delivery, expected action, observed action.
- `examples/vocal_cue_detection.html`: small multiples with model rows and compact bars.
- `examples/fraud_instruction_variants.html`: compact comparison figure for instruction variants.
- `examples/grounded_fraud_instruction_variants.html`: same style generated from `data/fraud_instruction_variants.csv`.
- `examples/grounded_fraud_instruction_variants.pdf`: exported PDF from the grounded HTML example.
- `examples/random_complex_plot.html`: random complex plot showing Python-generated geometry finished in HTML/SVG style.
- `examples/random_ridgeline_plot.html`: random ridgeline density plot generated from a support script.

## Recreated Paper Plots

- `examples/figure_runtime.html`: LaTeX-style paper plot recreation. Use SVG geometry, not PNG crops, for editable figures.

## Lessons From This Workspace

- When the user asks for an HTML figure, do not crop the PNG.
- When they ask for an identical editable figure, recreate the structure in SVG and measure coordinates from the source.
- For complex plots, use Python as a geometry generator and HTML/SVG as the final design layer.
- For grounded examples, keep source data in `data/`, generation code in `scripts/`, and output in `examples/`.
- For publication figures, Sora + DM Mono with a white card is the strongest local pattern.
- For editorial posters, Fraunces + Geist + JetBrains Mono gives a strong research identity.
- Specific copy beats polished copy. Use numbers, baselines, and verifiers.
