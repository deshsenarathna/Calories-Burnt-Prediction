import streamlit as st
import joblib
import numpy as np

model = joblib.load("calories_model.pkl")

st.set_page_config(
    page_title="Calories Predictor",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 Calories Burnt Prediction")
st.markdown("Enter your details and get an instant calorie burn estimate.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
        weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=70)

    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
        heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=90)
        body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0, value=37.0)

    submitted = st.form_submit_button("Predict Calories", use_container_width=True)

if submitted:
    gender_val = 0 if gender == "Male" else 1
    bmi = weight / ((height / 100) ** 2)
    age_duration = age * duration
    weight_duration = weight * duration

    features = np.array([[
        gender_val,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp,
        bmi,
        age_duration,
        weight_duration
    ]])

    prediction = model.predict(features)[0]

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.success(f"Estimated Calories Burnt: {prediction:.2f}")

    with result_col2:
        st.info(f"BMI: {bmi:.2f}")