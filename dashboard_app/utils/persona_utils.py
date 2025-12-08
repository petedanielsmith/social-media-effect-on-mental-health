import joblib
import streamlit as st
import pandas as pd

def clean_persona_values(persona: dict) -> dict:
    '''
    This function cleans and converts persona values to appropriate types.
    
    Parameters:
    - persona: A dictionary containing persona values.
    
    Returns:
    - A dictionary containing cleaned and converted persona values.
    '''
    cleaned = {}
    for key, value in persona.items():

        # Whole-number sliders
        if key in ["stress_level", "mood_level", "anxiety_level"]:
            cleaned[key] = int(round(value))

        # Age or minutes values
        elif key in ["age", "daily_screen_time_min", "social_media_time_min", "physical_activity_min"]:
            cleaned[key] = int(round(value))

        # Sleep hours: leave as float with 1 decimal place max
        elif key == "sleep_hours":
            cleaned[key] = round(float(value), 1)

        # Ratio values
        elif key == "interaction_negative_ratio":
            cleaned[key] = float(value)

        # Categorical values
        else:
            cleaned[key] = value

    return cleaned


@st.cache_data
def load_cluster_profiles():
    '''
    This function loads the cluster profiles data from a parquet file and is cached to improve performance.
    
    Returns:
    - A pandas DataFrame containing the cluster profiles.
    '''
    return pd.read_parquet("./data/cluster_profiles.parquet")


CLUSTER_NAMES = {
    0: "Young WhatsApp Overloaded Male",
    1: "Female Facebook Worrier",
    2: "Snapchat-Heavy Stressed Female",
    3: "Female YouTube High-Use Stressed Group",
    4: "Healthy Older Facebook User",
    5: "Older TikTok User With Moderate Strain",
    6: "TikTok-Addicted Young Stressed Male"
}

# Load cluster profiles data
cluster_profiles = load_cluster_profiles()

# Constant dictionary mapping cluster names to their profiles
PERSONAS = {
    f"Cluster {row.name} - {CLUSTER_NAMES.get(row.name, 'Unnamed')}": row.to_dict()
    for _, row in cluster_profiles.iterrows()
}