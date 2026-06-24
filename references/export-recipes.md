# Export Recipes

Inspect the exported PNG/PDF, not only the browser view — run the verify loop in
`SKILL.md`. These are the export commands it uses.

Current headless Chrome notes: use bare `--headless` (the old headless mode was removed
in Chrome 132; `--headless=new` is now redundant). `--disable-gpu` has been unnecessary
since 2021. `--virtual-time-budget` is still supported and lets time-dependent rendering
settle before capture. Prefer serving over `http://localhost` rather than `file://` when
fonts, fetches, or scripts must load.

## Background Removal

Treat background removal as part of the figure, not as cleanup after export.

- For paper figures, slides, posters, and composite layouts, default to `body { background: transparent; }` and export with transparency.
- Keep a visible card or page background only when it is part of the intended design.
- Do not leave accidental browser, viewport, or page backgrounds around a figure.
- If exporting a transparent PNG with Playwright, use `omitBackground: true`.
- If a browser screenshot cannot preserve transparency, switch to Playwright or export the SVG directly.
- Inspect the exported asset over both light and dark backgrounds before calling it done.

## Chrome Poster Export

```bash
chrome --headless \
  --force-device-scale-factor=3 \
  --window-size=1080,1200 \
  --virtual-time-budget=4000 \
  --screenshot=output.png input.html
```

Use a taller window than the card height to avoid clipping.

## Chrome PDF Export

Single-page posters and figures only. For multi-slide HTML decks (Reveal.js etc.), do
**not** use `--print-to-pdf` — it reflows to a print layout, not the slide viewports. See
`references/slide-decks.md` for the screenshot-per-slide → stitch path.

```bash
chrome --headless \
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
- If the output has a white rectangle behind the figure, remove the page/card background or use `omitBackground: true`.
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
