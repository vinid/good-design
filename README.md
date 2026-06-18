# Design Good Figures

A Cursor Agent Skill for designing scientific posters, publication figures, plots, diagrams, and benchmark visuals in HTML/SVG.

The goal is simple: make research visuals that are clear enough for experts, polished enough for public presentation, and still editable as code.

## Gallery

<table>
  <tr>
    <td><img src="examples/swe_bench_lite_comparison.png" alt="SWE-bench Lite benchmark comparison" /></td>
    <td><img src="examples/random_complex_plot.png" alt="Complex scatter and density plot" /></td>
    <td><img src="examples/research_poster.png" alt="Research poster example" /></td>
  </tr>
  <tr>
    <td><sub>Benchmark card with uncertainty</sub></td>
    <td><sub>Complex plot with generated geometry</sub></td>
    <td><sub>Claim-first research poster</sub></td>
  </tr>
</table>

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

## Install For Other Agents

`design-good-figures` follows the Agent Skills format: a directory with `SKILL.md` frontmatter plus optional `references/`, `scripts/`, `examples/`, and `data/` folders. That makes it portable to agents that support Agent Skills.

With the Agent Skills CLI:

```bash
npx skills add vinid/design-good-figures --agent cursor
npx skills add vinid/design-good-figures --agent claude-code
npx skills add vinid/design-good-figures --agent codex
```

Manual project installs:

```bash
git clone https://github.com/vinid/design-good-figures .agents/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures .cursor/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures .claude/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures .codex/skills/design-good-figures
```

Manual global installs:

```bash
git clone https://github.com/vinid/design-good-figures ~/.agents/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures ~/.cursor/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures ~/.claude/skills/design-good-figures
git clone https://github.com/vinid/design-good-figures ~/.codex/skills/design-good-figures
```

Cursor also discovers compatible skills from `.agents/skills/`, `.claude/skills/`, `.codex/skills/`, and their user-level equivalents.

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
│   ├── random_complex_plot.png
│   ├── random_ridgeline_plot.html
│   ├── research_poster.html
│   ├── research_poster.png
│   ├── swe_bench_lite_comparison.html
│   ├── swe_bench_lite_comparison.png
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

### Benchmark Comparison

`examples/swe_bench_lite_comparison.html` is a compact benchmark-card example: a claim-first title, grouped bars, visible uncertainty, direct value labels, and a source note in one export-ready HTML/SVG file. The gallery preview is a transparent PNG generated from that HTML.

Open these directly in a browser:

- `examples/swe_bench_lite_comparison.html`
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
