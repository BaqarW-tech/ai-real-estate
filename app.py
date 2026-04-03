import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the brain
model = pickle.load(open('jeddah_model.pkl', 'rb'))
district_map = pickle.load(open('districts.pkl', 'rb'))

st.set_page_config(page_title="JeddahVision AI", page_icon="🇸🇦")

st.title("🇸🇦 Jeddah Real Estate AI Valuation")
st.markdown("This tool uses AI to estimate property values in Jeddah, helping investors align with **Vision 2030** goals.")

# Sidebar
st.sidebar.header("Property Details")
dist_name = st.sidebar.selectbox("Select District", list(district_map.values()))
area = st.sidebar.number_input("Area (Sqm)", value=250)
dist_corniche = st.sidebar.slider("Distance to Corniche (KM)", 0.0, 20.0, 5.0)

# Prediction Logic
dist_code = [k for k, v in district_map.items() if v == dist_name][0]
input_array = np.array([[dist_code, area, dist_corniche]])
prediction = model.predict(input_array)[0]

# Display Result
st.subheader(f"Estimated Price: {prediction:,.0f} SAR")

col1, col2 = st.columns(2)
with col1:
    st.write(f"**District:** {dist_name}")
    st.write(f"**Price per sqm:** {prediction/area:,.2f} SAR")
with col2:
    if dist_corniche < 2:
        st.success("🔥 High Demand: Close to Waterfront Projects.")
    else:
        st.info("Stable Residential Area.")

# Simple Map for Jeddah
st.map(pd.DataFrame({'lat': [21.5433], 'lon': [39.1728]}))
