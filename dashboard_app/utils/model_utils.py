import joblib
import streamlit as st

@st.cache_resource
def load_model(path):
    '''
    This function uses joblib to load the model and is cached to improve performance.
    
    Parameters:
    - path (str): The file path to the saved model.
    
    Returns:
    - The loaded model object.
    '''
    return joblib.load(path)


# Constant dictionary mapping model names to their loaded models and target variables
MODELS = {
    "Mental State": {
        "model": load_model("./models/predicting_mental_state_random_forest_model.pkl"),
        "target": "mental_state",
    },
    "Sleep Hours": {
        "model": load_model("./models/predicting_sleep_linear_regression_model.pkl"),
        "target": "sleep_hours",
    },
    "Stress Level": {
        "model": load_model("./models/predicting_stress_level_linear_regression_model.pkl"),
        "target": "stress_level",
    },
    "Anxiety Level": {
        "model": load_model("./models/predicting_anxiety_level_linear_regression_model.pkl"),
        "target": "anxiety_level",
    },
    "Mood Level": {
        "model": load_model("./models/predicting_mood_level_linear_regression_model.pkl"),
        "target": "mood_level",
    },
}