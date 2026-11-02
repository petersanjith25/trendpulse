import json
import csv
from pathlib import Path

source = Path("source_data/CA_category_id.json")
output = Path("source_data/categories.csv")

with source.open("r", encoding="utf-8") as f:
    data = json.load(f)

rows = []

for item in data["items"]:
    snippet = item.get("snippet", {})

    rows.append({
        "category_id": item.get("id"),
        "category_name": snippet.get("title"),
        "assignable": snippet.get("assignable"),
    })

with output.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["category_id", "category_name", "assignable"],
    )
    writer.writeheader()
    writer.writerows(rows)

print(f"Converted {len(rows)} categories to {output}")