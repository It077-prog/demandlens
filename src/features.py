import pandas as pd

TARGET = "Occupancy_Percent"
GROUP = "Hotel_Category"


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create exact previous-quarter and previous-year occupancy lags.

    Structural gaps (notably 2020) remain missing; no row-shift interpolation is used.
    """
    out = df.copy()
    key = out[["Year", "Quarter_Number", GROUP, TARGET]].copy()

    prev_q = key.copy()
    prev_q["Quarter_Number"] = prev_q["Quarter_Number"] + 1
    rollover = prev_q["Quarter_Number"] == 5
    prev_q.loc[rollover, "Quarter_Number"] = 1
    prev_q.loc[rollover, "Year"] = prev_q.loc[rollover, "Year"] + 1
    prev_q = prev_q.rename(columns={TARGET: "occupancy_lag_1"})
    out = out.merge(prev_q, on=["Year", "Quarter_Number", GROUP], how="left")

    prev_y = key.copy()
    prev_y["Year"] = prev_y["Year"] + 1
    prev_y = prev_y.rename(columns={TARGET: "occupancy_lag_4"})
    out = out.merge(prev_y, on=["Year", "Quarter_Number", GROUP], how="left")

    return out.sort_values(["Year", "Quarter_Number", GROUP]).reset_index(drop=True)


MODEL_A_FEATURES = [
    "Quarter_Number",
    "Hotel_Category",
    "Number_of_Hotels",
    "Available_Rooms",
    "occupancy_lag_1",
    "occupancy_lag_4",
]

AIRPORT_FEATURES = [
    "DXB_Arrivals",
    "DXB_Departures",
    "DXB_Transit",
    "DWC_Arrivals",
    "DWC_Departures",
    "DWC_Transit",
]

VISITOR_FEATURES = [
    "Total_Overnight_Visitors",
    "Visitors_Africa",
    "Visitors_Americas",
    "Visitors_Australasia",
    "Visitors_GCC",
    "Visitors_MENA",
    "Visitors_NE_Asia_and_South_East_Asia",
    "Visitors_Russia_CIS_and_Eastern_Europe",
    "Visitors_South_Asia",
    "Visitors_Western_Europe",
]
