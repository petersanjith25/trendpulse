
from pathlib import Path
import csv
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "source_data"

PARTS = [
    "part1_python_foundations",
    "part2_numpy_pandas",
    "part3_visualization_eda",
    "part4_sql_spreadsheet",
]

DROP_COLUMNS = {"description", "tags", "thumbnail_link"}
LIMIT_BYTES = 100 * 1024 * 1024

# Copy the required CSV files into each part.
csv_files = list(SOURCE.glob("*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No CSV files found in source_data. "
        "Check that the dataset is downloaded and categories are converted."
    )

for part in PARTS:
    data_dir = ROOT / part / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    notes = []

    for source_file in csv_files:
        destination = data_dir / source_file.name
        size = source_file.stat().st_size

        if size > LIMIT_BYTES:
            # Stream the CSV to avoid loading a large file into memory.
            with source_file.open(
                "r", encoding="utf-8-sig", newline=""
            ) as src, destination.open(
                "w", encoding="utf-8", newline=""
            ) as dst:
                reader = csv.reader(src)
                writer = csv.writer(dst)

                header = next(reader)
                removed = [
                    col for col in header if col in DROP_COLUMNS
                ]
                kept_indices = [
                    i for i, col in enumerate(header)
                    if col not in DROP_COLUMNS
                ]

                writer.writerow([header[i] for i in kept_indices])

                for row in reader:
                    writer.writerow([
                        row[i] for i in kept_indices if i < len(row)
                    ])

            if removed:
                notes.append(
                    f"- **{source_file.name}:** Removed columns "
                    f"`{', '.join(removed)}` because the original "
                    "file exceeded 100 MB."
                )
            else:
                notes.append(
                    f"- **{source_file.name}:** Exceeded 100 MB; "
                    "no specified columns were present to remove."
                )
        else:
            shutil.copy2(source_file, destination)

    readme = [
        f"# {part}",
        "",
        "This part contains its own local copies of the project data.",
        "",
        "## Data files",
        "",
    ]

    readme.extend(f"- `{f.name}`" for f in csv_files)
    readme.extend(["", "## Data preparation notes", ""])

    if notes:
        readme.extend(notes)
    else:
        readme.append(
            "No columns were removed. All source CSV files were "
            "100 MB or smaller."
        )

    readme.extend([
        "",
        "## Reproduce",
        "",
        "Place the required original CSV files in the root "
        "`source_data/` folder and run `python prepare_data.py`.",
        "",
    ])

    (ROOT / part / "README.md").write_text(
        "\n".join(readme), encoding="utf-8"
    )

    print(f"Prepared {part}/data")

print("Finished copying data to all four parts.")
