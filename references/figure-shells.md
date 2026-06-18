# Figure Shells

Use these for paper figures, plot cards, diagrams, and annotated screenshots.

## Publication Figure Shell

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: transparent;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 24px;
    font-family: "Sora", sans-serif;
  }
  .card {
    background: white;
    border-radius: 16px;
    padding: 24px 28px 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,.06), 0 8px 32px rgba(0,0,0,.07);
    max-width: 900px;
    width: 100%;
  }
  svg { width: 100%; height: auto; display: block; }
</style>
</head>
<body>
<div class="card">
<svg viewBox="0 0 850 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="360" fill="#ffffff" />
  <text x="425" y="24" text-anchor="middle" font-family="Sora,sans-serif" font-size="14" font-weight="700" fill="#0f172a">Figure title states the comparison</text>
  <text x="425" y="42" text-anchor="middle" font-family="Sora,sans-serif" font-size="10" fill="#64748b">Subtitle explains dots, bars, scale, or sample size</text>
</svg>
</div>
</body>
</html>
```

## Rules

- Body background: `transparent` for paper export.
- SVG: explicit `viewBox`, `width: 100%`, `height: auto`.
- Use SVG-native shapes for charts and diagrams.
- Use measured coordinates when recreating a paper plot.
- Do not use screenshots, PNG crops, or pixel-traced SVG when the user asks for an editable figure.
- Pixel-traced SVG is only acceptable when the user explicitly asks for exact pixel reproduction over editability.

## Annotated Screenshots

Use screenshots only as a substrate, not as the whole figure. Put labels outside the screenshot, draw thin callout lines and dots, and keep the screenshot itself unmodified when possible.

Pattern:

```html
<div class="figure">
  <div class="annotation problem">Problem<br>Description</div>
  <div class="annotation-line line-left-problem"></div>
  <div class="annotation-dot dot-left-problem"></div>
  <img class="platform-image" src="screenshot.png" alt="Platform view">
</div>
```

```css
.figure { position: relative; padding: 0 180px; }
.platform-image { width: 100%; display: block; border-radius: 14px; border: 1px solid #1f2937; }
.annotation { position: absolute; font-size: 25px; font-weight: 700; color: #1e40af; text-align: center; }
.annotation-line { position: absolute; height: 2px; background: #3b82f6; }
.annotation-dot { position: absolute; width: 5px; height: 5px; border-radius: 50%; background: #3b82f6; }
```

For a contained example of figure-card structure, see `examples/outcome_matrix.html`.
