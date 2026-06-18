# Export Recipes

Always inspect the exported PNG/PDF, not only the browser view.

## Chrome Poster Export

```bash
chrome --headless --disable-gpu \
  --force-device-scale-factor=3 \
  --window-size=1080,1200 \
  --virtual-time-budget=4000 \
  --screenshot=output.png input.html
```

Use a taller window than the card height to avoid clipping.

## Chrome PDF Export

```bash
chrome --headless --disable-gpu \
  --print-to-pdf=output.pdf \
  --print-to-pdf-no-header \
  --no-pdf-header-footer input.html
```

In poster HTML, add:

```css
@page { size: 1080px 1080px; margin: 0; }
@media print {
  * { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  body { padding: 0; }
}
```

Contained script:

```bash
python scripts/export_pdf.py examples/grounded_fraud_instruction_variants.html examples/grounded_fraud_instruction_variants.pdf
```

## Playwright Figure Export

- Wait for fonts before capture.
- Capture the `.card` bounding box, not the full viewport.
- Use `omitBackground: true` for transparent paper figures.
- Use a larger viewport than the figure to avoid clipping shadows.

Reusable exporter:

```js
const { chromium } = require("playwright");

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1400, height: 900 },
    deviceScaleFactor: 2
  });

  await page.goto(`file://${process.argv[2]}`);
  await page.waitForTimeout(1200);

  const card = await page.locator(".card").boundingBox();
  await page.screenshot({
    path: process.argv[3],
    clip: {
      x: card.x - 32,
      y: card.y - 32,
      width: card.width + 64,
      height: card.height + 64
    },
    omitBackground: true
  });

  await browser.close();
})();
```

## Export Pitfalls

- If fonts look wrong, preload local `woff2` files or wait longer before capture.
- If colors wash out in PDF, add `print-color-adjust: exact`.
- If the output has debug UI, hide `.controls` in print.
- If a shadow is clipped, expand the screenshot clip box.
- If the PDF background should be transparent, use Playwright with `omitBackground: true`.

## Support Scripts

Use support scripts when a plot needs generated geometry: densities, contours, layouts, sampled points, heatmap cells, or paths.

Pattern:

- Python computes coordinates and SVG marks.
- The output is an HTML file with editable SVG.
- The script uses the skill palette, fonts, card shell, labels, and export conventions.
- Keep generated examples under `examples/`.
- Keep reusable generators under `scripts/`.

Contained examples:

- `scripts/generate_ridgeline_demo.py` writes `examples/random_ridgeline_plot.html`.
- `scripts/generate_fraud_instruction_variants.py` reads `data/fraud_instruction_variants.csv` and writes `examples/grounded_fraud_instruction_variants.html`.
