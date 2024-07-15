import streamlit as st
import pickle
import pandas as pd

# load the model
model = pickle.load(open('model.pkl', 'rb'))

# add title
st.set_page_config(page_title="Predict Students Performance", page_icon=":school:")
st.title('Predict Students Performance')
st.write('Can we predict students status? whether they will be graduated, dropout, or enrolled?')

# CREATE UI
# create columns 1, 2
col1, col2 = st.columns(2)
with col1:
    Curricular_units_2nd_sem_approved = st.number_input("Number of curricular units approved by the student in the 2nd semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=20, value=None, step=1)

with col2:
    Curricular_units_1st_sem_approved = st.number_input("Number of curricular units approved by the student in the 1st semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=26, value=None, step=1)
    

# create columns 3, 4
col3, col4 = st.columns(2)

with col3:
    Curricular_units_2nd_sem_grade = st.number_input("2nd semester grade",
                                                        placeholder="Type grade...",
                                                        min_value=0.0, max_value=18.571, value=None)

with col4:
    Curricular_units_1st_sem_grade = st.number_input("1st semester grade",
                                                        placeholder="Type grade...",
                                                        min_value=0.0, max_value=18.875, value=None)
    

# create columns 5, 6
col5, col6 = st.columns(2)

with col5:
    Tuition_fees_up_to_date = st.selectbox(
            "Does tuition fees up to date?",
            ("Yes", "No"),
            index=None,
            placeholder="Select tuition fees up to date...")
    
with col6:
    Curricular_units_2nd_sem_evaluations = st.number_input("Number of curricular units evaluated by the student in the 2nd semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=33, value=None, step=1)

# create columns 7, 8
col7, col8 = st.columns(2)

with col7:
    Curricular_units_1st_sem_evaluations = st.number_input("Number of curricular units evaluated by the student in the 1st semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=12, value=None, step=1)

with col8:
    Curricular_units_1st_sem_enrolled = st.number_input("Number of curricular units enrolled by the student in the 1st semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=26, value=None, step=1)

# create columns 9, 10
col9, col10 = st.columns(2)

with col9:
    Curricular_units_2nd_sem_enrolled = st.number_input("Number of curricular units enrolled by the student in the 2nd semester",
                                                        placeholder="Type number of curricular...",
                                                        min_value=0, max_value=23, value=None, step=1)

with col10:
    Course = st.selectbox(
            "Select one course",
            (
                '33 - Biofuel Production Technologies',
                '171 - Animation & Multimedia Design',
                '8014 - Social Service (evening attendance)',
                '9003 - Agronomy',
                '9070 - Communication Design',
                '9085 - Veterinary Nursing',
                '9119 - Informatics Engineering',
                '9130 - Equinculture',
                '9147 - Management',
                '9238 - Social Service',
                '9254 - Tourism',
                '9500 - Nursing',
                '9556 - Oral Hygiene',
                '9670 - Advertising & Marketing Management',
                '9773 - Journalism & Communication',
                '9853 - Basic Education',
                '9991 - Management (evening attendance)'
            ),
            index=None,
            placeholder="Select one course...")

# create columns 11, 12
col11, col12 = st.columns(2)

with col11:
    Age_at_enrollment = st.number_input("Age of enrollment",
                                        placeholder="Type student age...",
                                        min_value=17, max_value=70, value=None, step=1)

with col12:
    Previous_qualification_grade = st.number_input("Previous qualification grade",
                                        placeholder="Type previous qualification grade...",
                                        min_value=95.0, max_value=190.0, value=None)

# last column
Admission_grade = st.number_input("Admission grade",
                                placeholder="Type admission grade...",
                                min_value=95.0, max_value=190.0, value=None)

# store input in pandas dataframe
user_input = pd.DataFrame([[
        Curricular_units_2nd_sem_approved, Curricular_units_1st_sem_approved, Curricular_units_2nd_sem_grade,
       Curricular_units_1st_sem_grade, Tuition_fees_up_to_date, Curricular_units_2nd_sem_evaluations,
       Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_enrolled,
       Curricular_units_2nd_sem_enrolled, Course, Age_at_enrollment,
       Previous_qualification_grade, Admission_grade
]],
        columns=[
       'Curricular_units_2nd_sem_approved',
       'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_grade',
       'Curricular_units_1st_sem_grade', 'Tuition_fees_up_to_date',
       'Curricular_units_2nd_sem_evaluations',
       'Curricular_units_1st_sem_evaluations',
       'Curricular_units_1st_sem_enrolled',
       'Curricular_units_2nd_sem_enrolled', 'Course', 'Age_at_enrollment',
       'Previous_qualification_grade', 'Admission_grade'
                        ])

# encode tuition up to date
def encode_tuition_update(tuition):
    return tuition.apply(lambda x: 1 if x=='Yes' else 0)

user_input['Tuition_fees_up_to_date'] = encode_tuition_update(user_input['Tuition_fees_up_to_date'])

# encode course name
def encode_course(course):
    if course == '33 - Biofuel Production Technologies':
        return 33
    elif course == '171 - Animation & Multimedia Design':
        return 171
    elif course == '8014 - Social Service (evening attendance)':
        return 8014
    elif course == '9003 - Agronomy':
        return 9003
    elif course == '9070 - Communication Design':
        return 9070
    elif course == '9085 - Veterinary Nursing':
        return 9085
    elif course == '9119 - Informatics Engineering':
        return 9119
    elif course == '9130 - Equinculture':
        return 9130
    elif course == '9147 - Management':
        return 9147
    elif course == '9238 - Social Service':
        return 9238
    elif course == '9254 - Tourism':
        return 9254
    elif course == '9500 - Nursing':
        return 9500
    elif course == '9556 - Oral Hygiene':
        return 9556
    elif course == '9670 - Advertising & Marketing Management':
        return 9670
    elif course == '9773 - Journalism & Communication':
        return 9773
    elif course == '9853 - Basic Education':
        return 9853
    else:
        return 9991
    
user_input['Course'] = user_input['Course'].apply(encode_course)

# decode label
def decode_label(prediction):
    if prediction == 0:
        return "Enrolled"
    elif prediction == 1:
        return "Graduated"
    else:
        return "Dropout"

# show the result
if st.button("Predict", type="primary"):
    # make prediction
    predicted_status = model.predict(user_input)
    predicted_status = predicted_status[0]
    result = decode_label(predicted_status)

    # show the result
    if result == "Graduated":
        return st.success(f"Predicted status is: {result}", icon="🔥")
    elif result == "Dropout":
        return st.error(f"Predicted status is: {result}", icon="🚨")
    else:
        return st.info(f"Predicted status is: {result}")

