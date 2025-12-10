import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from datetime import date
from utils.data_utils import load_data
from utils.graph_utils import plot_distribution, plot_frequency, plot_stacked_category, plot_group_by_bar, plot_trend_over_time

st.set_page_config(
    layout="wide",
)
 
if "page" not in st.session_state:
    # Initialise the page number in session state to 1
    st.session_state.page = 1

def reset_page():
    """Reset the page number to 1 when called."""
    st.session_state.page = 1

def next_page(total_pages):
    """Increment the page number by 1 when called."""
    if st.session_state.page < total_pages:
        st.session_state.page += 1

def prev_page():
    """Decrement the page number by 1 when called."""
    if st.session_state.page > 1:
        st.session_state.page -= 1

# Load the cleaned dataset
df = load_data()

# Add sidebar filters
with st.sidebar:
    st.header(":material/filter_alt: Filters")

    # Get min and max dates for date filter
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    # Date range filter
    min_date = df["date"].min()
    max_date = df["date"].max()

    # Date range filter
    date_range = st.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        format="DD/MM/YYYY",
        on_change=reset_page
    )

    # Initialise start_date and end_date
    start_date = None
    end_date = None

    if isinstance(date_range, tuple) and len(date_range) == 2:
        # Set start_date and end_date based on date_range
        start_date, end_date = date_range
    elif isinstance(date_range, date):
        # If date_range is a single date, set start_date and leave end_date as None
        start_date = date_range
        end_date = None

    # gender multi select filter
    gender = st.multiselect("Select Genders", options=["Male", "Female", "Other"],  on_change=reset_page)

    # age group multi select filter
    age_group = st.multiselect("Select Age Groups", options=['<18', '18-24', '25-34', '35-44', '45-54', '55+'], on_change=reset_page)

    # platform multi select filter
    platform = st.multiselect("Select Platforms", options=['Facebook', 'Instagram', 'Snapchat', 'TikTok', 'Twitter', 'WhatsApp', 'YouTube'], on_change=reset_page)

    # mental state multi select filter
    mental_state = st.multiselect("Select Mental States", options=['Healthy', 'Stressed', 'At Risk'], on_change=reset_page)
    

# Create a copy of the dataframe to apply filters on
df_filtered = df.copy()

# Apply date range filter
if start_date and end_date:
    df_filtered = df_filtered[
        (df_filtered["date"] >= pd.to_datetime(start_date)) &
        (df_filtered["date"] <= pd.to_datetime(end_date))
    ]

# Apply gender filter
if len(gender) > 0:
    df_filtered = df_filtered[df_filtered["gender"].isin(gender)]

# Apply age group filter
if len(age_group) > 0:
    df_filtered = df_filtered[df_filtered["age_group"].isin(age_group)]

# Apply platform filter
if len(platform) > 0:
    df_filtered = df_filtered[df_filtered["platform"].isin(platform)]

# Apply mental state filter
if len(mental_state) > 0:
    df_filtered = df_filtered[df_filtered["mental_state"].isin(mental_state)]

# Display the count of filtered records in the sidebar
st.sidebar.markdown(f"Filtered Records: **{len(df_filtered)}** / {len(df)}")

# Main title
st.write("# " + ":material/bar_chart:" + " Data Visualisation")

# Subtitle
st.caption("EDA - Exploratory Data Analysis and Visualisation of the social media and mental health dataset.")


# Create tabs for different visualisations
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
            [":material/table: Table", 
             ":material/leaderboard: Distributions", 
             ":material/bar_chart: Frequency Charts", 
             ":material/grid_on: Correlations", 
             ":material/search_insights: Category vs Numeric", 
             ":material/looks_one: Numeric vs Numeric", 
             ":material/category: Category vs Category", 
             ":material/monitoring: Trends Over Time"])

