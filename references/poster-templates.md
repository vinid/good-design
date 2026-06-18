# Poster Templates

Use posters for one result or one argument, not a whole paper dump.

## Fixed-Canvas Poster

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Research Poster</title>
<style>
  :root {
    --bg: #0e0c0a;
    --paper: #f1ead8;
    --muted: #9a9488;
    --rule: #3a3530;
    --accent: #ff5b1e;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { background: #2a2624; font-family: "Geist", -apple-system, sans-serif; }
  body { display: grid; place-items: center; min-height: 100vh; padding: 48px; }
  .poster {
    width: 1080px;
    height: 1080px;
    background: var(--bg);
    color: var(--paper);
    padding: 72px 80px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .meta, footer { display: flex; justify-content: space-between; color: var(--muted); }
  .meta { font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; }
  h1 {
    font-family: "Fraunces", Georgia, serif;
    font-size: 76px;
    line-height: 1.04;
    font-weight: 400;
    letter-spacing: -0.025em;
    max-width: 12ch;
  }
  .accent { color: var(--accent); }
  .evidence {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    border-top: 1px solid var(--rule);
    padding-top: 34px;
  }
  .num { font-variant-numeric: tabular-nums; color: var(--accent); font-size: 34px; font-weight: 600; }
  .label { color: var(--muted); font-size: 14px; line-height: 1.35; }
  footer { border-top: 1px solid var(--rule); padding-top: 28px; font-size: 14px; }
  @page { size: 1080px 1080px; margin: 0; }
  @media print {
    * { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
    body { padding: 0; background: var(--bg); }
  }
</style>
</head>
<body>
<main class="poster">
  <div class="meta"><span>PROJECT NAME</span><span>VENUE / YEAR</span></div>
  <h1>Main result in one sentence with <span class="accent">the number</span>.</h1>
  <section class="evidence">
    <div><div class="num">2x</div><div class="label">faster than best human baseline</div></div>
    <div><div class="num">$500</div><div class="label">per problem</div></div>
    <div><div class="num">4</div><div class="label">fields with public verifiers</div></div>
    <div><div class="num">1st</div><div class="label">on benchmark</div></div>
  </section>
  <footer><span>paper / code / source</span><span>authors or affiliation</span></footer>
</main>
</body>
</html>
```

## Poster Rules

- One dominant claim. Everything else supports it.
- Make the most important number the largest, darkest, or closest to the headline.
- Put source, paper, code, verifier, or affiliation in the footer.
- Use fixed canvas dimensions and `@page` matching the canvas.
- Hide debug controls in print if you add them.
- Use local fonts for export-heavy posters.

## Local Pattern

- `examples/research_poster.html`: dark editorial poster with one large claim and four result tiles.
