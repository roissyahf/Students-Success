# Students' Performance Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://students-success.streamlit.app/)

## 🔍 About the project

This Streamlit application empowers higher education institution to predict students' dropout and academic success. By predicting students' success, education institution can improve the efficiency and quality of teaching and learning, and hence can reduce the dropout rate.

The dataset used to build the classification model, includes information known at the time of student enrollment (academic path, demographics, and social-economic factors) and the students' academic performance at the end of the first and second semesters.

## ⚒️ Setup environment
```
conda create --name student-performance-app python=3.9
conda activate student-performance-app
pip install streamlit pickle-mixin pandas
```

## 🚀 Run streamlit app
```
streamlit run app.py
```

## Business Understanding
Jayajaya Institute is one of the educational institutions that has been established since 2000. To date it has produced many graduates with an excellent reputation. However, there are also many students who do not complete their education, aka dropouts. This high number of dropouts is certainly one of the big problems for an educational institution. Therefore, Jayajaya Institute wants to detect as soon as possible students who might drop out so that they can be given special guidance.

## Business Problem
The problem Jayajaya Institute trying to solve is drop out students, they need to identify what causes the problem and then need to monitor the student performance via dashboard. 

### Project Scope
This project will be focus on two things: extracting insights from the given dataset to draw action item so that the institute can reduce the high number of dropouts, and build a machine learning model to predict whether the student potentially will dropout, enroll, or graduate. The machine learning model be deployed using streamlit, allowing easy access for end user.

### Steps

1. Data wrangling including data gathering, assesing data, and cleaning the data
2. Ask initial questions, then answer it by creating charts which then will be used to create monitoring dashboard
3. Exploratory data analysis by conducting bivariate and multivariate analysis
4. Model preprocessing, by encoding categorical features then splitting data into train and test set
5. Model training, by comparing performance of boosting and tree-based algorithms to find the best performing model with the highest recall score
6. Model evaluation, make used of hyperparameter tuning for the best performing model discovered so that recall score can increase
7. Model deployment, create simple UI using streamlit so that the user can easily predict the students' performance

### Preparation

[Click to see the data source](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance). We need to use jupyter notebook for data exploration and model experimentation, utilized Tableau Public to create dashboard, and streamlit for model deployment.

## Initial Questions
Here's the initial questions that will be answered in dashboard:

1. How many students does Jayajaya Institute have?, how many dropout students, and how's the dropout rate?
2. How's the dropout rate by course?
3. How's the dropout rate by previous qualification grade vs admission grade?
4. How's the proportion of gender dropout rate for different age group (18-25, 26-35, 36-45, 46-55, 56-65, Over 65)?
5. Is there any correlation between curricular units 1st semester approved and curricular units 2nd semester approved with the dropout status?
6. Is there any correlation between curricular units 1st semester evaluated and curricular units 2nd semester evaluations with the dropout status?

## Business Dashboard
This is a single page dashboard, with focus on showing how's the difference between dropout, enrolled, and graduated status across course, admission grade, previous qualification grade, and age group. [Here's the link to access the dashboard.](https://public.tableau.com/shared/XNP2X9NDR?:display_count=n&:origin=viz_share_link)

## Information discovered
1. Jayajaya institute have 4424 students, 1421 of them are dropout and hence the dropout rate is quite high at 32.12%.
2. The course with the highest number of dropout is Management (evening attendance) at 136, while Biofuel Production Technology has the lowest number of dropout rate at 8. 
3. Students with a fair previous qualification grade have the highest dropout rate at 40.22%. Conversely, students with an excellent admission grade have the lowest dropout rate at 4.88%. 
4. It reveals that younger students (18-25) have the highest overall dropout rate (58.9%), with a nearly even split between males (27.02%) and females (31.88%). This number is quite large because the majority of students are 18-25 years old. Dropout rates decrease steadily for each age group after that, with the lowest dropout rate among students at age of 56-65 (0.42%). This finding is also due to the fact that only a few students are in that age range.
5. A cluster of green dots (graduated students) in the upper right quadrant both in scatter plot of curricular units approved and in scatter plot of curricular units evaluated would indicate that students who approved more curricular units in both semesters were more likely to graduate.

## Conclusion
1. It was found that factors contribute to high number of student dropout rate in Jayajaya Insitute are: curricular units 1st and 2nd semester enrolled, curricular units 1st and 2nd semester approved, curricular units 1st and 2nd semester evaluations, curricular units 1st and 2nd semester grades, course, age at enrollment, previous qualification grade, and admission grade.
2. From the experimentation, the best model to predict students' success is LGBM, with recall score in enrolled class is 0.85, recall score in graduate class is 0.87, and recall score in dropout class is 0.92. From 35 features available in the dataset, only 13 features used as predictor. The top 5 most importance variables of the model are: admission grade, curricular units 2nd semester grade, previous qualification grade, curricular units 1st semester grade, and course.

## Action Items Recommendation
1. Targeted Support for Evening Attendance Students
The data shows that Management (evening attendance) has the highest dropout rate. This suggests that the institute investigate the specific challenges faced by evening attendance students and develop targeted support programs to address them. This could involve offering additional academic assistance, improved time management resources, or childcare options for students with families.

2. Early Intervention for Students with Fair Grades
The finding that students with a fair previous qualification grade have the highest dropout rate suggests that Jayajaya Institute implement early intervention strategies for these at-risk students. This could involve providing academic mentoring, tutoring services, or study skills workshops. Early intervention can help these students get back on track and improve their chances of success.

3. Focus on Young Adult Students
While the overall dropout rate is high for younger students (18-25), it's important to consider that this is also the largest age group. However, the finding that the dropout rate is still significantly higher than other age groups suggests that the institute develop programs specifically tailored to the needs of younger students. This could involve orientation programs to help students adjust to college life, social support groups to combat loneliness, or mental health resources to address anxieties or stress.

4. Analyze Curricular Unit Data
The scatter plots on curricular units suggest a possible link between course completion and graduation rates. Jayajaya Institute should delve deeper into this data to identify specific curricular units that tend to be problematic for students. Are there units with a higher dropout rate? Are there units that graduating students consistently perform well in?  By identifying these trends, the institute can re-evaluate the curriculum or provide additional support for challenging courses.