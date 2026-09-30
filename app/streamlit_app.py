import streamlit as st

st.set_page_config(page_title="StaySignal", page_icon="📈", layout="wide")

st.title("StaySignal")
st.subheader("Dubai Hospitality Demand Intelligence")

st.info(
    "V0.1 engineering shell. The product UI will use the validated model only after "
    "chronological benchmark comparisons are complete."
)

st.markdown(
    """
### Product question

**What is likely to happen to Dubai hotel occupancy next, why, how uncertain is the forecast,
and should a human planner accept or override the recommendation?**

### Current modelling sequence

1. Seasonal-naive benchmark
2. Model A — hotel history and supply
3. Model B — add Dubai airport passenger signals
4. Model C — add overnight visitor signals
"""
)
