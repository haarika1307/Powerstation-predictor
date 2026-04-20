import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.recommendation import recommend_station

st.title("⚡ AI EV Charging Optimization System")

# Load data
df = load_data("data/charging_ev_and_grid_optimization_dataset.csv")
df = clean_data(df)
df = create_features(df)

# User inputs
mode = st.selectbox("Select Mode", ["fast", "cheap", "eco"])

if st.button("Find Best Station"):
    result = recommend_station(df, user_input={}, mode=mode)

    st.subheader("🚗 Recommended Station")
    st.write(result)