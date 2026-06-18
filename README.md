# Design Good Figures

A Cursor Agent Skill for designing scientific posters, publication figures, plots, diagrams, and benchmark visuals in HTML/SVG.

The goal is simple: make research visuals that are clear enough for experts, polished enough for public presentation, and still editable as code.

## What This Skill Helps With

- Research posters with one strong claim and clear supporting evidence
- Publication figures built as editable HTML/SVG
- Benchmark comparison plots
- Outcome matrices and small multiples
- Annotated screenshots
- Complex plots where Python generates geometry and HTML/SVG handles design
- PDF/PNG export workflows

The skill combines practical HTML/SVG templates, Tufte-style plotting principles, contained examples, and small support scripts.

## Install In Cursor

In Cursor:

1. Open `Settings`
2. Go to `Rules`
3. Click `Add Rule`
4. Choose `Remote Rule (GitHub)`
5. Enter:

```text
https://github.com/vinid/design-good-figures
```

Cursor should discover the skill from `SKILL.md`.

Manual install:

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/vinid/design-good-figures ~/.cursor/skills/design-good-figures
```

## Repository Structure

```text
.
├── SKILL.md
├── references/
│   ├── analytical-design.md
│   ├── design-principles.md
│   ├── examples.md
│   ├── export-recipes.md
│   ├── figure-shells.md
│   ├── plot-templates.md
│   ├── poster-templates.md
│   └── tufte-principles.md
├── examples/
│   ├── figure_runtime.html
│   ├── fraud_instruction_variants.html
│   ├── grounded_fraud_instruction_variants.html
│   ├── grounded_fraud_instruction_variants.pdf
│   ├── outcome_matrix.html
│   ├── random_complex_plot.html
│   ├── random_ridgeline_plot.html
│   ├── research_poster.html
│   └── vocal_cue_detection.html
├── scripts/
│   ├── export_pdf.py
│   ├── generate_fraud_instruction_variants.py
│   └── generate_ridgeline_demo.py
└── data/
    └── fraud_instruction_variants.csv
```

## Design Philosophy

Good figures should answer:

- What is the claim?
- Compared to what?
- What is the evidence?
- Can the viewer verify the scale, units, and baseline?
- Did design clarify the data, or decorate it?

For complex plots, use Python as a geometry engine, not as the art director:

1. Python computes points, densities, layouts, contours, or paths.
2. The output remains editable HTML/SVG.
3. Typography, spacing, color, labels, annotations, and export are handled in the figure shell.

## Included Examples

Open these directly in a browser:

- `examples/research_poster.html`
- `examples/outcome_matrix.html`
- `examples/random_complex_plot.html`
- `examples/random_ridgeline_plot.html`
- `examples/grounded_fraud_instruction_variants.html`

The grounded example is generated from:

```text
data/fraud_instruction_variants.csv
```

Regenerate it with:

```bash
python scripts/generate_fraud_instruction_variants.py
```

## Export To PDF

Use the contained PDF exporter:

```bash
python scripts/export_pdf.py examples/grounded_fraud_instruction_variants.html examples/grounded_fraud_instruction_variants.pdf
```

The exporter uses headless Chrome or Chromium.

## When To Use The Skill

Use this skill when asking Cursor to:

- design a new scientific figure
- critique a figure
- recreate a paper plot as editable SVG
- make a research poster
- improve a benchmark chart
- generate a plot from data
- export a figure to PDF

## Rule Of Thumb

If the plot is simple, write SVG directly.

If the plot is complex, generate the geometry with a script, then finish the figure in HTML/SVG.

If it is only a PNG crop, it is not an editable figure.