with tab1:
    st.info(":material/table: Table View of the raw data")

    # Define full list of fields to be displayed in the table
    all_fields = ["date", "year", "month", "month_name", "week_number", "day_of_week", 	
                  "age", "age_group", "gender",
                  "platform", "daily_screen_time_min", "social_media_time_min", "sleep_hours", "physical_activity_min", 	
                  "negative_interactions_count", "positive_interactions_count", "interaction_total", "interaction_negative_ratio", 	
                  "anxiety_level", "stress_level", "mood_level", "mental_state"]
    
    # add multi select to pick fields to display
    fields = st.multiselect("Select columns to display in table", options=all_fields, default=all_fields)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Add a page size slider
        page_size = st.slider("Select number of rows per page", min_value=5, max_value=100, value=20, step=5, on_change=reset_page)

    with col2:
        # Sort by column dropdown
        sort_by = st.selectbox("Sort by column", options=["None"] + fields, index=0, on_change=reset_page)

    with col3:
        # sort order dropdown
        sort_order = st.selectbox("Sort order", options=["Ascending", "Descending"], index=0, on_change=reset_page)

    # Sort the entire dataset first
    if sort_by != "None":
        # Sort by selected column
        sorted_df = df_filtered[fields].sort_values(
            by=sort_by,
            ascending=(sort_order == "Ascending")
        )
    else:
        # Sort by index instead
        sorted_df = df_filtered[fields].sort_index(
            ascending=(sort_order == "Ascending")
        )

    # Pagination setup
    total_rows = len(sorted_df)
    total_pages = max(1, (total_rows + page_size - 1) // page_size)
    
    # Clamp page to valid range
    if st.session_state.page > total_pages:
        st.session_state.page = total_pages
    if st.session_state.page < 1:
        st.session_state.page = 1

    page = st.session_state.page

    start = (page - 1) * page_size
    end = start + page_size
    page_df = sorted_df.iloc[start:end].copy()

    if "date" in page_df.columns:
        page_df["date"] = page_df["date"].dt.strftime("%d/%m/%Y")

    # Display
    st.dataframe(page_df, width="stretch", height=600)

    info_col, buttons_col = st.columns(2)

    with info_col:
        # Display page info
        st.caption(f"Showing rows {start + 1} to {min(end, total_rows)} of {total_rows}. (Page {page}/{total_pages})")

    with buttons_col:
        # Add previous and next page buttons
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                "Previous Page",
                disabled=(page <= 1),
                on_click=prev_page,
                width="stretch"
            )
        with col2:
            st.button(
                "Next Page",
                disabled=(page >= total_pages),
                on_click=lambda: next_page(total_pages),
                width="stretch"
            )
        

with tab2:
    st.info(":material/leaderboard: Distributions of numerical features")

    # Define numerical fields for distribution plots
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
    
    # Extra options expander
    with st.expander("Extra Options"):
        
        col1, col2, col3 = st.columns(3)

        with col1:
            # Add skewness sub title toggle
            on = st.toggle("Add skewness", value=False)
            if on:
                show_skewness = True
            else:
                show_skewness = False
        with col2:
            # Add kurtosis sub title toggle
            on = st.toggle("Add kurtosis", value=False)
            if on:
                show_kurtosis = True
            else:
                show_kurtosis = False

        with col3:
            # Add count toggle
            on = st.toggle("Add count", value=False)
            if on:
                show_count = True
            else:
                show_count = False

        col1, col2, col3 = st.columns(3)

        with col1:
            # Add standard deviation line dropdown
            on = st.toggle("Add 1st Quartile Line", value=False)
            if on:
                show_q1 = True
            else:
                show_q1 = False

        with col2:
            # Add show 3rd quartile line toggle
            on = st.toggle("Add 3rd Quartile Line", value=False)
            if on:
                show_q3 = True
            else:
                show_q3 = False

        with col3:
            # Add IQR line toggle
            on = st.toggle("Add IQR Line", value=False)
            if on:
                show_iqr = True
            else:
                show_iqr = False

        
        
        col1, col2, col3 = st.columns(3)

        with col1:
            # Add mean line toggle
            on = st.toggle("Add Mean Line", value=False)
            if on:
                show_mean = True
            else:
                show_mean = False

        with col2:
            # Add median line toggle
            on = st.toggle("Add Median Line", value=False)
            if on:
                show_median = True
            else:
                show_median = False

        with col3:
            # Add standard deviation line dropdown
            std_line = st.selectbox("Add Standard Deviation Line", ["None", "1 SD", "2 SD", "3 SD"])

    # Create subplots based on number of fields selected to change the grid layout dynamically
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
        # Flatten the 2D array of axes to 1D for easier indexing
        ax = ax.flatten()
    else:
        # is only one plot, convert to list so for loop works
        ax = [ax]

    # for each field, plot the distribution
    for i, field in enumerate(fields):
        # call the plot distribution function from graph_utils to draw that fields distribution
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

    # Warning for IQR lines with box plots
    if(chart_type in ["Box Plot", "Violin Plot & Box Plot"] and show_iqr == True):
        st.warning("Note: Box whiskers may not line up with the IQR lines as Seaborn automatically adjusts the whiskers to the min and max values when there are no outliers.")

        

