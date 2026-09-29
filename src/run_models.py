import json
from pathlib import Path

from .baseline import seasonal_naive_predictions
from .data import load_master
from .evaluate import evaluate_frame
from .features import AIRPORT_FEATURES, MODEL_A_FEATURES, VISITOR_FEATURES, add_lag_features
from .models import fit_predict_year

OUTPUT = Path("outputs/metrics/model_metrics.json")


def main() -> None:
    df = add_lag_features(load_master())
    results = {}

    baseline = seasonal_naive_predictions(df)
    results["seasonal_naive"] = evaluate_frame(baseline[baseline["Year"] == 2024])

    _, model_a = fit_predict_year(df, MODEL_A_FEATURES, test_year=2024)
    results["model_a"] = evaluate_frame(model_a)

    _, model_b = fit_predict_year(df, MODEL_A_FEATURES + AIRPORT_FEATURES, test_year=2024)
    results["model_b"] = evaluate_frame(model_b)

    visitor_df = df.dropna(subset=["Total_Overnight_Visitors"]).copy()
    if 2024 in set(visitor_df["Year"]):
        _, model_c = fit_predict_year(
            visitor_df,
            MODEL_A_FEATURES + AIRPORT_FEATURES + VISITOR_FEATURES,
            test_year=2024,
        )
        results["model_c"] = evaluate_frame(model_c)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
