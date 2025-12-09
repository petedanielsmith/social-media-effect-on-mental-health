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

- List here your project hypothesis(es) and how you envision validating it (them)

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

Todo

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

- In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

- Thank the people who provided support through this project.
