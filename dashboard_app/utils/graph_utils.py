import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_distribution(
    axes, type, df, column, bins, kde,
    mean, median, std, q1, q3, iqr,
    skew, kurtosis, count
):
    """
    Plots the distribution of a numerical column using various plot types
    and annotates it with optional summary statistics.

    Parameters:
    - axes : The axes on which to plot
    - type : The type of plot to create. Options: "Histogram", "Histogram & KDE", "Violin Plot", "Box Plot", "Violin Plot & Box Plot"
    - df : The DataFrame containing the data
    - column : The column name of the numerical data to plot
    - bins : Number of bins for histogram
    - kde : Whether to include KDE in histogram
    - mean : Whether to annotate mean
    - median : Whether to annotate median
    - std : Standard deviation annotation option: "None", "1 SD", "2 SD", "3 SD"
    - q1 : Whether to annotate first quartile
    - q3 : Whether to annotate third quartile
    - iqr : Whether to annotate interquartile range fences
    - skew : Whether to include skewness in subtitle
    - kurtosis : Whether to include kurtosis in subtitle
    - count : Whether to include count in subtitle
   
    Returns:
    - None
    """

    # Get series and formatted title
    series = df[column]
    col_title = column.replace("_", " ").title()
    
    # plot based on type
    match type:
        case "Histogram" | "Histogram & KDE":
            # Plot histogram + KDE
            sns.histplot(data=df, x=column, kde=kde, bins=bins, color="skyblue", ax=axes)
        case "Violin Plot":
            sns.violinplot(data=df, x=column, inner="quartile", color="skyblue", ax=axes)
        case "Box Plot":
            sns.boxplot(data=df, x=column, color="skyblue", ax=axes)
        case "Violin Plot & Box Plot":
            # Plot violin plot + box plot 
            sns.violinplot(
                data=df,
                x=column,
                inner=None,
                color="skyblue",
                ax=axes
            )
            sns.boxplot(
                data=df,
                x=column,
                width=0.2,
                color="white",
                ax=axes
            )

    # Build subtitle
    sub_parts = []
    if skew:
        sub_parts.append(f"Skewness: {series.skew():.2f}")
    if kurtosis:
        sub_parts.append(f"Kurtosis: {series.kurtosis():.2f}")
    if count:
        sub_parts.append(f"Count: {series.count()}")

    # Format subtitle to add pipe separators if multiple parts
    sub_text = " | ".join(sub_parts)

    # Add Title + subtitle
    if sub_text:
        axes.set_title(f"{col_title}\n{sub_text}", fontsize=16, pad=20)
    else:
        axes.set_title(f"{col_title}", fontsize=16)

    # Set axis labels
    axes.set_xlabel(col_title)
    axes.set_ylabel("Frequency")

    # Set annotations positions so that they don't overlap if multiple are selected
    y_start = 0.95     # start just under the top of plot
    y_step  = -0.05    # move DOWN for each extra label
    y_pos   = y_start

    def annotate_line(x, label, color):
        """Helper function to annotate a vertical line on the plot."""
        nonlocal y_pos
        axes.axvline(x, color=color, linestyle="dashed", linewidth=2)
        axes.text(
            x, y_pos,
            label,
            ha="center", va="top",
            transform=axes.get_xaxis_transform(),  # FIXED
            fontsize=12, color=color
        )
        y_pos += y_step

    # Summary stats calculations for annotations
    mean_val = series.mean()
    median_val = series.median()
    std_val = series.std()
    q1_val = series.quantile(0.25)
    q3_val = series.quantile(0.75)
    iqr_val = q3_val - q1_val

    # Add annotations based on user selections
    if mean:
        # Annotate mean
        annotate_line(mean_val, "Mean", "r")
    if median:
        # Annotate median
        annotate_line(median_val, "Median", "b")
    if q1:
        # Annotate first quartile
        annotate_line(q1_val, "Q1", "m")
    if q3:
        # Annotate third quartile
        annotate_line(q3_val, "Q3", "m")
    if iqr:
        # Annotate IQR ranges
        annotate_line(q1_val - 1.5*iqr_val, "Q1 - 1.5 IQR", "y")
        annotate_line(q3_val + 1.5*iqr_val, "Q3 + 1.5 IQR", "y")

    # Add standard deviation annotations
    if std in ("1 SD", "2 SD", "3 SD"):
        annotate_line(mean_val + std_val, "+1σ", "g")
        annotate_line(mean_val - std_val, "-1σ", "g")

        # Add 2 SD annotations
        if std in ("2 SD", "3 SD"):
            annotate_line(mean_val + 2*std_val, "+2σ", "orange")
            annotate_line(mean_val - 2*std_val, "-2σ", "orange")

        # Add 3 SD annotations
        if std == "3 SD":
            annotate_line(mean_val + 3*std_val, "+3σ", "purple")
            annotate_line(mean_val - 3*std_val, "-3σ", "purple")

    # Adjust layout to prevent clipping
    axes.figure.tight_layout()



