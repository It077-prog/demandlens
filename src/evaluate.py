from __future__ import annotations

import math
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error


def regression_metrics(actual, predicted) -> dict[str, float]:
    y_true = np.asarray(actual, dtype=float)
    y_pred = np.asarray(predicted, dtype=float)

    mae = mean_absolute_error(y_true, y_pred)
    rmse = math.sqrt(mean_squared_error(y_true, y_pred))

    nonzero = y_true != 0
    mape = float(np.mean(np.abs((y_true[nonzero] - y_pred[nonzero]) / y_true[nonzero])) * 100)

    return {"mae": float(mae), "rmse": float(rmse), "mape": mape}


def evaluate_frame(frame: pd.DataFrame, actual_col="actual", pred_col="prediction") -> dict[str, float]:
    clean = frame[[actual_col, pred_col]].dropna()
    metrics = regression_metrics(clean[actual_col], clean[pred_col])
    metrics["n"] = int(len(clean))
    return metrics
