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

PERSONA_DETAILS = [
    {
        "bulletpoints" : [
            "Age ≈ 25",
            "Very high daily screen time (423 min)", 
            "Surprisingly low social media minutes → suggests WhatsApp messaging dominates",
            "Low physical activity",
            "Low negative interactions", 
            "Stress high (6.6) and mood low (6.2)", 
            "Anxiety low-moderate (1.8)",
        ],
        "strapline" : "A young male who spends most of his digital time messaging rather than browsing social feeds. Low negative interaction but still stressed — possibly due to high digital load rather than conflict.",
        "image_path" : "./images/persona_0.png",
        "name" : "Cluster 0",
        "name_detailed" : CLUSTER_NAMES[0],
    },
    {
        "bulletpoints" : [
            "Age ≈ 25",
            "High screen time, high social media time", 
            "High negative interaction ratio",
            "Stress elevated (7.2)",
            "Mood lower", 
            "Anxiety slightly higher", 
            "Mostly female Facebook users",
        ],
        "strapline" : "A young woman spending long hours on Facebook, experiencing more negative interactions, and showing higher stress + anxiety.",
        "image_path" : "./images/persona_1.png",
        "name" : "Cluster 1",
        "name_detailed" : CLUSTER_NAMES[1],
    },
    {
        "bulletpoints" : [
            "High screen time but extremely high social media use (232 min)", 
            "Moderate negative interaction ratio", 
            "Stress high (7.7)",
            "Mood lower",
            "Anxiety higher (3.0)", 
        ],
        "strapline" : "Snapchat power user with high engagement and rising emotional strain.",
        "image_path" : "./images/persona_2.png",
        "name" : "Cluster 2",
        "name_detailed" : CLUSTER_NAMES[2],
    },
    {
        "bulletpoints" : [
            "Highest overall screen time (435 min)", 
            "High YouTube usage", 
            "Medium negative interaction ratio",
            "Stress very high (7.76)",
            "Mood lower", 
            "Anxiety ~3.0", 
            "Younger demographic",
        ],
        "strapline" : "Heavy YouTube binge-watcher with very high stress levels.",
        "image_path" : "./images/persona_3.png",
        "name" : "Cluster 3",
        "name_detailed" : CLUSTER_NAMES[3],
    },
    {
        "bulletpoints" : [
            "Age ≈ 51 → clearly separated", 
            "Low screen time (194 min)", 
            "Low social media time (only 66 min)",
            "Very high physical activity (40 min/day)",
            "Zero negative interactions", 
            "Stress = 5, mood = 7 (very positive), anxiety = 1", 
            "Mostly Facebook",
            "Mental state = Healthy",
        ],
        "strapline" : "Older, active adult with balanced tech use and generally strong mental health.",
        "image_path" : "./images/persona_4.png",
        "name" : "Cluster 4",
        "name_detailed" : CLUSTER_NAMES[4],
    },
    {
        "bulletpoints" : [
            "Age ≈ 45", 
            "Moderate screen & social media time", 
            "High physical activity",
            "Moderate negative interactions",
            "Stress moderately high", 
            "Mood ~6", 
            "Anxiety low",
        ],
        "strapline" : "Middle-aged TikTok user, fairly active lifestyle, some stress but not extreme.",
        "image_path" : "./images/persona_5.png",
        "name" : "Cluster 5",
        "name_detailed" : CLUSTER_NAMES[5],
    },
    {
        "bulletpoints" : [
            "Age ≈ 24", 
            "Very high screen time", 
            "Extremely high social media usage (277 min)",
            "High negative interaction ratio (0.427)",
            "Highest stress in all clusters (8.5)", 
            "Lowest mood", 
            "Highest anxiety (3.8)",
        ],
        "strapline" : "",
        "image_path" : "./images/persona_6.png",
        "name" : "Cluster 6",
        "name_detailed" : CLUSTER_NAMES[6],
    },
]