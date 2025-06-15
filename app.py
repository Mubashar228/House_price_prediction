import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("random_forest_model .pkl")

st.set_page_config(page_title="🏡 House Price Prediction", layout="centered")
st.title("🏡 House Price Prediction App")

st.markdown("### Enter the property details:")

# Input fields
location_id = st.number_input("Location ID", min_value=0, step=1)
property_type = st.number_input("Property Type (encoded)", min_value=0, step=1)
location = st.number_input("Location (encoded)", min_value=0, step=1)
city = st.number_input("City (encoded)", min_value=0, step=1)
province_name = st.number_input("Province (encoded)", min_value=0, step=1)
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")
baths = st.number_input("Number of Baths", min_value=0, step=1)
purpose = st.number_input("Purpose (encoded)", min_value=0, step=1)
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
area_type = st.number_input("Area Type (encoded)", min_value=0, step=1)
area_size = st.number_input("Area Size (in Marla/Kanal)", min_value=0.0, step=0.1)
area_category = st.number_input("Area Category (encoded)", min_value=0, step=1)

# Prediction button
if st.button("🔍 Predict House Price"):
    input_data = np.array([[location_id, property_type, location, city, province_name,
                            latitude, longitude, baths, purpose, bedrooms,
                            area_type, area_size, area_category]])
    try:
        prediction = model.predict(input_data)
        st.success(f"🏷 Estimated Price: {int(prediction[0]):,} PKR")
    except Exception as e:
        st.error(f"❌ Error in prediction: {e}")
