# DemandLens

DemandLens is a Dubai hospitality demand-intelligence portfolio project.

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

## Benchmark

The initial 2024 seasonal-naive benchmark predicts each quarter using the same hotel category and quarter from the previous year.

Observed benchmark results:

- MAE: 0.92 occupancy percentage points
- RMSE: 1.12
- MAPE: 1.18%

Any proposed model must be compared against this benchmark on chronological validation.

## Modelling plan

1. Seasonal-naive baseline
2. Model A — lagged occupancy + quarter + hotel category + hotel supply
3. Model B — Model A + Dubai airport passenger signals
4. Model C — Model B + overnight visitor signals
5. Compare out-of-sample MAE / RMSE / MAPE
6. Productize the best defensible model in Streamlit

## Structure

```
data/
  processed/
src/
  data.py
  features.py
  baseline.py
  models.py
  evaluate.py
app/
  streamlit_app.py
tests/
outputs/
  metrics/
```

## Methodology

- Time-series splits only; no random train/test split.
- 2020 is kept missing rather than synthetically interpolated.
- Simple baselines are retained unless a more complex model demonstrably improves out-of-sample performance.
- Human judgement remains explicit in the planned product layer.
