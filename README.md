# Urban Energy Forecast

Forecasting regional electricity demand from historical public data

## Problem

Utility companies must decide in advance how much electricity to generate to meet demand.
Overproduction wastes resources and increases costs, while underproduction risks power
shortages and grid instability. Since energy demand fluctuates by hour, day, and season,
accurately forecasting future consumption is essential for balancing cost efficiency with
supply reliability.

## Solution and Features

This project uses historical hourly energy consumption data (PJM Interconnection, covering
multiple U.S. regions from 2002-2018) to forecast future electricity demand. By identifying
daily, weekly, and seasonal consumption patterns, it provides a data-driven basis for supply
planning and helps reduce the gap between predicted and actual demand.

## Tech Stack

- **Python 3.11+** — core language
- **pandas / numpy** — data cleaning and manipulation
- **scikit-learn** — baseline ML models (Random Forest, etc.)
- **statsmodels / Prophet** — time series forecasting
- **matplotlib / plotly** — visualization
- **Streamlit** — interactive dashboard
- **pytest** — unit testing

## Setup

```bash
git clone https://github.com/pouya3883/urban-energy-forecast.git
cd urban-energy-forecast
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Data

Raw data files are not included in this repository. Download the AEP hourly
dataset from [Kaggle](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)
and place `AEP_hourly.csv` inside the `data/` folder before running any scripts.

## Project Structure

## Results

## Tips and Limits
