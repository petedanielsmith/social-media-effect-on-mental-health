import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from utils.data_utils import load_data
from utils.graph_utils import plot_distribution

st.set_page_config(
    layout="wide",
)

# Load the cleaned dataset
df = load_data()

# add filter bar here
#-----------------------

# Create a copy of the dataframe to apply filters on
df_filtered = df.copy()

# Apply filters here
#-----------------------

st.write("# " + ":material/bar_chart:" + " Data Visualisation")

st.caption("EDA - Exploratory Data Analysis and Visualisation of the social media and mental health dataset.")


# Create tabs for different visualisations
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([":material/table: Table", ":material/leaderboard: Distributions", ":material/bar_chart: Frequency Charts", ":material/grid_on: Correlations", ":material/monitoring: Combined Charts", ":material/monitoring: Trends Over Time"])

with tab1:
    st.info(":material/table: Table View")

with tab2:
    st.info(":material/leaderboard: Distributions of numerical features")

    dist_fields = [ "age", "daily_screen_time_min", "social_media_time_min", "sleep_hours", "physical_activity_min" ]

    # add multi select to pick fields to plot distributions for numerical features
    fields = st.multiselect("Select numerical features to plot distributions", options=dist_fields, default=dist_fields)
    
    col1, col2 = st.columns(2)

    with col1:
        # Add a chart type dropdown
        chart_type = st.selectbox("Select chart type", ["Histogram", "Histogram & KDE", "Violin Plot", "Box Plot", "Violin Plot & Box Plot"])

    with col2:
        # Add a bin size slider thats only visible if chart type is histogram or histogram & kde
        if chart_type in ["Histogram", "Histogram & KDE"]:
            bin_size = st.slider("Select bin size for histogram", min_value=1, max_value=100, value=30, step=1)
        else:
            bin_size = None
    
    with st.expander("Extra Options"):
        col1, col2, col3 = st.columns(3)

        with col1:
            on = st.toggle("Add Mean Line", value=False)
            if on:
                show_mean = True
            else:
                show_mean = False

        with col2:
            on = st.toggle("Add Median Line", value=False)
            if on:
                show_median = True
            else:
                show_median = False

        with col3:
            std_line = st.selectbox("Add Standard Deviation Line", ["None", "1 SD", "2 SD", "3 SD"])

        col1, col2, col3 = st.columns(3)

        with col1:
            on = st.toggle("Add 1st Quartile Line", value=False)
            if on:
                show_q1 = True
            else:
                show_q1 = False

        with col2:
            on = st.toggle("Add 3rd Quartile Line", value=False)
            if on:
                show_q3 = True
            else:
                show_q3 = False

        with col3:
            on = st.toggle("Add IQR Line", value=False)
            if on:
                show_iqr = True
            else:
                show_iqr = False

        col1, col2, col3 = st.columns(3)

        with col1:
            on = st.toggle("Add skewness", value=False)
            if on:
                show_skewness = True
            else:
                show_skewness = False
        with col2:
            on = st.toggle("Add kurtosis", value=False)
            if on:
                show_kurtosis = True
            else:
                show_kurtosis = False

        with col3:
            on = st.toggle("Add count", value=False)
            if on:
                show_count = True
            else:
                show_count = False

    match len(fields):
        case 0 | 1:
            fig, ax = plt.subplots(1, 1, figsize=(20, 10))
        case 2:
            fig, ax = plt.subplots(1, 2, figsize=(20, 10))
        case 3 | 4:
            fig, ax = plt.subplots(2, 2, figsize=(20, 10))
        case 5:
            fig, ax = plt.subplots(2, 3, figsize=(20, 10))

    if isinstance(ax, np.ndarray):
        ax = ax.flatten()
    else:
        ax = [ax]

    for i, field in enumerate(fields):
        plot_distribution(
                axes=ax[i],
                type=chart_type,
                df=df_filtered,
                column=field,
                bins=bin_size,
                kde=(chart_type == "Histogram & KDE"),
                mean=show_mean,
                median=show_median,
                std=std_line,
                q1=show_q1,
                q3=show_q3,
                iqr=show_iqr,
                skew=show_skewness,
                kurtosis=show_kurtosis,
                count=show_count
            )
    
    # Hide unused subplots to make the layout cleaner
    if(len(fields) == 0):
        ax[0].set_visible(False)
    else:
        for j in range(i + 1, len(ax)):
            ax[j].set_visible(False)

    # Adjust layout
    plt.tight_layout()
    st.pyplot(fig)

    if(chart_type in ["Box Plot", "Violin Plot & Box Plot"] and show_iqr == True):
        st.warning("Note: Box whiskers may not line up with the IQR lines as Seaborn automatically adjusts the whiskers to the min and max values when there are no outliers.")

        

with tab3:
    st.info(":material/bar_chart: Frequency Charts for categorical features")

with tab4:
    st.info(":material/grid_on: Correlation Matrix and Heatmaps")

with tab5:
    st.info(":material/monitoring: Combined Charts for multi-variable analysis")

with tab6:
    st.info(":material/monitoring: Trends Over Time")