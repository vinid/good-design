from pathlib import Path
import argparse
import shutil
import subprocess


def find_chrome():
    candidates = [
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    raise SystemExit("No Chrome/Chromium executable found.")


parser = argparse.ArgumentParser()
parser.add_argument("input_html")
parser.add_argument("output_pdf")
parser.add_argument("--chrome")
parser.add_argument("--virtual-time-budget", default="4000")
args = parser.parse_args()

input_path = Path(args.input_html).resolve()
output_path = Path(args.output_pdf).resolve()
output_path.parent.mkdir(parents=True, exist_ok=True)

chrome = args.chrome if args.chrome else find_chrome()
cmd = [
    chrome,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--print-to-pdf-no-header",
    f"--virtual-time-budget={args.virtual_time_budget}",
    f"--print-to-pdf={output_path}",
    input_path.as_uri(),
]

subprocess.run(cmd, check=True)
print(output_path)
