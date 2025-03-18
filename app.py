import streamlit as st
import joblib

# Load the trained model
model = joblib.load('final_svm_model.pkl')

st.title("🌸 Iris Flower Classification 🌸")  # Modify the heading

# st.header("Predict the species of an Iris flower")  # Modify the subheading
# Smaller subheading using Markdown
st.markdown("<h3 style='text-align: center;'>Predict the species of an Iris flower</h3>", unsafe_allow_html=True)

# Add author name
st.markdown("<h5 style='text-align: center; color: grey;'>By Priyanshi Negi</h5>", unsafe_allow_html=True)

st.write("Enter the flower details:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)")
sepal_width = st.number_input("Sepal Width (cm)")
petal_length = st.number_input("Petal Length (cm)")
petal_width = st.number_input("Petal Width (cm)")

# Predict button
if st.button("Predict"):
    prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    st.write(f"Predicted Flower Class: {prediction[0]}")
