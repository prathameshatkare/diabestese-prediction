# importing Important Libraries
import pickle
import streamlit as st

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Split Columns
col1, col2 = st.columns(2)

# Input fields with validation
# Input fields with validation
with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1)
with col2:
    insulin = st.number_input('Insulin', min_value=0, max_value=1000, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=60.0, step=0.1)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01)
    age = st.number_input('Age', min_value=0, max_value=120, step=1)

# Prediction
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
    if pregnancies == 0 or glucose == 0 or blood_pressure == 0 or skin_thickness == 0 or insulin == 0 or bmi == 0.0 or diabetes_pedigree_function == 0.0 or age == 0:
        st.warning("Please fill in all the fields.")
    else:
        diabetes_prediction = model_diabetes.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The patient has diabetes'
        else:
            diabetes_diagnosis = 'The patient does not have diabetes'

        st.success(diabetes_diagnosis)
