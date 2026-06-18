from pathlib import Path
import csv


base = Path(__file__).resolve().parents[1]
data_path = base / "data" / "fraud_instruction_variants.csv"
out = base / "examples" / "grounded_fraud_instruction_variants.html"

rows = list(csv.DictReader(data_path.open()))

scenario_labels = {
    "Wire fraud calm": ("Wire fraud", "calm transfer"),
    "Wire fraud frightened": ("Wire fraud", "frightened transfer"),
    "Welfare callback crying": ("Welfare callback", "crying caller"),
}
conditions = ["Attend", "Override"]
models = ["Gemini Live", "OpenAI Realtime"]
scenario_order = ["Wire fraud calm", "Wire fraud frightened", "Welfare callback crying"]
outcome_colors = {
    "correct": "#16a34a",
    "wrong": "#dc2626",
    "warning": "#f59e0b",
}

row_by_key = {}
for row in rows:
    key = (row["scenario"], row["condition"], row["model"])
    row_by_key[key] = row

condition_x = {"Attend": 314, "Override": 646}
model_x = {
    ("Attend", "Gemini Live"): 198,
    ("Attend", "OpenAI Realtime"): 363,
    ("Override", "Gemini Live"): 530,
    ("Override", "OpenAI Realtime"): 695,
}
scenario_y = {
    "Wire fraud calm": 142,
    "Wire fraud frightened": 198,
    "Welfare callback crying": 254,
}

marks = []
for scenario in scenario_order:
    label, sublabel = scenario_labels[scenario]
    y = scenario_y[scenario]
    marks.append(f'<text x="30" y="{y + 4}" font-family="Sora,sans-serif" font-size="10.5" font-weight="700" fill="#0f172a">{label}</text>')
    marks.append(f'<text x="30" y="{y + 18}" font-family="Sora,sans-serif" font-size="8.5" fill="#94a3b8">{sublabel}</text>')
    for condition in conditions:
        for model in models:
            row = row_by_key[(scenario, condition, model)]
            numerator = int(row["numerator"])
            denominator = int(row["denominator"])
            color = outcome_colors[row["outcome"]]
            x = model_x[(condition, model)] - 40
            width = 72 * numerator / denominator
            marks.append(f'<rect x="{x}" y="{y}" width="72" height="9" rx="4.5" fill="#e2e8f0"/>')
            if numerator > 0:
                marks.append(f'<rect x="{x}" y="{y}" width="{width:.1f}" height="9" rx="4.5" fill="{color}"/>')
            marks.append(f'<text x="{x + 80}" y="{y + 9}" font-family="DM Mono,monospace" font-size="8.5" fill="#64748b">{numerator}/{denominator}</text>')

marks_text = "\n  ".join(marks)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: transparent; display: flex; justify-content: center; align-items: flex-start;
          padding: 24px; font-family: Sora, sans-serif; }}
  .card {{ background: white; border-radius: 16px; padding: 24px 28px 20px;
           box-shadow: 0 2px 8px rgba(0,0,0,.06), 0 8px 32px rgba(0,0,0,.07);
           max-width: 940px; width: 100%; }}
  svg {{ width: 100%; height: auto; display: block; }}
</style>
<title>Grounded Fraud Instruction Variants</title>
</head>
<body>
<div class="card">
<svg viewBox="0 0 884 312" xmlns="http://www.w3.org/2000/svg">
  <rect width="884" height="312" fill="#ffffff"/>
  <text x="442" y="24" text-anchor="middle" font-family="Sora,sans-serif" font-size="14" font-weight="600" fill="#0f172a">Instruction shifts affective decisions</text>
  <text x="442" y="42" text-anchor="middle" font-family="Sora,sans-serif" font-size="10" fill="#64748b">Bars generated from data/fraud_instruction_variants.csv</text>

  <text x="314" y="74" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="700" fill="#0f172a">Attend</text>
  <text x="314" y="88" text-anchor="middle" font-family="Sora,sans-serif" font-size="8.5" fill="#94a3b8">pay attention to how caller sounds</text>
  <text x="646" y="74" text-anchor="middle" font-family="Sora,sans-serif" font-size="11" font-weight="700" fill="#0f172a">Override</text>
  <text x="646" y="88" text-anchor="middle" font-family="Sora,sans-serif" font-size="8.5" fill="#94a3b8">do not act on words alone</text>

  <text x="198" y="115" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">Gemini Live</text>
  <text x="363" y="115" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">OpenAI Realtime</text>
  <text x="530" y="115" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">Gemini Live</text>
  <text x="695" y="115" text-anchor="middle" font-family="Sora,sans-serif" font-size="9" font-weight="600" letter-spacing="0.06em" fill="#94a3b8">OpenAI Realtime</text>

  <rect x="14" y="128" width="856" height="44" rx="8" fill="#f8fafc"/>
  <rect x="14" y="184" width="856" height="44" rx="8" fill="#f8fafc"/>
  <rect x="14" y="240" width="856" height="44" rx="8" fill="#f8fafc"/>

  {marks_text}

  <line x1="458" y1="108" x2="458" y2="286" stroke="#e2e8f0" stroke-width="1.2"/>
</svg>
</div>
</body>
</html>
"""

out.write_text(html)
print(out)
