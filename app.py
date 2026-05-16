import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("placement_model.pkl", "rb"))

# Title
st.title("Student Placement Prediction System")

# Inputs
cgpa = st.number_input("Enter CGPA", 0.0, 10.0)
internships = st.number_input("Number of Internships", 0, 10)
projects = st.number_input("Number of Projects", 0, 20)
aptitude = st.number_input("Aptitude Score", 0, 100)

# Predict button
if st.button("Predict"):

    sample = pd.DataFrame(
        [[cgpa, internships, projects, aptitude]],
        columns=['CGPA', 'Internships', 'Projects', 'AptitudeTestScore']
    )

    prediction = model.predict(sample)

    if prediction[0] == "Placed":
        st.success("Student is likely to be Placed")
    else:
        st.error("Student is likely NOT to be Placed")