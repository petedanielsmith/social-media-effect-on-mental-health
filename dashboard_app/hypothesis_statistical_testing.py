import streamlit as st

st.set_page_config(layout="wide")

st.write("# " + ":material/experiment:" + " Hypothesis & Statistical Testing")
st.caption("Overview of the hypotheses tested, the statistical methods applied, and the conclusions drawn from the results.")

st.markdown("---")

st.subheader("Purpose of the Statistical Tests")

st.markdown("""
The goal of the hypothesis testing phase was to formally assess whether the patterns observed 
in the exploratory data analysis were statistically meaningful.  
To do this, I evaluated relationships between:

- **Numerical vs categorical variables** using **ANOVA**  
- **Categorical vs categorical variables** using **Chi-square tests**  
- **Numerical vs numerical variables** using **correlation analysis** (Pearson & Spearman)

These tests ensure the findings are not due to random variation, even though the dataset 
is synthetic and patterns are intentionally strong.
""")

st.markdown("---")


st.subheader("Statistical Methods Used")

st.markdown("""
### **ANOVA (Analysis of Variance)**
Used when comparing the **mean value of a numerical variable across multiple groups**  
(e.g., sleep across age groups, stress across platforms).  
ANOVA works well here thanks to a large sample size, which makes it robust to mild violations of normality.

---

### **Chi-Square Test of Independence**
Used for relationships between **two categorical variables**  
(e.g., platform × mental state).  
It checks whether the distribution of categories differs significantly across groups.

---

### **Correlation Analysis (Pearson & Spearman)**
Used when assessing how **two numerical variables** move together  
(e.g., screen time vs stress).  

- **Pearson** → linear correlation  
- **Spearman** → monotonic (rank-based) correlation  

Using both provides a more reliable insight into potential nonlinear relationships.
""")

st.markdown("---")


st.subheader("Results for Each Hypothesis")

# Sleep vs Age Group expander
with st.expander("**Sleep vs Age Group** — ANOVA"):
    st.markdown("""
**Hypotheses:**

- **H₀:** Mean sleep hours are equal across age groups  
- **H₁:** At least one age group has a different mean sleep duration  

**Results:**  
A one-way ANOVA showed extremely large differences in sleep hours across age groups:

- **F = 5898.93**  
- **p < 0.001**  
- **η² = 0.855** (very large effect)

Age group alone explained **≈ 85%** of the variance in sleep, which is unusually high for behavioural data 
and reflects the synthetic nature of the dataset.

**Conclusion:**  
I **reject H₀** and accept **H₁** — sleep duration differs significantly across age groups.
""")


# Stress vs Platform expander
with st.expander("**Stress vs Platform** — ANOVA"):
    st.markdown("""
**Hypotheses:**

- **H₀:** Mean stress level is equal across platforms  
- **H₁:** At least one platform differs  

**Results:**  
ANOVA revealed a significant difference in stress levels across platforms:

- **F = 196.19**  
- **p < 0.001**  
- **η² = 0.191**

Platforms explain about **19%** of the variance in stress.

**Conclusion:**  
We **reject H₀** — stress level varies significantly between platforms.
""")


# Platform vs Mental State expander
with st.expander("**Platform vs Mental State** — Chi-Square Test"):
    st.markdown("""
**Hypotheses:**

- **H₀:** No association between platform and mental state  
- **H₁:** Platform and mental state are associated  

**Results:**  

- **Chi-square = 466.00**  
- **p < 0.001**  
- **dof = 12**

This shows a strong dependency between the two variables.

**Conclusion:**  
 I **reject H₀** — platform choice is strongly associated with mental state.
""")


# Sleep vs Mental State expander
with st.expander("**Sleep vs Mental State** — ANOVA"):
    st.markdown("""
**Hypotheses:**

- **H₀:** Sleep hours are equal across mental states  
- **H₁:** At least one mental state differs  

**Results:**  

- **F = 827.30**  
- **p < 0.001**  
- **η² = 0.249**

Mental state explains ~25% of the variance in sleep duration.

**Conclusion:**  
I **reject H₀** — sleep differs significantly across mental-state categories.
""")


# Screen Time vs Stress expander
with st.expander("**Screen Time vs Stress** — Correlation"):
    st.markdown("""
**Hypotheses:**

- **H₀:** No linear correlation  
- **H₁:** Linear correlation exists  

**Results:**

- **Pearson r = 0.836 (p < 0.001)**  
- **Spearman ρ = 0.812 (p < 0.001)**  

Both indicate a **very strong positive relationship**.

**Conclusion:**  
I **reject H₀** — higher screen time is strongly associated with higher stress.
""")


# Screen Time vs Stress expander
with st.expander("**Negative Interaction Ratio vs Stress** — Correlation"):
    st.markdown("""
**Hypotheses:**

- **H₀:** No linear correlation  
- **H₁:** Linear correlation exists  

**Results:**

- **Pearson r = 0.443 (p < 0.001)**  
- **Spearman ρ = 0.294 (p < 0.001)**  

This is a **moderate** positive correlation.

**Conclusion:**  
I **reject H₀** — a higher proportion of negative interactions relates to higher stress.
""")


st.markdown("---")


st.subheader("Overall Interpretation")

st.markdown("""
The statistical tests strongly support the patterns found in the visual EDA:

- Sleep varies substantially across age groups and mental-state categories  
- Platform choice relates meaningfully to stress and mental state  
- Higher screen time strongly corresponds to higher stress  
- Negative interaction ratio shows a moderate but significant correlation with stress  

These effects are larger than typically seen in real-world behavioural datasets, 
which is expected given the synthetic nature of the data.

The combined results provide a clear confirmation of meaningful structure in the dataset.
""")
