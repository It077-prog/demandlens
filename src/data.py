from pathlib import Path
import pandas as pd


DEFAULT_DATA_PATH = Path("data/processed/demandlens_master.csv")


def load_master(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the prepared quarterly DemandLens master dataset."""
    df = pd.read_csv(path)
    df["Year"] = pd.to_numeric(df["Year"], errors="raise").astype(int)
    df["Quarter_Number"] = pd.to_numeric(df["Quarter_Number"], errors="raise").astype(int)
    df["time_index"] = df["Year"] * 4 + df["Quarter_Number"]
    return df.sort_values(["Year", "Quarter_Number", "Hotel_Category"]).reset_index(drop=True)
