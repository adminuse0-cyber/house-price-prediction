import streamlit as st
import pickle
import numpy as np

# Load Trained Model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏡 House Price Prediction App")
st.write("Enter house details to estimate price:")

sqft = st.number_input("Square Feet (SqFt)", min_value=300, max_value=10000, value=1000)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])

if st.button("Predict Price"):
    features = np.array([[sqft, bedrooms, bathrooms]])
    price_in_inr = prediction[0] * 83  
    st.success(f"Estimated House Price: ₹{price_in_inr:,.2f}")
