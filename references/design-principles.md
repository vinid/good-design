# Design Principles

## Typography

Use a small type system:

- **Research posters:** Fraunces for large titles, Geist for body, JetBrains Mono for metrics and labels.
- **Data figures:** Sora for labels and titles, DM Mono for counts, ticks, scores, and model IDs.
- **LaTeX-style figures:** Helvetica/Arial for labels, Times-style italic for math annotations.

Rules:

- Use tabular numerals for metrics.
- Use uppercase mono labels sparingly.
- Keep labels close to the data they explain.
- Do not use random bold text. Bold only when it changes the read order.
- Load local `woff2` fonts for export-heavy posters.

## Color

Use palettes with roles, not vibes.

TTT dark editorial:

```css
--ink: #0e0c0a;
--paper: #f1ead8;
--paper-dim: #9a9488;
--rule: #3a3530;
--accent: #ff5b1e;
```

Voicenego data figures:

```css
--ink: #0f172a;
--muted: #64748b;
--faint: #94a3b8;
--grid: #e2e8f0;
--panel: #f8fafc;
--success: #16a34a;
--warning: #f59e0b;
--error: #dc2626;
--blue: #2563eb;
```

Rules:

- One accent color should carry the headline result.
- Model identity colors and semantic colors should not collide.
- Use row tints at very low opacity, around `0.03`, for grouping.
- Use gray for baselines and old results.
- Use red only for wrong, dangerous, or failed outcomes.

## Plot Design Rules

Apply Tufte principles from `references/tufte-principles.md` and `references/analytical-design.md`.

Checklist:

- Show data variation, not design variation.
- Show the comparison directly.
- Use dots for individual observations when possible.
- Use a line or tick for mean/summary, not a heavy decorative bar.
- Keep gridlines faint or remove them.
- Label values at the point of use.
- Use the same scale across small multiples.
- Make legends small; prefer direct labels when space allows.
- If the visual effect exaggerates the data effect, fix the scale.
- Every non-data element must earn its ink.

For tables:

- Keep borders sparse.
- Use horizontal rules only to group.
- Highlight the winning row or changed value, not the whole table.
- Put units in headers.
- Align numbers on decimals when possible.

For benchmark graphics:

- Always show the baseline.
- State whether higher or lower is better.
- Show public verifier or review status when trust matters.
- Avoid vague "SOTA" claims without the number and comparison.

## Choosing Plot Types

- **Exact before/after:** slopegraph, paired labels, or two-number comparison.
- **Many categories, one metric:** sorted dot plot or horizontal bars.
- **Repeated tasks or conditions:** small multiples with identical scales.
- **Individual runs matter:** dot plot with mean tick.
- **Distribution shifts:** density curves or ridgelines on a shared axis.
- **Process or mechanism:** diagram with boxes and arrows.
- **Qualitative conditions:** matrix with semantic colors.
- **Benchmark tables:** table only if exact values matter more than shape.

## Copy

Write like a researcher with taste, not a product page.

Good:

- `$500 per problem. Four fields. All four: first.`
- `Prompt a frozen model. Pick the best guess.`
- `Train on this problem. The weights change.`
- `Submissions are on AtCoder. Anyone can verify.`

Avoid:

- "This changes everything."
- "A paradigm shift."
- "Game-changing breakthrough."
- "Unlocking the future of..."
- "Dive into..."
- "Not just X, but Y" unless the contrast is genuinely needed.

Rules:

- Use specific nouns and numbers.
- Short lines beat polished filler.
- If a claim sounds like marketing, replace it with evidence.
- Do not oversell beyond the paper. Bend framing, not facts.
- Mention uncertainty or caveats only when the visual claim needs them.

## Common Failure Modes

- **Beautiful but wrong:** geometry or scale changed while recreating a paper figure. Measure the source.
- **PNG masquerading as HTML:** user asked for editable figure but got an image crop. Rebuild in SVG.
- **Pixel-traced SVG:** faithful but not editable. Use only if asked for exact pixel reproduction.
- **Poster as paper figure:** too much display type, not enough labels.
- **Paper figure as poster:** precise but visually flat; missing hierarchy.
- **Font mismatch in export:** webfonts did not load. Preload fonts and wait before screenshot.
- **Controls in output:** hide debug UI with print CSS.
- **Too many equal sections:** real evidence is uneven. Let important findings take more space.
- **Decorative color:** every color should mean something.
