# Plot Templates

Copy these SVG blocks into the publication figure shell and adapt coordinates, labels, and colors.

## Small Multiples With Model Rows

Use for comparing models across tasks, conditions, or modalities.

```html
<svg viewBox="0 0 850 326" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="326" fill="#ffffff" />
  <text x="185" y="35" text-anchor="middle" font-family="Sora,sans-serif" font-size="12" font-weight="700" fill="#0f172a">Condition A</text>
  <text x="462" y="35" text-anchor="middle" font-family="Sora,sans-serif" font-size="12" font-weight="700" fill="#0f172a">Condition B</text>
  <text x="739" y="35" text-anchor="middle" font-family="Sora,sans-serif" font-size="12" font-weight="700" fill="#0f172a">Condition C</text>

  <rect x="18" y="66" width="260" height="224" rx="8" fill="#f8fafc" />
  <rect x="295" y="66" width="260" height="224" rx="8" fill="#f8fafc" />
  <rect x="572" y="66" width="260" height="224" rx="8" fill="#f8fafc" />

  <text x="30" y="95" font-family="Sora,sans-serif" font-size="9.5" font-weight="600" fill="#f59e0b">Model A</text>
  <rect x="139" y="84" width="100" height="9" rx="4.5" fill="#e2e8f0" />
  <rect x="139" y="84" width="85" height="9" rx="4.5" fill="#16a34a" />
  <text x="248" y="93" font-family="DM Mono,monospace" font-size="8.5" fill="#64748b">17/20</text>
</svg>
```

Pattern from `examples/vocal_cue_detection.html`.

## Outcome Matrix

Use when the point is a chain of reasoning: scenario, cue, expected action, observed action.

```html
<svg viewBox="0 0 768 378" xmlns="http://www.w3.org/2000/svg">
  <rect width="768" height="378" fill="#ffffff" />
  <text x="113" y="14" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">SCENARIO</text>
  <text x="310" y="14" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">CUE</text>
  <text x="484" y="14" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">EXPECTED</text>
  <text x="676" y="14" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">OBSERVED</text>

  <rect x="8" y="26" width="210" height="52" rx="9" fill="#f1f5f9" />
  <text x="24" y="48" font-family="Sora,sans-serif" font-size="12.5" font-weight="700" fill="#0f172a">Scenario name</text>
  <text x="24" y="65" font-family="Sora,sans-serif" font-size="10" fill="#64748b">Short input text</text>

  <rect x="244" y="26" width="132" height="52" rx="9" fill="#fdeede" />
  <text x="310" y="56" text-anchor="middle" font-family="Sora,sans-serif" font-size="11.5" font-weight="600" fill="#b45309">Cue</text>

  <rect x="400" y="26" width="168" height="52" rx="9" fill="#eafaf0" />
  <text x="484" y="56" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="600" fill="#15803d">Correct action</text>

  <rect x="592" y="26" width="168" height="52" rx="9" fill="#fdeceb" />
  <text x="676" y="56" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="600" fill="#dc2626">Wrong action</text>
</svg>
```

Pattern from `examples/outcome_matrix.html`.

## Benchmark Runtime Plot

Use for lower-is-better comparisons over an ordered axis.

```html
<svg viewBox="0 0 1800 520" xmlns="http://www.w3.org/2000/svg">
  <rect width="1800" height="520" fill="#ffffff" />
  <path d="M2 371H1798" stroke="#111111" stroke-width="4" />

  <path d="M20 371 C80 371 110 260 170 260 C230 260 250 371 330 371 Z"
        fill="rgba(76,122,209,.5)" stroke="#4f72c9" stroke-width="5" />
  <path d="M520 371 C650 371 730 250 850 250 C970 250 1050 371 1160 371 Z"
        fill="rgba(76,122,209,.5)" stroke="#4f72c9" stroke-width="5" />
  <path d="M1450 371 C1540 371 1620 250 1710 250 C1760 250 1780 320 1788 371 Z"
        fill="rgba(76,122,209,.5)" stroke="#4f72c9" stroke-width="5" />

  <line x1="760" y1="120" x2="760" y2="371" stroke="#111" stroke-width="4" stroke-dasharray="14 10" />
  <line x1="1580" y1="120" x2="1580" y2="371" stroke="#111" stroke-width="4" stroke-dasharray="14 10" />
  <line x1="1760" y1="100" x2="1760" y2="371" stroke="#4f72c9" stroke-width="4" stroke-dasharray="14 10" />

  <text x="1580" y="95" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="31" fill="#151515">Best Human</text>
  <text x="1760" y="80" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="31" fill="#4f72c9">Best Method</text>
  <text x="0" y="430" font-family="Helvetica,Arial,sans-serif" font-size="36" fill="#151515">Slowest</text>
  <text x="1797" y="430" text-anchor="end" font-family="Helvetica,Arial,sans-serif" font-size="36" fill="#151515">Fastest</text>
  <text x="900" y="429" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="34" fill="#151515">Benchmark Runtime (lower is better)</text>
</svg>
```

For exact recreations, measure the source image and set the SVG `viewBox` to the source coordinate system. Do not stretch by eye.

## Dot Plot With Mean Tick

Use when individual observations matter.

```html
<svg viewBox="0 0 720 260" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="260" fill="#ffffff" />
  <line x1="100" y1="190" x2="660" y2="190" stroke="#e2e8f0" />
  <text x="80" y="194" text-anchor="end" font-family="DM Mono,monospace" font-size="10" fill="#64748b">0</text>
  <text x="80" y="94" text-anchor="end" font-family="DM Mono,monospace" font-size="10" fill="#64748b">1</text>
  <line x1="100" y1="90" x2="660" y2="90" stroke="#e2e8f0" />

  <text x="100" y="50" font-family="Sora,sans-serif" font-size="12" font-weight="700" fill="#0f172a">Model A</text>
  <circle cx="180" cy="132" r="3.5" fill="#2563eb" opacity=".65" />
  <circle cx="215" cy="118" r="3.5" fill="#2563eb" opacity=".65" />
  <circle cx="250" cy="154" r="3.5" fill="#2563eb" opacity=".65" />
  <line x1="170" y1="128" x2="260" y2="128" stroke="#0f172a" stroke-width="2" />

  <text x="380" y="50" font-family="Sora,sans-serif" font-size="12" font-weight="700" fill="#0f172a">Model B</text>
  <circle cx="460" cy="104" r="3.5" fill="#f59e0b" opacity=".65" />
  <circle cx="495" cy="96" r="3.5" fill="#f59e0b" opacity=".65" />
  <circle cx="530" cy="112" r="3.5" fill="#f59e0b" opacity=".65" />
  <line x1="450" y1="104" x2="540" y2="104" stroke="#0f172a" stroke-width="2" />
</svg>
```

Dots show data variation. The tick shows the summary. Avoid hiding the data behind a single bar unless the individual observations do not matter.