with tab3:
    st.info(":material/bar_chart: Frequency Charts for categorical features")

    # Define fields for frequency plots
    freq_fields = [ 'age_group', 'platform', 'gender', 'mental_state', 'anxiety_level', 
                    'stress_level', 'mood_level', 'month_name', 'day_of_week', 'week_number', 
                    'negative_interactions_count', 'positive_interactions_count', 'interaction_total', 'interaction_negative_ratio' ]

    # add multi select to pick fields to plot frequencies for features
    fields = st.multiselect("Select features to plot frequencies", 
                            options=freq_fields, 
                            default=[f for f in freq_fields if f not in ["interaction_negative_ratio", "week_number"]])
    
    
    # Add a toggle for including percentages
    include_percentages = st.toggle("Include percentages on bars", value=False)

    # Create subplots based on number of fields selected to change the grid layout dynamically
    match len(fields):
        case 0 | 1:
            fig, ax = plt.subplots(1, 1, figsize=(20, 10))
        case 2:
            fig, ax = plt.subplots(1, 2, figsize=(20, 10))
        case 3 | 4:
            fig, ax = plt.subplots(2, 2, figsize=(20, 12))
        case 5 | 6:
            fig, ax = plt.subplots(3, 2, figsize=(20, 15))
        case 7 | 8:
            fig, ax = plt.subplots(4, 2, figsize=(20, 18))
        case 9 | 10:
            fig, ax = plt.subplots(5, 2, figsize=(20, 20))
        case 11 | 12:
            fig, ax = plt.subplots(6, 2, figsize=(20, 25))
        case 13 | 14:
            fig, ax = plt.subplots(7, 2, figsize=(20, 30))
        

    if isinstance(ax, np.ndarray):
        # Flatten the 2D array of axes to 1D for easier indexing
        ax = ax.flatten()
    else:
        # is only one plot, convert to list so for loop works
        ax = [ax]

    # for each field, plot the frequency
    for i, field in enumerate(fields):
        # call the plot frequency function from graph_utils to draw that fields frequency
        plot_frequency(
            axes=ax[i],
            df=df_filtered,
            column=field,
            percentage_label=include_percentages
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
    

with tab4:
    st.info(":material/grid_on: Correlation Matrix and Heatmaps")

    # Define numerical fields for correlation
    numeric_fields = [ 'year', 'month', 'week_number', 'daily_screen_time_min', 'social_media_time_min',
                    'sleep_hours', 'physical_activity_min', 'negative_interactions_count', 'positive_interactions_count',
                    'interaction_total', 'interaction_negative_ratio', 'anxiety_level', 'stress_level', 'mood_level' ]

    # add multi select to pick fields to plot correlations
    fields = st.multiselect("Select numerical features to compute correlations", 
                           options=numeric_fields, 
                           default=[f for f in numeric_fields if f not in ['year', 'month', 'week_number']])
    
    col1, col2 = st.columns(2)

    with col1:
        # Add a chart type dropdown
        type = st.selectbox("Select chart type", ["Heatmap", "Correlation Matrix"])

    with col2:
        # Add a correlation method dropdown
        method = st.selectbox("Select correlation method", ["Pearson", "Spearman", "Kendall"])

    col1, col2 = st.columns(2)

    with col1:
        # Define decimal options based on chart type
        if type == "Heatmap":
            decimal_options = ["No values shown", "0", "1", "2", "3", "4", "5"]
        else:
            decimal_options = ["0", "1", "2", "3", "4", "5"]

        # User selects number of decimals
        decimals = st.selectbox("Number format, the number of decimal places:", decimal_options, index=2 if type=="Heatmap" else 2)
 
    with col2:
        if type == "Heatmap":
            # Define available colour maps
            colours_list = [
                                {"name": "Yellow Green Blue", "value": "YlGnBu"},
                                {"name": "Cool Warm", "value": "coolwarm"},
                                {"name": "Yellow Orange Brown", "value": "YlOrBr"},
                                {"name": "Viridis", "value": "viridis"},
                                {"name": "Magma", "value": "magma"},
                            ]
            # User selects colour name
            colour_name = st.selectbox("Select colour for Heatmap", [c["name"] for c in colours_list])

            # Get colour map value
            colour_map = next(c["value"] for c in colours_list if c["name"] == colour_name)


    # Determine formatting
    if decimals == "No values shown":
        show_values = False
        fmt = None
    else:
        show_values = True
        fmt = f".{decimals}f"
        table_fmt = f"{{:.{decimals}f}}"

    if len(fields) >= 2:
        # Calculate the correlation values using the selected method
        corr = df_filtered[fields].corr(method=method.lower())

        if (type == "Heatmap"):
            # set figure size
            plt.figure(figsize=(12, 12))

            # Create a heatmap to visually show the correlation
            sns.heatmap(
                corr,
                cmap=colour_map,
                square=True,
                linewidths=1,
                linecolor="white",
                annot=show_values,
                fmt=fmt,
            )
            # Add a title
            plt.title("Correlation Matrix" + f"\n({method} Method)", fontsize=16)
            plt.tight_layout()
            st.pyplot(plt)
        else:
            # Add a matrix title
            st.markdown("**Correlation Matrix**" + f" - ({method} Method)")
            # Display the correlation matrix as a styled dataframe
            st.dataframe(corr.style.format(table_fmt), width="stretch")
    else:
        # Display a warning if less than two features are selected
        st.warning("Please select at least two numerical features to compute correlations.")

with tab5:
    st.info(":material/search_insights: Comparing category vs numeric visualisations")

     # Define numerical fields for distribution plots
    numeric_fields = [ "age", "daily_screen_time_min", "social_media_time_min", "sleep_hours", "physical_activity_min" ]

    # add multi select to pick fields to plot
    fields = st.multiselect("Select numerical features", options=numeric_fields)

    col1, col2 = st.columns(2)

    with col1:
        # define category fields that can be selected
        category_fields = [ 'platform', 'age_group', 'gender', 'mental_state', 'anxiety_level', 'stress_level', 'mood_level' ]

        # add dropdown to select category
        category = st.selectbox("Select Category", options=category_fields, index=0)

    with col2:
        if len(fields) == 0:
            chart_type = None
        else:
            # add dropdown to select chart type
            chart_type = st.selectbox("Select chart type", ["Box Plot", "Violin Plot", "Bar Chart"] if len(fields) == 1 else ["Grouped Bar Chart"], index=0)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)

    match chart_type:
        case "Box Plot":
            # Add a box plot
            sns.boxplot(data=df, x=category, y=fields[0], color="skyblue", ax=ax)
            # Add a title and labels
            ax.set_title(f"{fields[0].replace('_', ' ').title()} by {category.replace('_', ' ').title()}", fontsize=16)
            ax.set_xlabel(category.replace('_', ' ').title())
            ax.set_ylabel(fields[0].replace('_', ' ').title())
        case "Violin Plot":
            # Add a violin plot
            sns.violinplot(data=df, x=category, y=fields[0], inner="quartile", color="skyblue", legend=False, ax=ax)
            # Add a title and labels
            ax.set_title(f"{fields[0].replace('_', ' ').title()} by {category.replace('_', ' ').title()}", fontsize=16)
            ax.set_xlabel(category.replace('_', ' ').title())
            ax.set_ylabel(fields[0].replace('_', ' ').title())
        case "Bar Chart":
            # Add a bar chart
            sns.barplot(data=df, x=category, y=fields[0], color="skyblue", ax=ax)
            # Add a title and labels
            ax.set_title(f"{fields[0].replace('_', ' ').title()} by {category.replace('_', ' ').title()}", fontsize=16)
            ax.set_xlabel(category.replace('_', ' ').title())
            ax.set_ylabel(fields[0].replace('_', ' ').title())
        case "Grouped Bar Chart":
            plot_group_by_bar(
                axes=ax,
                df=df_filtered,
                columns=fields,
                group_by=category,
                title=f"Comparison of " + ", ".join([f.replace('_', ' ').title() for f in fields]) + f" by {category.replace('_', ' ').title()}"
            )
    if chart_type is not None:
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Please select at least one numerical feature to plot. More chart types become available when only one numerical feature is selected.")


