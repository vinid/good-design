# Execution Discipline

Taste is necessary but not sufficient. Most "looks like shit" verdicts are not taste
problems — they are mechanical: marks leaking out of their boxes, labels colliding,
arrows pointing everywhere, a "best" mark that contradicts its own encoding. These are
cheap to prevent with explicit rules and the verify loop.

The verify loop (edit → screenshot → look at the image → fix) is defined in `SKILL.md`.
Run it on every change that touches geometry, marks, labels, diagrams, or wrapping. The
rules below are what you look for in each screenshot.

## SVG Containment

The #1 figure failure is an element escaping its intended box. The trap is that the DOM
will not warn you, because of how SVG actually clips:

- **`viewBox` never clips.** It is only a coordinate transform — it maps a user-space
  rectangle onto the SVG viewport. It defines the coordinate system, not a clip region.
- **A `<rect>` or `<g>` you draw as a "card" or "panel" does not clip its children at
  all.** It is just paint. A child placed at coordinates beyond that rectangle still
  renders in full.
- **Only viewport-establishing elements clip**, and only when they carry
  `overflow: hidden` — that is the `<svg>` element itself (and `<pattern>`, `<marker>`,
  `<symbol>`, `<image>`, `<foreignObject>`), or an element with an explicit `clipPath`.

So a star badge can hang off a card edge, or a check mark sit past a panel border, and
the bounding boxes will look fine. Only the rendered image reveals it.

Rules:

- **Nothing exceeds its parent box.** If a mark sits at `x + w`, that must be `≤` the
  container's right edge. Same for top and bottom.
- **Labels clear lines and other labels.** Aim for ≥ 8px of separation when space is
  tight; if two things crowd and are not intentionally grouped, move one. In genuinely
  dense small multiples, prefer tight-but-legible over a hard pixel law.
- **Badges, markers, and pills anchor inside, not on the corner.** Inset decorative
  elements from the edge; never straddle it.
- **To actually enforce a box, wrap children in a nested `<svg>` with
  `overflow="hidden"` or apply a `clipPath`** — drawing a `<rect>` around them does
  nothing.
- **Verify containment in the screenshot**, not the DOM.

## Diagram Hygiene

Loop and process diagrams look "random" for the same recurring reasons: mixed arrow
styles, mixed directions, unequal node sizes, freehand placement. Defaults for
flow/process diagrams:

- **One arrow style** for the whole diagram — one head, one weight, one color.
- **One reading direction.** Left → right or top → bottom. Do not mix. (Genuine cycles,
  branching trees, or feedback loops are the deliberate exception, not license to
  scatter arrows.)
- **Equal node geometry.** Boxes that mean the same kind of thing are the same size and
  sit on a shared baseline. Size a node differently only when size encodes something.
- **Prefer a grid over freehand.** Snap nodes to a few x/y tracks. If you are eyeballing
  coordinates, you will get the "random" look.
- **Contain every node and arrow** (see containment rules above).

## Encoding Integrity

If length or position encodes a value, the highlighted or "best" mark must be extremal
in that encoding — the longest bar, or the shortest when lower is better. A green "best"
bar drawn shorter than the gray candidates it beats is a true data-integrity error, not
a style nitpick (the Lie Factor is no longer 1.0). Decide the direction once — "higher is
better" vs "lower is better" — and make every mark, axis, tick, and highlight obey it.
See `references/design-principles.md` and `references/tufte-principles.md` for the Lie
Factor.
