import pandas as pd

from src.baseline import seasonal_naive_predictions
from src.evaluate import regression_metrics


def test_seasonal_naive_uses_same_quarter_previous_year():
    frame = pd.DataFrame(
        [
            {"Year": 2023, "Quarter_Number": 1, "Quarter": "Q1", "Hotel_Category": "5-Star", "Occupancy_Percent": 80.0},
            {"Year": 2024, "Quarter_Number": 1, "Quarter": "Q1", "Hotel_Category": "5-Star", "Occupancy_Percent": 82.0},
        ]
    )
    pred = seasonal_naive_predictions(frame)
    value = pred.loc[pred["Year"].eq(2024), "prediction"].iloc[0]
    assert value == 80.0


def test_metrics_are_zero_for_perfect_predictions():
    metrics = regression_metrics([80, 81], [80, 81])
    assert metrics["mae"] == 0
    assert metrics["rmse"] == 0
    assert metrics["mape"] == 0
