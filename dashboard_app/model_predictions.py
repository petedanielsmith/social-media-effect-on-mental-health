import streamlit as st
import pandas as pd
import joblib
from math import floor

# Import utilities to load models, personas and section header
from utils.model_utils import  MODELS
from utils.persona_utils import clean_persona_values, PERSONAS
from utils.ui_components import section_header

st.set_page_config(
    # Set a wide layout to give more page space
    layout="wide",
)

# Add page title and icon
st.write("# " + ":material/psychology:" + " Model Predictions")

# Add page description under title
st.caption('''
    Use this page to predict mental health related targets based on user input features.
''')

with st.expander("How to use this page"):
    st.write('''
        Here is how to use the Model Predictions page:
        1. Select the model you want to use for prediction from the dropdown menu.
        2. (Optional) Choose a persona from the dropdown to autofill input values based on predefined profiles.
        3. Adjust the input features as needed using the provided sliders and dropdowns.
        4. Click the "Predict" button to see the model's prediction based on your inputs.
        5. The prediction result will be displayed below the button.
    ''')

section_header(1, "Select Model:")

dropdownCol1, dropdownCol2 = st.columns(2)
with dropdownCol1:
    # Dropdown to select which model to use for prediction
    selected_model_name = st.selectbox("Choose what you want to predict", list(MODELS.keys()))
    selected_model = MODELS[selected_model_name]
    target = selected_model["target"]

with dropdownCol2:
    # Dropdown to select persona to autofill values
    persona_name = st.selectbox(
    "Choose a persona (optional to autofill values)",
    ["None"] + list(PERSONAS.keys())
    )

# Apply persona values
if persona_name != "None":
    persona_raw = PERSONAS[persona_name]
    persona = clean_persona_values(persona_raw)

    # Set standard features
    for key, value in persona.items():
        if key != "interaction_negative_ratio":
            st.session_state[key] = value

    # Handle interaction ratio specially
    ratio = persona["interaction_negative_ratio"]
    total = 10
    neg = int(round(ratio * total))
    pos = total - neg

    st.session_state["neg_interactions"] = neg
    st.session_state["pos_interactions"] = pos

section_header(2, "Enter Prediction Parameters:")

# Create three columns for input features
col1, col2, col3 = st.columns(3)

input_data = {}

# 1st Column
with col1:
    input_data["gender"] = st.selectbox("Gender", ["Male", "Female", "Other"], disabled=(target == "gender"), key="gender")
    input_data["age"] = st.slider("Age", 13, 80, 30, key="age")
    input_data["physical_activity_min"] = st.slider("Daily Physical Activity (min)", 0, 180, 30, key="physical_activity_min")
    input_data["sleep_hours"] = st.slider("Sleep Hours", 4.0, 10.0, 7.0, disabled=(target == "sleep_hours"), key="sleep_hours")

# 2nd Column
with col2:
    input_data["mental_state"] = st.selectbox("Mental State", ["Healthy", "Stressed", "At Risk"], disabled=(target == "mental_state"), key="mental_state")
    input_data["mood_level"] = st.slider("Mood Level", 1, 10, 5, disabled=(target == "mood_level"), key="mood_level")
    input_data["stress_level"] = st.slider("Stress Level", 1, 10, 5, disabled=(target == "stress_level"), key="stress_level")
    input_data["anxiety_level"] = st.slider("Anxiety Level", 1, 10, 5, disabled=(target == "anxiety_level"), key="anxiety_level")

# 3rd Column
with col3:
    input_data["platform"] = st.selectbox("Platform", ["Instagram", "Snapchat", "Facebook", "WhatsApp", "TikTok", "YouTube"], key="platform")
    input_data["daily_screen_time_min"] = st.slider("Daily Screen Time (min)", 0, 600, 300, key="daily_screen_time_min")
    input_data["social_media_time_min"] = st.slider("Social Media Time (min)", 0, 400, 150, key="social_media_time_min")

    intCol1, intCol2 = st.columns(2)
    with intCol1:
        # Positive Interactions input
        pos = st.number_input("Positive Interactions", 0, 100, 10, key="pos_interactions")

    with intCol2:
        # Negative Interactions input
        neg = st.number_input("Negative Interactions", 0, 100, 2, key="neg_interactions")
 
    # Calculate and store the interaction negative ratio
    input_data["interaction_negative_ratio"] = neg / max(pos + neg, 1)

# Convert to dataframe (required for sklearn pipelines)
df_input = pd.DataFrame([input_data])

section_header(3, "Click to Predict:")

# Predict Button
if st.button("Predict"):
    # Get the model from the selected option
    model = selected_model["model"]

    # Drop the target column from input if present
    df_input = df_input.drop(columns=[target])

    # Make prediction
    prediction = model.predict(df_input)[0]

    # Display prediction with appropriate formatting
    match selected_model_name:
        case "Mental State":
            if prediction == "Healthy":
                st.success(f"### Predicted Mental State: **{prediction}**")
            elif prediction == "Stressed":
                st.warning(f"### Predicted Mental State: **{prediction}**")
            else:
                st.error(f"### Predicted Mental State: **{prediction}**")
        case "Sleep Hours":
            if prediction >= 7:
                st.success(f"### Predicted Sleep Hours: **{round(prediction, 1)} hours** (Healthy)")
            elif prediction >= 6:
                st.warning(f"### Predicted Sleep Hours: **{round(prediction, 1)} hours** (Moderate)")
            else:
                st.error(f"### Predicted Sleep Hours: **{round(prediction, 1)} hours** (Low)")
        case "Stress Level":
            if prediction <= 5:
                st.success(f"### Predicted Stress Level: **{round(prediction, 0)}** (Low)")
            elif prediction <= 8:
                st.warning(f"### Predicted Stress Level: **{round(prediction, 0)}** (Moderate)")
            else:
                st.error(f"### Predicted Stress Level: **{round(prediction, 0)}** (High)")
        case "Anxiety Level":
            if prediction <= 1:
                st.success(f"### Predicted Anxiety Level: **{round(prediction, 0)}** (Low)")
            elif prediction <= 3:
                st.warning(f"### Predicted Anxiety Level: **{round(prediction, 0)}** (Moderate)")
            else:
                st.error(f"### Predicted Anxiety Level: **{round(prediction, 0)}** (High)")
        case "Mood Level":
            if prediction >= 7:
                st.success(f"### Predicted Mood Level: **{round(prediction, 0)}** (Good)")
            elif prediction >= 5:
                st.warning(f"### Predicted Mood Level: **{round(prediction, 0)}** (Average)")
            else:
                st.error(f"### Predicted Mood Level: **{round(prediction, 0)}** (Poor)")
        case _:
            print("Unknown model selected")

    # Show more detailed raw prediction for regression models
    if selected_model_name != "Mental State":
        st.text(f"More detailed raw prediction: {prediction}")