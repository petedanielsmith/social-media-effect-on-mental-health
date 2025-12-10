import streamlit as st

st.set_page_config(
    layout="wide",
)

# Add banner image
st.image("./images/socail-media-mental-health-banner.jpg", width="stretch")

# Add title centered
st.html(
    """
    <h1 style="text-align:center; margin-top: -20px;">
        Social Media & Mental Health Indicators Dashboard
    </h1>
    """
)

# horizontal line
st.write("---")


# Dataset Overview Section
st.markdown(
    """
    ### Dataset used  
    This dashboard is built using the **Social Media Mental Health Indicators Dataset**  
    sourced from Kaggle: https://www.kaggle.com/datasets/sonalshinde123/social-media-mental-health-indicators-dataset  

    The dataset captures the relationship between:
    - **Daily social media usage**
    - **Screen-time behaviour**
    - **Lifestyle factors** (sleep, activity)
    - **Interaction quality** (positive vs. negative)
    - **Mental well-being indicators** (stress, anxiety, mood)

    It contains **5,000 individual-level records**, each describing how digital habits
    and daily behavior may influence mental health outcomes.
    """
)

# horizontal line
st.write("---")


# Dataset Overview Section
st.markdown("## Original Dataset Overview")

st.markdown(
    """
    The original dataset included the following fields:
    """
)

# Define original columns and data types
original_cols = {
    "person_name": "object (891 unique)",
    "age": "int64 (57 unique)",
    "date": "object (686 unique)",
    "gender": "object (3 unique)",
    "platform": "object (7 unique)",
    "daily_screen_time_min": "int64 (342 unique)",
    "social_media_time_min": "int64 (304 unique)",
    "negative_interactions_count": "int64 (3 unique)",
    "positive_interactions_count": "int64 (5 unique)",
    "sleep_hours": "float64 (19 unique)",
    "physical_activity_min": "int64 (36 unique)",
    "anxiety_level": "int64 (4 unique)",
    "stress_level": "int64 (5 unique)",
    "mood_level": "int64 (4 unique)",
    "mental_state": "object (3 unique)"
}

# Display original columns and data types
st.json(original_cols)

# horizontal line
st.write("---")

# Data Cleaning & Feature Engineering Section
st.markdown("## Data Cleaning & Feature Engineering")

st.markdown(
    """
    After cleaning and feature engineering, several improvements were applied:
    - Converted `date` to proper date datatype
    - Extracted **year**, **month**, **month name**, **week number**, **day of week**
    - Created **age group** category
    - Converted categorical fields into optimised categorical dtypes
    - Engineered new useful fields including:
        - **interaction_total**
        - **interaction_negative_ratio**
    """
)

# Define cleaned columns and data types
cleaned_cols = {
    "date": "datetime64[ns]",
    "year": "int32",
    "month": "int32",
    "month_name": "category",
    "week_number": "UInt32",
    "day_of_week": "category",
    "age": "int64",
    "age_group": "category",
    "gender": "category",
    "platform": "category",
    "daily_screen_time_min": "int64",
    "social_media_time_min": "int64",
    "sleep_hours": "float64",
    "physical_activity_min": "int64",
    "negative_interactions_count": "int64",
    "positive_interactions_count": "int64",
    "interaction_total": "int64",
    "interaction_negative_ratio": "float64",
    "anxiety_level": "int64",
    "stress_level": "int64",
    "mood_level": "int64",
    "mental_state": "category"
}

# Display cleaned columns and data types
st.json(cleaned_cols)

# horizontal line
st.write("---")

# Dashboard Sections Overview
st.markdown("## Dashboard Sections")

st.markdown(
    """
    This application contains **six main sections**:

    ### 1. **Introduction**
    This page. Provides dataset context and dashboard overview.

    ### 2. **Data Visualisation**
    A full exploratory analysis toolkit including:
    - Table views  
    - Distributions  
    - Frequency plots  
    - Correlation heatmaps  
    - Category vs Numeric  
    - Numeric vs Numeric  
    - Category vs Category  
    - Trends over time  
    With a fully interactive sidebar filter system.

    ### 3. **Hypothesis Testing**
    A presentation of statistical tests performed on the dataset  
    (ANOVA, Chi-Square, correlation tests).

    ### 4. **Clusters**
    Clustering analysis results including:
    - User persona groups  
    - Behavioral segment descriptions  
    - Cluster visualisation  

    ### 5. **Models Overview**
    Overview of machine learning models built (preprocessing, algorithms, parameters).

    ### 6. **Model Predictions**
    An interactive form where you enter user details and receive ML-based predictions  
    (e.g., mood, stress, mental state).
    """
)

# horizontal line
st.write("---")


# Footer
st.html(
    """
    <div style="text-align:center; color:gray; margin-top:20px;">
        Built with Streamlit • Data Source: Kaggle • Author: Pete Smith
    </div>
    """
)