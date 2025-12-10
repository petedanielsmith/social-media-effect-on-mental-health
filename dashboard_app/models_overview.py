import streamlit as st

st.set_page_config(
    layout="wide",
)

st.write("# " + ":material/schema:" + " Models Overview")

st.caption("Overview of all the models created for the project and their types and parameters.")

st.write("## Overview of the Machine Learning Models")

st.markdown("""
This page summarises all machine learning models developed for the project.  
Each model was trained using the cleaned dataset, evaluated on held-out test data, and interpreted in the context of the behavioural patterns observed in the EDA.
All models share a consistent preprocessing pipeline that ensures fair handling of numerical and categorical features.

---

# **Shared Preprocessing Pipeline**

Before data reaches any model, it goes through a unified preprocessing stage:

- **Numerical features** → `StandardScaler()`
- **Categorical features** → `OneHotEncoder(handle_unknown="ignore")`
- **Class imbalance handling** → `SMOTE(random_state=42)`

SMOTE was used for the mental-state prediction model because the dataset is imbalanced (e.g., far more “Stressed” users than “At Risk”). SMOTE synthesises new minority samples, helping the classifier avoid bias toward majority classes.

---

# **1. Mental State Classification Model**

**Model type:** Random Forest Classifier  
**Pipeline:** Preprocessing → SMOTE → RandomForest  
**Hyperparameter search:** GridSearchCV (5-fold CV)  
**Best parameters identified:**

- `n_estimators = 100`  
- `max_depth = None`  
- `min_samples_split = 2`  
- `min_samples_leaf = 1`

**Performance (Test Set):**

| Metric | Value |
|--------|--------|
| Accuracy | **1.00** |
| Precision | **1.00** |
| Recall | **1.00** |
| F1-score | **1.00** |

The model perfectly predicted all mental-state labels.

### **Feature Importance Summary**
The most influential predictors were:

- Daily screen time
- Stress  
- Physical activity 
- Social media time
- Sleep hours  
- Mood  
- Anxiety  
- Age
 

Demographic features (e.g., gender, platform) contributed very little.  
This aligns with EDA findings: *behaviour outweighs identity* in predicting mental state.

### **Conclusion**
The classifier performs exceptionally well and generalises perfectly on both test data and synthetic cluster personas. Its behaviour aligns closely with the dataset's structured relationships.

---

# **2. Sleep Prediction Model**

**Model type:** Linear Regression  
**Pipeline:** Preprocessing → LinearRegression

**Performance:**

| Metric | Value |
|--------|--------|
| MAE | **0.025** |
| RMSE | **0.028** |
| R² | **0.997** |

### Interpretation
The scatter plot showed an almost perfect diagonal line:  
predicted values nearly match actual values with extremely small deviations.

Sleep is highly predictable in this dataset and is strongly linked to:

- Screen time  
- Physical activity  
- Mood / stress  
- Negative interaction ratio  

### Conclusion
The sleep regression model is highly accurate, generalises well to personas, and captures the behavioural structure extremely effectively.

---

# **3. Stress Level Prediction Model**

**Model type:** Linear Regression  
**Performance:**

| Metric | Value |
|--------|--------|
| MAE | **0.153** |
| RMSE | **0.204** |
| R² | **0.964** |

### Interpretation
The scatterplot shows a tight band around the diagonal.  
Residuals are normally distributed and centred around zero.

### Conclusion
Stress levels can be predicted very reliably from behavioural and emotional factors.  
The model aligns extremely well with observed trends and generalises smoothly.

---

# **4. Anxiety Level Prediction Model**

**Model type:** Linear Regression  
**Performance:**

| Metric | Value |
|--------|--------|
| MAE | **0.193** |
| RMSE | **0.243** |
| R² | **0.912** |

### Interpretation
Predictions increase smoothly with actual anxiety levels.  
Some small scatter appears—but no bias or structural patterns.

### Conclusion
Anxiety is naturally more variable, but still highly predictable.  
The model remains consistent with both test data and cluster personas.

---

# **5. Mood Level Prediction Model**

**Model type:** Linear Regression  
**Performance:**

| Metric | Value |
|--------|--------|
| MAE | **0.178** |
| RMSE | **0.223** |
| R² | **0.918** |

### Interpretation
Predicted mood follows a strong, clean linear relationship with actual mood.  
Residuals are small and centered.

### Conclusion
Mood is highly predictable using behavioural features, especially emotional metrics (stress, anxiety) and lifestyle indicators (sleep, activity).

---

# **Overall Summary**

Across all models:

- Behavioural and emotional variables are far more predictive than demographics.
- Linear models perform exceptionally well due to the structured synthetic dataset.
- The classification model benefits significantly from SMOTE and rich behavioural features.
- All regression models generalise cleanly to persona clusters.

These results reinforce earlier findings from EDA, clustering, and hypothesis testing, showing that digital behaviour and emotional state strongly explain well-being variables in the dataset.

---
""")
