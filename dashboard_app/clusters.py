import streamlit as st

# Import utilities to load personas
from utils.persona_utils import PERSONA_DETAILS, cluster_profiles


st.set_page_config(
    layout="wide",
)

st.write("# " + ":material/diversity_3:" + " Clusters")

st.caption("Segmentation of users into distinct clusters based on their behaviours and characteristics.")


tab1, tab2, tab3 = st.tabs([":material/person: Personas",":material/2d: Scatter Plot", " :material/menu_book: Methodology"])

with tab1:
    st.info('Each of the clusters were assigned to a persona based on their key characteristics and the centroid values of the clusters.', icon=":material/person:")

    # Create three columns for displaying personas
    cols = st.columns(3)

    # Display each persona in a card-like format
    for i, persona in enumerate(PERSONA_DETAILS):
        with cols[i % 3]:
            st.write(f"##### {persona['name']}")
            st.image(persona['image_path'], width="stretch")
            st.write(f"###### {persona['name_detailed']}")
            # Add custom HTML for the bulletpoints to align the cards in the columns with a fixed height
            st.html(f"""
                <div style="
                    display: flex;
                    flex-direction: column;
                    height: 260px;  
                    justify-content: flex-start;
                    overflow: hidden;
                ">
                    <div style="margin-top: 6px; font-weight: 600;">Key Characteristics:</div>

                    <ul style="padding-left: 20px; margin: 2px 0 0 0;">
                        {''.join(f"<li>{bp}</li>" for bp in persona['bulletpoints'])}
                    </ul>
                </div>
            """)

            # Add popover for raw data
            popover = st.popover(f"View Cluster {i}", width="stretch", icon=":material/database_search:")

            # Get raw data for the cluster
            row = cluster_profiles.loc[i].to_frame("Value")
            row["Value"] = row["Value"].astype(str) 

            # Display raw data in the popover
            popover.write(f"### Cluster {i} Raw Data")
            popover.dataframe(row, height=455)

with tab2:
    st.info('Using PCA to reduce the dimensions and visualise clusters as a 2D scatter plot', icon=":material/2d:")
    st.image("./images/pca_clusters_k7_scatter_plot.png", width="stretch")

with tab3:
    st.info('Methodology behind the clustering process I used', icon=":material/menu_book:")

    st.write("## Clustering Methodology")

    st.markdown("""
    This page outlines the full methodology used to cluster users based on their behavioural, lifestyle, and mental-health indicators.  
    The goal was to uncover meaningful user personas that reflect distinct patterns in screen time, emotional wellbeing, and digital habits.
    """)

    st.markdown("---")

    st.write("### Pipeline Structure")
    st.code("""
    pipeline = Pipeline(steps=[
        ("onehot", OneHotEncoder(variables=categorical_features, drop_last=True)),
        ("scaler", StandardScaler()),
        ("kmeans", KMeans(n_clusters=7, random_state=42, n_init="auto"))
    ])
    """, language="python")

    st.markdown("""
    The clustering pipeline performed:

    - **Categorical encoding** using OneHotEncoder  
    - **Standardisation** using StandardScaler  
    - **K-Means clustering**, where the number of clusters *k* was selected through multiple validation methods  
    """)

    st.markdown("---")


    st.write("### Selecting the Number of Clusters")

    st.markdown("""
    To find the best value of **k**, I evaluated:

    #### **1. Silhouette Scores**
    Tested k = 2 → 10.

    - Highest average silhouette score was **k = 8** (≈ 0.342)
    - **k = 7** and **k = 5** also performed well, showing clean structure
    - Very high silhouette scores here reflect the synthetic nature of the dataset

    #### **2. Elbow Method**
    The elbow plot showed:

    - Small elbows at **k = 5** and **k = 7**
    - A deeper elbow at **k = 8**
    - k = 9 increased slightly but without meaningful structural improvement

    This suggested a possible range of **5–8 clusters**.

    #### **3. PCA Visualisation**
    To visually assess cluster separation, I plotted 2D PCA projections for **k = 5, 7, and 8**.

    """)

    st.markdown("---")

    st.write("### PCA Cluster Comparisons")

    st.markdown("""
    #### **k = 5 — Broad, but mixed clusters**
    - Clear high-level groupings  
    - Some clusters contain more than one behavioural pattern  
    - PCA shows overlapping internal sub-groups → under-segmentation  

    #### **k = 7 — Best balance**
    - Strong separation with no noisy or tiny clusters  
    - PCA shows well-defined, stable cluster shapes  
    - Subgroups become meaningful and interpretable  
    - Silhouette score (≈ 0.311) remains high and consistent  
    - Clear behavioural “persona” profiles emerge  

    #### **k = 8 — Over-fragmentation**
    - Several clusters split unnecessarily  
    - Some clusters become nearly identical  
    - One large, meaningful group is chopped into two  
    - Begins to capture noise instead of structure  

    **Final Choice: `k = 7`**  
    This value captures distinct behavioural groups without splitting meaningful patterns.  
    """)

    st.markdown("---")

    st.write("### Persona Creation")
    st.markdown("""
    After selecting **k = 7**, I extracted the cluster centroids and analysed the average characteristics of each group.  
    These were then transformed into human-readable personas that describe:

    - Lifestyle patterns  
    - Digital behaviour  
    - Emotional wellbeing  
    - Social interaction quality  

    These personas help translate raw cluster statistics into understandable groups.
    """)

    st.markdown("---")

    st.write("### Conclusion")

    st.markdown("""
    The clustering analysis revealed highly distinct user groups:

    - Younger users with **high screen time**, **frequent negative interactions**, and **heavy social media use** tended to fall into stressed or anxious clusters.
    - A single group of older users with **low screen time**, **high physical activity**, and **no negative interactions** emerged as the only cluster classified as *mentally healthy*.
    - The patterns reinforce the broader analytical finding:  
    **More digital engagement—especially negative interactions—is linked to poorer mental wellbeing**, while **balanced use and active lifestyles** correlate with better outcomes.

    Overall, the clustering step provided a clear persona-level perspective on how digital habits map to mental health within this synthetic dataset.
    """)

