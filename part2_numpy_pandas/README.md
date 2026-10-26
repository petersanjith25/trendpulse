# part2_numpy_pandas

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


# Part 2: NumPy and Pandas — TrendPulse

## Overview

This module applies NumPy and Pandas to analyze YouTube Trending Videos data across available countries.

## Learning Objectives

- Convert Pandas columns into NumPy arrays using `.to_numpy()`.
- Inspect array shapes and data types.
- Perform safe division and min-max normalization.
- Calculate a weighted engagement score and log-transformed views.
- Identify records in the top 10% of engagement scores.
- Build a days-by-countries matrix and use broadcasting.
- Concatenate datasets and investigate data-quality issues.
- Filter records, merge category information, and aggregate statistics.
- Calculate days to trend and observed trending lifespan.

## Data Files

Place the required country CSV files and `categories.csv` in the local `data/` directory.

The notebook uses whichever country files are available in its configuration. At least one country CSV and a compatible category lookup are required to run all exercises.

## Notebook

Open `part2_numpy_pandas.ipynb` and run the cells in order.

## Engagement Score

The educational score uses min-max normalized metrics:

- Views: 40%
- Likes: 35%
- Comments: 25%

The weights emphasize reach while also considering audience interaction. This score is a custom analytical measure, not a standard engagement rate or trained machine learning model.

## Data Quality

The notebook investigates duplicate composite keys, invalid trending dates, missing descriptions, and likely deleted/private video placeholders. It documents row counts before and after the category left merge.

## Requirements

```bash
python -m pip install pandas numpy jupyter
```

## Run Independently

From this directory:

```bash
jupyter notebook part2_numpy_pandas.ipynb
```

Ensure the required files exist in `data/`. Paths are relative to this Part so the notebook can run independently.

## Limitations

Results depend on the countries and date ranges available in the supplied datasets. Trending-record counts and observed trending lifespan do not represent all YouTube uploads or views.
