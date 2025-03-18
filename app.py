import streamlit as st
import joblib

# Load the trained model
model = joblib.load('final_svm_model.pkl')

# Define class labels
class_labels = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}

# Centered Title
st.markdown("<h2 style='text-align: center;'>🌸 Iris Flower Classification 🌸</h2>", unsafe_allow_html=True)

# Subheading
st.markdown("<h4 style='text-align: center;'>Predict the species of an Iris flower</h4>", unsafe_allow_html=True)

# Author Name
st.markdown("<p style='text-align: center; font-size: 14px; color: grey;'>By Priyanshi Negi</p>", unsafe_allow_html=True)

st.write("### Enter the flower details:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)")
sepal_width = st.number_input("Sepal Width (cm)")
petal_length = st.number_input("Petal Length (cm)")
petal_width = st.number_input("Petal Width (cm)")

# Predict button
if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    flower_name = class_labels[prediction]  # Map number to class name
    st.success(f"🌼 Predicted Flower Class: **{flower_name}** ({prediction})")