with tab6:
    st.info( ":material/looks_one: Comparing numeric vs numeric visualisations as a scatter plot")

    st.caption("Comparing numeric vs numeric visualisations as a scatter plot.")

    # define numeric fields that can be selected
    numeric_fields = [ "age", "social_media_time_min", "daily_screen_time_min", "sleep_hours", "physical_activity_min"]

    # define category fields that can be selected
    category_fields = [ 'age_group', 'platform', 'gender', 'mental_state', 'anxiety_level', 'stress_level', 'mood_level' ]

    col1, col2 = st.columns(2)

    with col1:
        # add dropdown to select x axis
        x_axis = st.selectbox("Select X-Axis", options=numeric_fields, index=0)
    
    with col2:
        # add dropdown to select y axis
        y_axis = st.selectbox("Select Y-Axis", options=numeric_fields, index=1)

    col1, col2 = st.columns(2)

    with col1:
        # add dropdown to select hue
        hue = st.selectbox("Select Category to Colour (Optional)", options=["None"] + category_fields, index=0)

    # create figure
    fig = plt.figure(figsize=(12, 8))

    # create scatter plot
    sns.scatterplot(
        data=df_filtered,
        x=x_axis,
        y=y_axis,
        hue=None if hue == "None" else hue,
        palette=None if hue == "None" else "Set2",
        alpha=0.7
    )

    # Add a title
    plt.title(f"{x_axis.replace('_', ' ').title()} vs {y_axis.replace('_', ' ').title()}", fontsize=16)
    plt.tight_layout()

    # set axis labels
    plt.xlabel(x_axis.replace('_', ' ').title())
    plt.ylabel(y_axis.replace('_', ' ').title())

    # display figure
    st.pyplot(fig)

