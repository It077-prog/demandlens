import pandas as pd

from .features import TARGET


def seasonal_naive_predictions(df: pd.DataFrame) -> pd.DataFrame:
    """Predict each quarter from the same category and quarter one year earlier."""
    source = df[["Year", "Quarter_Number", "Hotel_Category", TARGET]].copy()
    source["Year"] = source["Year"] + 1
    source = source.rename(columns={TARGET: "prediction"})

    actual = df[["Year", "Quarter_Number", "Quarter", "Hotel_Category", TARGET]].copy()
    result = actual.merge(
        source,
        on=["Year", "Quarter_Number", "Hotel_Category"],
        how="left",
    )
    return result.rename(columns={TARGET: "actual"})
