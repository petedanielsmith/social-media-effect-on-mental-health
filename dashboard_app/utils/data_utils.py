import pandas as pd
import streamlit as st

@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_parquet("./data/mental_health_social_media_dataset_cleaned.parquet")
    return df

