"""Writes the current national figures into README.md between the summary markers, from data/latest.csv."""

import csv
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((ROOT / "data" / "latest.csv").open(encoding="utf-8")))
national = next(row for row in rows if row["level"] == "national")
n = {key: int(value) for key, value in national.items() if value.isdigit()}
d = date.fromisoformat(national["as_of"])
as_of = f"{d:%B} {d.day}, {d.year}"
addressing_h1b = n["h1b_yes"] + n["h1b_no"]
refusal = round(100 * n["h1b_no"] / addressing_h1b) if addressing_h1b else 0
specialties = sum(row["level"] == "specialty" for row in rows)
states = sum(row["level"] == "state" for row in rows)

summary = f"""<!-- summary:start -->
**As of {as_of}:**

| | Programs |
| --- | ---: |
| Websites read | {n["programs_read"]:,} |
| State a visa or IMG policy | {n["state_visa_or_img_policy"]:,} |
| Accept J-1 physicians | {n["j1_yes"]:,} |
| Sponsor H-1B | {n["h1b_yes"]:,} |
| Say they do not sponsor H-1B | {n["h1b_no"]:,} ({refusal}% of those that address H-1B) |
| Offer both | {n["j1_and_h1b"]:,} |
| Consider IMGs without naming a visa | {n["img_without_visa_named"]:,} |

{specialties} specialty rows and {states} state rows in [`data/latest.csv`](data/latest.csv).
<!-- summary:end -->"""

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
readme.write_text(re.sub(r"<!-- summary:start -->.*?<!-- summary:end -->", summary, text, flags=re.S), encoding="utf-8")
print(f"README summary updated for {as_of}")
