<p align="center">
 <img width="100%" src="./images/socail-media-mental-health-banner.jpg " align="center" alt="Project banner" />
 <h1 align="center">Social Media and the effect on Mental Health</h1>
 <p align="center">Analysing social media and mental health data from Kaggle and using machine learning algorithms.</p>
</p>

<p align="center">
  <br/>
  <a href="https://www.python.org/" title="Python official website"><img alt="Python Logo" height="30px" src="./images/python-logo.png" /></a>
  <a href="https://pandas.pydata.org/" title="Pandas official wesbite"><img alt="Pandas Logo" height="30px" src="./images/pandas-logo.png" /></a>
   <a href="https://matplotlib.org/stable/" title="Matplotlib offical website"><img alt="Matplotlib Logo" height="30px" src="./images/matplotlib-logo.png" /></a>
  <a href="https://seaborn.pydata.org/" title="Seaborn offical website"><img alt="Seaborn Logo" height="30px" src="./images/seaborn-logo.png" /></a>
  <a href="https://plotly.com/python/" title="Plotly offical website"><img alt="Plotly Logo" height="30px" src="./images/plotly-logo.png" /></a>
  <a href="https://www.kaggle.com/" title="Kaggle offical website"><img alt="Kaggle Logo" height="30px" src="./images/kaggle-logo.png" /></a>
  <br />
</p>

<p align="center">
  <a href="https://scikit-learn.org/stable/" title="Scikit-learn official website"><img alt="Scikit-learn Logo" height="30px" src="./images/sckit-learn.png" /></a>
  <a href="https://pingouin-stats.org/build/html/index.html" title="Pingouin official wesbite"><img alt="Pingouin Logo" height="30px" src="./images/pingouin.png" /></a>
  <a href="https://scipy.org/" title="SciPy offical website"><img alt="SciPy Logo" height="30px" src="./images/scipy.png" /></a>
  <a href="https://docs.streamlit.io/" title="Streamlit offical website"><img alt="Streamlit Logo" height="30px" src="./images/streamlit.png" /></a>
  <a href="https://feature-engine.trainindata.com/en/latest/" title="Feature-engine offical website"><img alt="Feature-engine Logo" height="30px" src="./images/feature-engine.png" /></a>
  <a href="https://imbalanced-learn.org/stable/" title="Imbalanced-learn offical website"><img alt="Imbalanced-learn Logo" height="30px" src="./images/imbalanced-learn.png" /></a>
  <br />
</p>

<p align="center">
    <a href="https://github.com/users/petedanielsmith/projects/4">Project Board</a>
    &nbsp;&nbsp;-&nbsp;&nbsp;
    <a href="./jupyter_notebooks/01_dataload_clean_and_look_at_distributions.ipynb">Jupyter Notebooks</a>
    &nbsp;&nbsp;-&nbsp;&nbsp;
    <a href="https://social-media-effect-on-mental-health.streamlit.app/">Streamlit Dashboard</a>
    &nbsp;&nbsp;-&nbsp;&nbsp;
    <a href="#conclusions">Conclusions</a>
    <br/><br/><br/>
</p>

<details>
<summary>Project Structure (Click to show)</summary>

