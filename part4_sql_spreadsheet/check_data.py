from pathlib import Path
import json
import csv

folder = Path("source_data")

for file in folder.iterdir():
    print(file.name, "-", round(file.stat().st_size / (1024 * 1024), 2), "MB")

json_file = folder / "US_category_id.json"
csv_file = folder / "categories.csv"

if json_file.exists():
    with json_file.open("r", encoding="utf-8") as f:
        categories = json.load(f)

    print("Category file format: JSON")
    print("Top-level keys:", list(categories.keys()))

elif csv_file.exists():
    with csv_file.open("r", encoding="utf-8-sig", newline="") as f:
        print("Category file format: CSV")
        print("First row:", next(csv.reader(f), None))

else:
    print("No known category file found. Check the filename.")