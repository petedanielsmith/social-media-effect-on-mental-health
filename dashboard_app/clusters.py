import streamlit as st

# Import utilities to load personas
from utils.persona_utils import PERSONA_DETAILS, cluster_profiles


st.set_page_config(
    layout="wide",
)

st.write("# " + ":material/diversity_3:" + " Clusters")

st.caption("Segmentation of users into distinct clusters based on their behaviors and characteristics.")


tab1, tab2, tab3 = st.tabs([":material/person: Personas",":material/2d: Scatter Plot", " :material/menu_book: Methodology"])

with tab1:
    st.info('Each of the clusters were assigned to a persona based on their key characteristics', icon=":material/person:")

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

    st.markdown(
        """
        Methodology for clustering will go here.
    """
    )
