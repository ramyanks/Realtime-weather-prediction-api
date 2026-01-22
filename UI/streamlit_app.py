import streamlit as st
import requests

# st.title("Hello Streamlit 🚀")
# st.write("Streamlit is working!")

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Realtime weather prediction", layout="centered")

st.title("Realtime weather prediction")
st.write("Enter details to predict temperature:")

# -------------------------
# Input fields
# -------------------------
humidity = st.number_input("humidity", min_value=1, max_value=100, value=1)
wind_speed = st.number_input("wind_speed", min_value=1, max_value=50, value=1)
meanpressure = st.number_input("meanpressure", min_value=1, max_value=2000, value=1)


# -------------------------
# Predict button
# -------------------------
if st.button("Predict"):
    payload = {
        "humidity": humidity,
        "wind_speed": wind_speed,
        "meanpressure": meanpressure
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction Result")
            st.success(f"Mean temperature: **{result['predicted_value']}**")
        else:
            st.error(f"API Error: {response.status_code}")
            st.json(response.json())

    except Exception as e:
        st.error(f"Connection error: {e}")