with tab7:
    st.info(":material/category: Comparing category vs category visualisation as a stacked bar chart")

    # define category fields that can be selected
    category_fields = [ 'platform', 'age_group', 'gender', 'mental_state', 'anxiety_level', 'stress_level', 'mood_level' ]

    col1, col2 = st.columns(2)

    with col1:
        # add dropdown to select x axis
        x_axis = st.selectbox("Select X-Axis category", options=category_fields[:-3], index=0)
    
    with col2:
        # add dropdown to select y axis
        colour_category = st.selectbox("Select colour category", options=category_fields, index=1)

    if x_axis == colour_category:
        st.warning("Please select different categories for X-Axis and Colour.")
    else:
        # create figure
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(1, 1, 1)

        # create stacked bar chart
        plot_stacked_category(
            axes=ax,
            df=df_filtered,
            group_one=x_axis,
            group_two=colour_category,
            title=f"{x_axis.replace('_', ' ').title()} vs {colour_category.replace('_', ' ').title()}"
        )

        # display figure
        st.pyplot(fig)

with tab8:
    st.info(":material/monitoring: Trends Over Time visualisations, with options for aggregation and rolling averages")

    # Define numerical fields for trend over time plots
    available_fields = [ "daily_screen_time_min", "social_media_time_min", "sleep_hours", "physical_activity_min" ]

    # add multi select to pick fields to plot
    fields = st.multiselect("Select features", options=available_fields)

    col1, col2 = st.columns(2)

    with col1:
        # sample frequency dropdown
        frequency = st.selectbox("Select sample frequency", ["Daily", "Weekly", "Monthly"], index=1)

    with col2:
        # select aggregation method
        aggregation_method = st.selectbox("Select aggregation method", ["Mean", "Median", "Sum"], index=0)

    col1, col2, col3 = st.columns(3)

    with col1:
        # Force y-axis to start at 0 toggle
        force_y_zero = st.toggle("Force Y-Axis to start at 0", value=False)
     
    with col2:
        # Show variability band toggle
        show_variability = st.toggle("Show Variability Band", value=False)
    
    with col3:
        # show rolling average
        show_rolling_average = st.toggle("Show Rolling Average", value=False)

    col1, col2 = st.columns(2)

    with col1:
        # rolling window size slider
        if show_rolling_average:
            rolling_window = st.slider("Rolling window size (periods)", 2, 12, 4)        
        else:        
            rolling_window = None
    
    
    if len(fields) == 0:
        st.warning("Please select at least one feature to plot.")
    else:
        # create figure
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(1, 1, 1)

        # create trend over time plot
        plot_trend_over_time(
            ax=ax,
            df=df_filtered,
            fields=fields,
            frequency=frequency,
            aggregation_method=aggregation_method,
            force_y_zero=force_y_zero,
            show_variability=show_variability,
            show_rolling_average=show_rolling_average,
            rolling_window=rolling_window
        )
        # display figure
        st.pyplot(fig)

