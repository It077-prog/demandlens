# StaySignal — Dubai Hospitality Demand Intelligence

StaySignal is a Dubai hospitality demand-intelligence portfolio project.

It forecasts quarterly hotel occupancy by classification category and compares a transparent seasonal-naive benchmark against progressively richer models using hotel supply, Dubai airport passenger flows, and overnight visitor signals.

## Project goal

Answer:

> What is likely to happen to Dubai hotel occupancy next, how uncertain is the forecast, which demand signals matter, and should a human planner accept or override the recommendation?

## Data

The project uses public Dubai datasets prepared into a quarterly master table:

- Hotels and Rooms Occupancy Average by Classification Category
- Passengers at Dubai Airports
- Overnight Visitors by Region

Important limitations:

- Hotel occupancy data contains no 2020 observations.
- Overnight visitor data overlaps the modelling table only from 2021 Q1 to 2024 Q2.
- Correlations are descriptive and are not treated as causal evidence.

## 2024 benchmark and model comparison

The initial seasonal-naive benchmark predicts each quarter using the same hotel category and quarter from the previous year.

| Model | Test window | N | MAE | RMSE | MAPE |
|---|---|---:|---:|---:|---:|
| Seasonal naive | 2024 Q1-Q4 | 12 | 0.92 | 1.12 | 1.18% |
| Model A: hotel history + supply | 2024 Q1-Q4 | 12 | 2.33 | 2.96 | 2.93% |
| Model B: Model A + airport signals | 2024 Q1-Q4 | 12 | 1.83 | 2.13 | 2.33% |
| Model C: Model B + visitor signals | 2024 Q1-Q2 | 6 | 1.91 | 2.34 | 2.38% |
| Seasonal naive, matched to Model C window | 2024 Q1-Q2 | 6 | 0.83 | 1.22 | 1.06% |

Current conclusion: the simple seasonal-naive benchmark remains the best validated forecast for the tested 2024 window. The richer models are retained as experiments, not presented as improvements.

## Modelling sequence

1. Seasonal-naive baseline
2. Model A — lagged occupancy + quarter + hotel category + hotel supply
3. Model B — Model A + Dubai airport passenger signals
4. Model C — Model B + overnight visitor signals
5. Compare out-of-sample MAE / RMSE / MAPE
6. Productize only the best defensible forecasting approach

## Structure

```text
data/
  processed/
    demandlens_master.csv
src/
  data.py
  features.py
  baseline.py
  models.py
  evaluate.py
  run_models.py
app/
  streamlit_app.py
tests/
outputs/
  metrics/
```

## Run locally

```bash
pip install -r requirements.txt
pytest -q
python -m src.run_models
streamlit run app/streamlit_app.py
```

## Methodology

- Time-series splits only; no random train/test split.
- 2020 is kept missing rather than synthetically interpolated.
- Lag features use exact calendar quarters, so the 2020 structural gap does not create false lags.
- Model C is compared against a matched-window baseline because overnight visitor data only covers 2024 Q1-Q2 in the test year.
- Simple baselines are retained unless a more complex model demonstrably improves out-of-sample performance.
- Human judgement remains explicit in the planned product layer.
