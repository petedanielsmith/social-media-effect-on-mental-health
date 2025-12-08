import streamlit as st

pages = [
    st.Page("introduction.py", title="Introduction", icon=":material/info:"),
    st.Page("data_visualisation.py", title="Data Visualisation", icon=":material/bar_chart:"),
    st.Page("hypothesis_statistical_testing.py", title="Hypothesis Testing", icon=":material/experiment:"),
    st.Page("clusters.py", title="Clusters", icon=":material/diversity_3:"),
    st.Page("models_overview.py", title="Models Overview", icon=":material/schema:"),
    st.Page("model_predictions.py", title="Model Predictions", icon=":material/psychology:"), 
]

pg = st.navigation(pages)
pg.run()