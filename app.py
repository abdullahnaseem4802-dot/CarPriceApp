import streamlit as st
import joblib
import pandas as pd

# Load model + dropdown values
model = joblib.load("model.pkl")
dropdown_values = joblib.load("dropdown_values.pkl")

# Check what keys exist in dropdown_values
# st.write(dropdown_values.keys())
st.title("🚗 Used Car Price Prediction App")


# --- Dropdown Inputs ---# Manufacturer dropdown
manufacturer = st.selectbox("Select Manufacturer", dropdown_values["manufacturer"])

# Define models per manufacturer
models_dict = {
    "acura": ["MDX", "RDX", "TLX"],
    "audi": ["A4", "Q7", "A6"],
    "bmw": ["X5", "X3", "320i"],
    "ford": ["Figo", "Mustang"],
    "chevrolet": ["Cruze", "Malibu", "Impala"],
    "honda": ["Civic", "Accord", "CR-V"],
    "toyota": ["Corolla", "Camry", "RAV4"]
}


# Model dropdown updates based on selected manufacturer
model_name = st.selectbox("Select Model", models_dict.get(manufacturer, []))

condition = st.selectbox("Select Condition", dropdown_values["condition"])
cylinders = st.selectbox("Select Cylinders", dropdown_values["cylinders"])
fuel = st.selectbox("Select Fuel Type", dropdown_values["fuel"])
title_status = st.selectbox("Select Title Status", dropdown_values["title_status"])
transmission = st.selectbox("Select Transmission", dropdown_values["transmission"])
drive = st.selectbox("Select Drive Type", dropdown_values["drive"])
size = st.selectbox("Select Size", dropdown_values["size"])
car_type = st.selectbox("Select Car Type", dropdown_values["type"])
paint_color = st.selectbox("Select Paint Color", dropdown_values["paint_color"])
state = st.selectbox("Select State", dropdown_values["state"])
region = st.selectbox("Select Region", dropdown_values["region"])

# --- Numeric Inputs ---
year = st.number_input("Year", min_value=1900, max_value=2025, step=1)
odometer = st.number_input("Odometer (miles)", min_value=0, max_value=1000000, step=500)

# --- Predict Button ---
if st.button("Predict Price"):
    # Create dataframe for prediction
    input_data = pd.DataFrame([{
        "year": year,
        "odometer": odometer,
        "manufacturer": manufacturer,
        "model": model_name,
        "condition": condition,
        "cylinders": cylinders,
        "fuel": fuel,
        "title_status": title_status,
        "transmission": transmission,
        "drive": drive,
        "size": size,
        "type": car_type,
        "paint_color": paint_color,
        "state": state,
        "region": region
    }])

    # One-hot encode to match training
    input_encoded = pd.get_dummies(input_data)
    model_features = model.feature_names_in_

    # Align columns with training features
    input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0]
    st.success(f"💰 Estimated Car Price: ${prediction:,.2f}")
