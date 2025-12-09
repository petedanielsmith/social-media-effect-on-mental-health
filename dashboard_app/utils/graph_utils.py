import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_distribution(
    axes, type, df, column, bins, kde,
    mean, median, std, q1, q3, iqr,
    skew, kurtosis, count
):

    series = df[column]
    col_title = column.replace("_", " ").title()

    box = None
    
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

    sub_text = " | ".join(sub_parts)

    # Title + subtitle
    if sub_text:
        axes.set_title(f"Histogram of {col_title}\n{sub_text}", fontsize=16, pad=20)
    else:
        axes.set_title(f"Histogram of {col_title}", fontsize=16)

    axes.set_xlabel(col_title)
    axes.set_ylabel("Frequency")

    # ---- Annotation rows INSIDE the plot ----
    y_start = 0.95     # start just under the top of plot
    y_step  = -0.05    # move DOWN for each extra label
    y_pos   = y_start

    def annotate_line(x, label, color):
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

    # Summary stats
    mean_val   = series.mean()
    median_val = series.median()
    std_val    = series.std()
    q1_val     = series.quantile(0.25)
    q3_val     = series.quantile(0.75)
    iqr_val    = q3_val - q1_val

    # Add annotations
    if mean:
        annotate_line(mean_val, "Mean", "r")
    if median:
        annotate_line(median_val, "Median", "b")
    if q1:
        annotate_line(q1_val, "Q1", "m")
    if q3:
        annotate_line(q3_val, "Q3", "m")
    if iqr:
        annotate_line(q1_val - 1.5*iqr_val, "Q1 - 1.5 IQR", "y")
        annotate_line(q3_val + 1.5*iqr_val, "Q3 + 1.5 IQR", "y")

    if std in ("1 SD", "2 SD", "3 SD"):
        annotate_line(mean_val + std_val, "+1σ", "g")
        annotate_line(mean_val - std_val, "-1σ", "g")

        if std in ("2 SD", "3 SD"):
            annotate_line(mean_val + 2*std_val, "+2σ", "orange")
            annotate_line(mean_val - 2*std_val, "-2σ", "orange")

        if std == "3 SD":
            annotate_line(mean_val + 3*std_val, "+3σ", "purple")
            annotate_line(mean_val - 3*std_val, "-3σ", "purple")

    axes.figure.tight_layout()


