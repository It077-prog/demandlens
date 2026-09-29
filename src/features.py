import pandas as pd


TARGET = "Occupancy_Percent"
GROUP = "Hotel_Category"


def add_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create hotel-category occupancy lags without filling structural gaps."""
    out = df.sort_values([GROUP, "Year", "Quarter_Number"]).copy()
    grouped = out.groupby(GROUP, sort=False)[TARGET]
    out["occupancy_lag_1"] = grouped.shift(1)
    out["occupancy_lag_4"] = grouped.shift(4)
    return out


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
