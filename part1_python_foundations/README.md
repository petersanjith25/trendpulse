# part1_python_foundations

This part contains its own local copies of the project data.

## Data files

- `categories.csv`
- `GBvideos.csv`
- `INvideos.csv`
- `USvideos.csv`

## Data preparation notes

No columns were removed. All source CSV files were 100 MB or smaller.

## Reproduce

Place the required original CSV files in the root `source_data/` folder and run `python prepare_data.py`.



# Part 1: Core Python — TrendPulse

## Overview

This module introduces core Python programming concepts through the YouTube Trending Videos dataset. It focuses on loading, cleaning, processing, and classifying video records.

## Learning Objectives

- Configure file paths, countries, and analysis thresholds.
- Load CSV files with Pandas and convert data into lists of dictionaries.
- Handle missing and invalid values using `try/except`.
- Parse trending dates using `datetime.strptime()`.
- Work with lists, dictionaries, tuples, and sets.
- Understand local and global variable scope.
- Practice `for` loops, `while` loops, `break`, and `continue`.
- Write reusable functions and implement rule-based video classification.

## Dataset

Place the required files in the `data/` directory:

- `USvideos.csv` — US trending video records.
- `GBvideos.csv` — UK trending video records, if available.
- `categories.csv` — video category IDs and names.

The notebook can run with just the US dataset. Countries whose files are missing are skipped.

## Notebook

Open `part1_core_python.ipynb` and run the cells in order.

The notebook includes configuration, loading, cleaning, data structures, scope demonstrations, title features, video classification, and refactoring.

## Data Cleaning Decisions

- Drop records with missing video IDs or titles.
- Drop records with invalid views or trending dates.
- Substitute zero for invalid likes, dislikes, and comment counts while tracking failures.
- Parse dates using `%y.%d.%m`.

These substitutions are simplifying assumptions. A zero substituted for missing engagement data does not represent a verified actual count.

## Requirements

Install the dependencies:

```bash
python -m pip install pandas jupyter
```

## Run Independently

From the `part1_python_foundations/` directory:

```bash
jupyter notebook part1_core_python.ipynb
```

Ensure the CSV files are present in the local `data/` directory.

## Output

The notebook reports the number of loaded and cleaned records, conversion failures, unique video IDs, the top 15 channels, category counts by country, title features, and rule-based video classifications.

## Limitations

The classification uses manually defined thresholds. It is intended for learning Python and data processing, not as a predictive machine learning model.
