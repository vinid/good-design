# Slide Decks

Posters and figures are a single canvas with a single export. A deck is a **sequence**.
The principles below are tool-agnostic; the Reveal.js section at the end is the worked
example.

`examples/ttt_talk_editorial/` is a full deck that applies these principles. Treat it as
**one example, not a template** — it is a warm-paper editorial style for one talk. Copy
the discipline (sequence, one claim per slide, shared shell, stable color, per-slide
verification), not the styling. Decks do not need to look like this.

## A Deck Is a Sequence, Not One Canvas

- **One claim per slide.** If a slide needs two screenshots to verify, it is two slides.
- **Consistent chrome.** Build one shared shell — folio/header/footer, page number,
  kicker — and reuse it on every slide. Define it once.
- **Stable color meaning across the whole deck**, not just within one figure. If green
  is "our result" on slide 4, green is still "our result" on slide 11. This is the
  per-figure color rule (`references/design-principles.md`) extended across the sequence.
- **Dramaturgy matters as much as any single figure.** Open with the stakes the audience
  cares about (e.g. "open models, ~$500/problem" belongs early, not buried). Close on the
  audience-level takeaway, not an inside-baseline detail.

## Per-Slide Verification

Decks render one slide at a time, so the verify loop (`SKILL.md`) is run **per slide**:

- Add an export mode that hides controls, progress bars, and any debug UI.
- Capture each slide at a fixed viewport — `1280×720` for 16:9 (use `1024×768` for 4:3,
  or a portrait size as needed). Document the aspect ratio you chose.
- Use a 2× device scale factor for HQ captures.
- Inspect each PNG. This is the only reliable way to catch overflow and collisions.

Capture command (current headless Chrome — bare `--headless`, no `--disable-gpu`, served
over HTTP for asset reliability):

```bash
chrome --headless \
  --force-device-scale-factor=2 \
  --window-size=1280,720 \
  --virtual-time-budget=4000 \
  --screenshot=slide_03.png \
  "http://localhost:8000/index.html?export=1#/3"
```

Prefer `http://localhost` over `file://`: hash routing works under `file://`, but fonts,
fetches, and some plugins do not load reliably there.

## PDF Export — the Trap

**The single biggest time-sink:** a deck framework's built-in PDF mode is not the same as
its slide viewports. Reveal's `?print-pdf` deliberately reflows the deck into a print
layout, so applying a single-poster `--print-to-pdf` recipe (see
`references/export-recipes.md`) to a deck produces a broken PDF.

The reliable path:

1. Screenshot every slide at `1280×720` (or `2560×1440` at 2× for HQ) via the export
   route above.
2. Stitch the PNGs into a PDF.

Stitch with Pillow — flatten RGBA onto white (a bare `.convert("RGB")` blackens
transparent regions) and set `resolution` so the page size is sane:

```python
from PIL import Image

def stitch_pdf(png_paths, out_path, dpi=144):
    pages = []
    for p in png_paths:
        img = Image.open(p)
        if img.mode == "RGBA":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        else:
            img = img.convert("RGB")
        pages.append(img)
    pages[0].save(out_path, save_all=True, append_images=pages[1:], resolution=dpi)
```

For a more robust path than hand-rolled stitching, dedicated tools (Decktape,
html2pdf-slides) capture each slide individually and assemble the PDF for you.

## Pagination

Inserting or removing a slide forces renumbering, which produces off-by-one errors.

- **Do not hardcode page numbers.** Render them programmatically — a CSS counter, a
  data-attribute, or the framework's slide-number API — so insert/delete cannot desync
  them.
- Keep a single source of truth for slide order.

## Reveal.js (Worked Example)

The framework-specific mechanics for the rules above:

- **Per-slide route:** navigate with the hash, e.g. `#/3` for slide 3. Reveal reads
  `location.hash` on init and routes there.
- **Export mode:** add an `export=1` URL flag your slide CSS uses to hide `.controls`,
  the progress bar, and debug UI.
- **PDF warning:** Reveal `?print-pdf` ≠ the slide viewport — it is the print stylesheet,
  saved through Chrome's print dialog. For faithful per-slide output use the
  screenshot → stitch path above. (Decktape explicitly does *not* use `?print-pdf`.)
- **Page numbers:** use Reveal's slide-number API rather than hardcoding.
