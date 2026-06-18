from pathlib import Path
import math
import random


random.seed(17)

base = Path(__file__).resolve().parents[1]
out = base / "examples" / "random_ridgeline_plot.html"

W = 940
H = 620
left = 118
right = 790
top = 96
row_gap = 82
axis_y = top + row_gap * 5
xmin = -2.9
xmax = 3.1

series = [
    ("Frozen search", "#94a3b8", -1.15, 0.62, 120),
    ("Prompt memory", "#64748b", -0.55, 0.58, 120),
    ("Self-refine", "#2563eb", 0.18, 0.54, 120),
    ("TTT step 24", "#3b82f6", 0.86, 0.48, 120),
    ("TTT step 49", "#ff5b1e", 1.52, 0.38, 120),
]


def sx(x):
    return left + (x - xmin) / (xmax - xmin) * (right - left)


def density(samples, x):
    bw = 0.28
    norm = 1 / (len(samples) * bw * math.sqrt(2 * math.pi))
    total = 0.0
    for sample in samples:
        z = (x - sample) / bw
        total += math.exp(-0.5 * z * z)
    return total * norm


paths = []
samples_by_name = []
for row, (name, color, mu, sigma, n) in enumerate(series):
    samples = [random.gauss(mu, sigma) for _ in range(n)]
    samples_by_name.append((name, color, samples))
    baseline = top + row * row_gap
    xs = [xmin + i / 120 * (xmax - xmin) for i in range(121)]
    vals = [density(samples, x) for x in xs]
    peak = max(vals)
    coords = [(sx(x), baseline - val / peak * 54) for x, val in zip(xs, vals)]
    d = f"M {sx(xmin):.2f} {baseline:.2f} "
    d += " ".join(f"L {x:.2f} {y:.2f}" for x, y in coords)
    d += f" L {sx(xmax):.2f} {baseline:.2f} Z"
    mean_x = sum(samples) / len(samples)
    p90 = sorted(samples)[int(len(samples) * 0.9)]
    paths.append(
        f'<path d="{d}" fill="{color}" opacity="0.28" stroke="{color}" stroke-width="2.2"/>'
    )
    paths.append(
        f'<line x1="{sx(mean_x):.2f}" y1="{baseline - 60:.2f}" x2="{sx(mean_x):.2f}" y2="{baseline + 7:.2f}" stroke="{color}" stroke-width="2"/>'
    )
    paths.append(
        f'<circle cx="{sx(p90):.2f}" cy="{baseline - 24:.2f}" r="4.4" fill="{color}" opacity="0.9"/>'
    )
    paths.append(
        f'<text x="{left - 18}" y="{baseline - 8:.2f}" text-anchor="end" font-family="Sora,sans-serif" font-size="12" font-weight="600" fill="#0f172a">{name}</text>'
    )
    paths.append(
        f'<text x="{sx(mean_x) + 8:.2f}" y="{baseline - 64:.2f}" font-family="DM Mono,monospace" font-size="9.5" fill="#64748b">mean {mean_x:+.2f}</text>'
    )

sample_ticks = []
for name, color, samples in samples_by_name:
    for sample in random.sample(samples, 22):
        sample_ticks.append(
            f'<line x1="{sx(sample):.2f}" y1="{axis_y + 9}" x2="{sx(sample):.2f}" y2="{axis_y + 15}" stroke="{color}" stroke-width="1" opacity="0.35"/>'
        )

paths_text = "\n  ".join(paths)
sample_ticks_text = "\n  ".join(sample_ticks)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Random Ridgeline Plot Demo</title>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 32px;
    background: #f8fafc;
    font-family: "Sora", sans-serif;
  }}
  .card {{
    width: min(100%, 1000px);
    background: #ffffff;
    border-radius: 18px;
    padding: 32px 36px 28px;
    box-shadow: 0 2px 8px rgba(15,23,42,.06), 0 18px 48px rgba(15,23,42,.10);
  }}
  svg {{ width: 100%; height: auto; display: block; }}
</style>
</head>
<body>
<div class="card">
<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Random ridgeline density demo">
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <text x="{W / 2}" y="28" text-anchor="middle" font-family="Sora,sans-serif" font-size="16" font-weight="700" fill="#0f172a">Random solution quality distributions over training</text>
  <text x="{W / 2}" y="50" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" fill="#64748b">Python computes distributions and quantiles; SVG handles hierarchy, labels, and annotation</text>

  <line x1="{left}" y1="{axis_y}" x2="{right}" y2="{axis_y}" stroke="#cbd5e1" stroke-width="1.2"/>
  <line x1="{sx(0):.2f}" y1="{top - 64}" x2="{sx(0):.2f}" y2="{axis_y}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="5 5"/>
  <text x="{sx(0):.2f}" y="{top - 72}" text-anchor="middle" font-family="DM Mono,monospace" font-size="10" fill="#94a3b8">old best</text>

  {paths_text}
  {sample_ticks_text}

  <text x="{left}" y="{axis_y + 44}" font-family="DM Mono,monospace" font-size="10" fill="#64748b">lower quality</text>
  <text x="{right}" y="{axis_y + 44}" text-anchor="end" font-family="DM Mono,monospace" font-size="10" fill="#64748b">higher quality</text>
  <text x="{(left + right) / 2}" y="{axis_y + 44}" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="600" fill="#0f172a">same task, same budget, different update rule</text>

  <line x1="806" y1="146" x2="898" y2="146" stroke="#e2e8f0"/>
  <text x="806" y="178" font-family="DM Mono,monospace" font-size="24" font-weight="500" fill="#ff5b1e">+2.67σ</text>
  <text x="806" y="199" font-family="Sora,sans-serif" font-size="11" fill="#64748b">right-shift in mean</text>
  <text x="806" y="239" font-family="DM Mono,monospace" font-size="24" font-weight="500" fill="#0f172a">p90</text>
  <text x="806" y="260" font-family="Sora,sans-serif" font-size="11" fill="#64748b">marked as dots</text>
  <text x="806" y="306" font-family="Sora,sans-serif" font-size="11" font-weight="700" fill="#ff5b1e">final distribution</text>
  <text x="806" y="326" font-family="Sora,sans-serif" font-size="11" fill="#64748b">narrower and shifted right</text>

  <text x="{W / 2}" y="{H - 20}" text-anchor="middle" font-family="Sora,sans-serif" font-size="10" fill="#94a3b8">Random demo data · generated with scripts/generate_ridgeline_demo.py · editable SVG</text>
</svg>
</div>
</body>
</html>
"""

out.write_text(html)
print(out)