- `.devcontainer` - Folder automatically added by Streamlit Cloud to deploy the dashboard
- `.github` - Folder containing user story template for the project board
- `charts` - Folder contains any exported chart images from the Jupyter Notebooks
- `dashboard_app` - root folder of the Streamlit dashnoard app
  - `utils` - folder that contains my shared utility library Python files
    - `graph_utils.py` - Various functions to generate custom charts
  - `model_utils.py`- Funcitons for loading cached models
  - `persona_utils.py` - Functions for loading the cluster data and cleaning it to apply to filter values
  - `ui_components.py` - Single function for a section header that displays a title, number in a circle and horizontal line
  - `main.py` - Main entry point with routing info for the streamlit multi page app
  - `introduction.py` - Introduction page of the dashboard
  - `data_visualisation.py' - Visualisation page for the dashboard
  - `hypothesis_statistical_testing.py` - Hypothesis testing page for the dashboard
  - `clusters.py` - Clutering page for the dashboard
  - `model_overview.py` - Model overview page for the dashboard
  - `model_predictions.py` - Model prediction page for the dashboard
- `data` - Folder to contain the data files
  - `cluster_profiles.parquet` - Exported mean centroid data for each of the clusters
  - `mental_health_social_media_dataset_cleaned.parquet` - Cleaned data file in parquet format to persist data types
  - `mental_health_social_media_dataset_raw.csv` - Original raw dataset downloaded from Kaggle
- `images` - Folder containing any static images used in the readme or dashboard app
- `jupyter_notebooks` - Folder to store the notebooks
  - `01_dataload_clean_and_look_at_distributions.ipynb` - Initial cleaning the data and look at distributions notebook
  - `02_eda_exploratory_data_analysis.ipynb` - Notebook to interogate the data and do the EDA
  - `03_hypothesis_and_statistical_testing.ipynb` - Notebook to carry out the statistical tests
  - `04_clustering.ipynb` - Notebook to do the k-means clustering
  - `05_predicting_mental_state.ipynb` - Notebook to create a model to predict mental state via random forest
  - `06_predicting_sleep.ipynb` - Notebook to create a model to predict sleep hours by linear regression
  - `07_predicting_stress_level.ipynb` - Notebook to create a model to predict stress level by linear regression
  - `08_predicting_anxiety_level.ipynb` - Notebook to create a model to predict anxiety level by linear regression
  - `09_predicting_mood_level.ipynb` - Notebook to create a model to predict mood level
- `models` - Folder to hold the saved ML models in pkl format
- `.gitignore` - List of everything to not include in the git reposiroty
- `README.md` - This readme file
- `requirements.txt` - List of Python libraries and their versions required to use this project

---

</details>

## Dataset Content

The dataset used in this project can be downloaded from [Kaggle: Social Media Mental Health Indicators Dataset](https://www.kaggle.com/datasets/sonalshinde123/social-media-mental-health-indicators-dataset). It captures the relationship between social media usage, screen-time behaviour, and daily lifestyle factors such as sleep duration and interaction quality.

**Columns include:**

- `person_name` - Name or identifier of the person
- `age` - Age of the individual in years
- `date` - Date the results were recorded
- `gender` - Gender (Male, Female or Other)
- `platform` - Primary social media platform used (Instagram, Snapchat, Facebook, WhatsApp, TikTok,
  YouTube, Twitter)
- `daily_screen_time_min` - Number of minutes spent using a screen in a day
- `social_media_time_min` - Number of minutes spent on social media in a day
- `negative_interactions_count` - Number of negative or harmful interactions experienced online
- `positive_interactions_count` - Number of positive or supportive interactions experienced online
- `sleep_hours` - Total number of hours the person sleeps per day
- `physical_activity_min` - Number of minutes spent doing physical activity
- `anxiety_level` - Anxiety level (1-10)
- `stress_level` - Stress level (1-10)
- `mood_level` - Mood level (1-10)
- `mental_state` - Mental state of the individual (Healthy, Stressed or At Risk)

## Business Requirements

- Describe your business requirements

## Hypothesis and how to validate?

- Statistical test methods used:

  - **ANOVA (Analysis of Variance)** - Used when comparing the mean value of a numerical variable across multiple groups
  - **Chi-Square Test of Independence** - Used for relationships between two categorical variables
  - **Correlation Analysis (Pearson & Spearman)** - Used when assessing how two numerical variables move together
    - `Pearson` - linear correlation
    - `Spearman` - monotonic (rank-based) correlation

- Sleep vs Age Group

  - H₀ : Mean sleep hours are equal across age groups
  - H₁ : At least one group differs
  - Method : A one-way ANOVA test

- Stress vs Platform

  - H₀ : Mean stress is equal across platforms
  - H₁ : At least one platform differs
  - Method : A one-way ANOVA test

- Platform vs Mental State

  - H₀ : No association between platform and mental state
  - H₁ : They are associated
  - Method : Chi-Square test

- Sleep vs Mental State

  - H₀ : Sleep is equal across mental states
  - H₁ : At least one mental_state differs
  - Method : A one-way ANOVA test

- Screen Time vs Stress

  - H₀ : No linear correlation
  - H₁ : Linear correlation exists
  - Method : Pearson & Spearman correlation

- Negative Interaction Ratio vs Stress

  - H₀ : No linear correlation
  - H₁ : Linear correlation exists
  - Method : Pearson & Spearman correlation

## Project Plan

The prjoject follows the following steps:

1. `Extract` - Extract the data from Kaggle.
2. `Load` - Load the CSV via Pandas.
3. `Transform` - Clean and process the data using Pandas, adding new columns and checking for missing or duplicated values.
4. `Visualise` - Creating charts with Matplotlib, Seaborn and Plotly to visualise trends and distributions.
5. `Analyse` - Interpret what the visualisations displayed.
6. `Statistical Tests` - Run statistical tests to accept or reject hypothesises.
7. `Unupervised Learning` - Use K-Means to cluster the data in to similar groups.
8. `Supervised Learning` - Use both Linear Regression and Random Forrest machine learning to create predictive models.
9. `Interactive Dashboard` - Use Streamlit to create an interactive dasboard that allows a user to both interogate the data and run predictions using new unseen data.
10. `Document` - Record findings and conclusions.

## The rationale to map the business requirements to the Data Visualisations

- List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used

- List the data analysis methods used and explain limitations or alternative approaches.
- How did you structure the data analysis techniques. Justify your response.
- Did the data limit you, and did you use an alternative approach to meet these challenges?
- How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations

- Were there any data privacy, bias or fairness issues with the data?
- How did you overcome any legal or societal issues?

## Dashboard Design

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
- How were data insights communicated to technical and non-technical audiences?
- Explain how the dashboard was designed to communicate complex data insights to different audiences.

## Unfixed Bugs

- Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
- Did you recognise gaps in your knowledge, and how did you address them?
- If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap

- What challenges did you face, and what strategies were used to overcome these challenges?
- What new skills or tools do you plan to learn next based on your project experience?

## Conclusions

## Deployment

The dashboard app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud) and can be accessed by visiting this URL in a web browser:

[https://social-media-effect-on-mental-health.streamlit.app/](https://social-media-effect-on-mental-health.streamlit.app/)

## Main Data Analysis Libraries

The libraries used for data analysis were:

1. `Pandas` - For data loading, transforming and cleaning.
2. `NumPy` - For data transforming.
3. `Matplotlib` - For overall multi chart layouts.
4. `Seaborn` - For a lot of the individual charts.
5. `Plotly` - For interactive charts.
6. `SciPy` - For statistical tets.
7. `Pingouin` - For statistical tets.
8. `Scikit-learn` - For machine learning alogrithms.
9. `Feature-engine` - For feature engineering.
10. `Imbalanced-learn` - For SMOTE when dealing with imbalanced datasets.
11. `Joblib` - For saving and loading models.
12. `Streamlit` - For creating an interactive web dashboard.

## Credits

### Content

- [Code institute](https://codeinstitute.net/) - The intial project structure and the LMS (Learning Managment System) from the course.
- [Kaggle](https://www.kaggle.com/) - Providing the data set used.
- [ChatGPT](https://chatgpt.com/) - Used to invent the user personas from my centroid means, rewriting contnent sections in notebooks and dashboard, bouncing ideas off and refactoring some code.
- [Github Copiolot](https://github.com/features/copilot) - Adding function docstrings and commenting code and speeding up repetative tasks.
- [Streamlit API Documentation](https://docs.streamlit.io/develop/api-reference) - One of the best, easy to use, product API documentation I have used.
- [SimpleSteps.guide](https://simplesteps.guide/guides/technology/machine-learning-ai) - My notes I recorded from the Code Institute course.

### Media

- [Google AI - Gemini 3](https://deepmind.google/models/gemini/) - AI generated persona images for the dashboard cluster page and banner logo for this README file.
- [Google Material Icons](https://fonts.google.com/icons) - Icons in the dashboard.
- [Code Institute](https://codeinstitute.net/) - Code Institute logo.
- [Python](https://www.python.org/) - Python logo image.
- [Pandas](https://pandas.pydata.org/) - Pandas logo image.
- [Matplotlib](https://matplotlib.org/) - Matplotlib logo image.
- [Seaborn](https://seaborn.pydata.org/) - Seaborn logo image.
- [Plotly](https://plotly.com/python/) - Plotly logo image.
- [Kaggle](https://www.kaggle.com/) - Kaggle logo image.
- [Scikit-learn](https://scikit-learn.org/stable/) - Scikit-learn logo image.
- [Pingouin](https://pingouin-stats.org/build/html/index.html) - Pingouin logo image.
- [SciPy](https://scipy.org/) - SciPy logo image.
- [Streamlit](https://docs.streamlit.io/) - Steamlit logo image.
- [Feature-engine](https://feature-engine.trainindata.com/en/latest/) - Feature-engine logo image.
- [Imbalanced-learn](https://imbalanced-learn.org/stable/) - Imbalanced-learn logo image.

## Acknowledgements (optional)

- Thank the people who provided support through this project.