def plot_frequency(axes, df, column, percentage_label):
    """
    Plots the frequency distribution of a categorical column as a bar plot,
    with optional percentage labels on each bar.
    
    Parameters:
    - axes : The axes on which to plot
    - df : The DataFrame containing the data
    - column : The column name of the categorical data to plot
    - percentage_label : Whether to include percentage labels on bars
    
    Returns:
    - None
    """
    
    # Draw the bar plot
    sns.countplot(x=column, data=df, color="skyblue", ax=axes)
    
    # Set labels
    axes.set_title(column.replace("_", " ").title(), fontsize=16)
    axes.set_ylabel("Frequency")
    axes.set_xlabel(column.replace("_", " ").title())

    if percentage_label:
        # Calculate counts and percentages
        total = len(df)
        
        # Loop through bars
        for p in axes.patches:
            height = p.get_height()
            percentage = 100 * height / total
            axes.text(
                p.get_x() + p.get_width() / 2,   # x position (center of bar)
                height,                          # y position (top of bar)
                f"{percentage:.1f}%",            # label text
                ha="center", va="bottom",        # alignment
                fontsize=10
            )


def plot_stacked_category(axes, df, group_one, group_two, title):
    """
    Plots a 100% stacked bar chart for two categorical variables.
    
    Parameters:
    - axes: matplotlib Axes object
    - df: DataFrame
    - group_one: main x-axis category
    - group_two: sub-category stacked in each bar
    - title: chart title
    """

    # Compute counts
    counts = (
        df.groupby([group_one, group_two], observed=False)
          .size()
          .reset_index(name="count")
    )

    # Compute total per group_one
    totals = counts.groupby(group_one, observed=False)["count"].transform("sum")

    # Compute proportions
    counts["proportion"] = counts["count"] / totals

    # Pivot for stacked bar format
    stacked = counts.pivot(index=group_one, columns=group_two, values="proportion").fillna(0)

    # Plot 100% stacked bars
    bottom = np.zeros(len(stacked))

    # Set colours
    colours = sns.color_palette("pastel", len(stacked.columns))

    # Plot stacked bars
    for col, colour in zip(stacked.columns, colours):
        axes.bar(
            stacked.index,
            stacked[col],
            bottom=bottom,
            label=col,
            width=0.7,
            color=colour
        )
        bottom += stacked[col]

    # Set titles and labels
    axes.set_title(title)
    axes.set_ylabel("Proportion")
    axes.set_xlabel(group_one.replace("_", " ").title())
    axes.legend(title=group_two)

    # Show percentages on bars
    # Iterate through each main category
    for i, category in enumerate(stacked.index):
        cumulative = 0
        # Iterate through each sub-category
        for col in stacked.columns:
            value = stacked.loc[category, col]
            # Only show values > 3% due to space
            if value > 0.03:
                # Show percentage text
                axes.text(
                    i, 
                    cumulative + value / 2,
                    f"{value*100:.0f}%",
                    ha="center",
                    va="center",
                    fontsize=9,
                    color="black"
                )
            # Update cumulative value
            cumulative += value