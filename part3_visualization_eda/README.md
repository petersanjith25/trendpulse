# part3_visualization_eda

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

# Part 3: Visualization and EDA — TrendPulse

## Overview

This module explores YouTube Trending Videos data using Matplotlib, Plotly, NumPy, and Pandas.

## Learning Objectives

- Profile and clean data from multiple countries.
- Create five Matplotlib charts and two interactive Plotly charts.
- Calculate mean, median, mode, and IQR-based outliers.
- Interpret correlations without making causal claims.
- Build a sequential video-analysis funnel.
- Estimate observed trending retention and lifespan.
- Analyze cohorts by first-trending month.
- Communicate findings through a numerical briefing.

## Data

Place the required country CSV files in `data/`. The notebook uses the available files and can compare multiple countries when present.

## Notebook

Run `part3_visualization_eda.ipynb` from this directory. Execute cells in order.

## Requirements

```bash
python -m pip install pandas numpy matplotlib plotly jupyter
```

## Methodology

Videos are summarized by country and video ID for peak-view and lifespan analyses. Retention measures continued presence across distinct observed trending dates. Correlations describe associations only.

## Limitations

The dataset contains videos that appeared in trending lists, not all YouTube videos. Observed lifespan may differ from true trending duration because of missing dates and dataset boundaries. Results depend on the countries and time periods provided.

## Reproducibility

Keep the input data in the local `data/` folder, run the notebook from top to bottom, and review the generated numerical briefing before sharing results.
