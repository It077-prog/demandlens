from __future__ import annotations

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .features import TARGET


def build_ridge_pipeline(feature_names: list[str]) -> Pipeline:
    categorical = [c for c in feature_names if c == "Hotel_Category"]
    numeric = [c for c in feature_names if c not in categorical]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler()),
                    ]
                ),
                numeric,
            ),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical,
            ),
        ],
        remainder="drop",
    )

    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", Ridge(alpha=1.0)),
        ]
    )


def fit_predict_year(
    df: pd.DataFrame,
    feature_names: list[str],
    test_year: int = 2024,
) -> tuple[Pipeline, pd.DataFrame]:
    """Train strictly before test_year and predict test_year."""
    train = df[df["Year"] < test_year].dropna(subset=[TARGET]).copy()
    test = df[df["Year"] == test_year].dropna(subset=[TARGET]).copy()

    model = build_ridge_pipeline(feature_names)
    model.fit(train[feature_names], train[TARGET])

    out = test[["Year", "Quarter", "Quarter_Number", "Hotel_Category", TARGET]].copy()
    out["prediction"] = model.predict(test[feature_names])
    out = out.rename(columns={TARGET: "actual"})
    return model, out
