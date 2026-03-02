import streamlit as st
import joblib
import numpy as np

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="Cooling Efficiency Monitor",
    layout="wide",
)

# ----------------------------------
# Custom Styling
# ----------------------------------

st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 700;
        color: #0E4D92;
    }
    .subtitle {
        font-size: 18px;
        color: #555555;
    }
    .metric-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #F0F6FF;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------
# Header Section
# ----------------------------------

st.markdown('<div class="main-title">Industrial Cooling Water Efficiency System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-Based Cooling Demand Prediction & Anomaly Detection</div>', unsafe_allow_html=True)

st.markdown("---")

# Optional: Add image (place image in project folder first)
st.image("images.jpg", use_column_width=True)

# ----------------------------------
# Load Model
# ----------------------------------

model = joblib.load("water_efficiency_model.pkl")
feature_names = joblib.load("model_feature.pkl")

# ----------------------------------
# Sidebar Inputs
# ----------------------------------

st.sidebar.header("System Parameters")

Relative_Compactness = st.sidebar.number_input("Relative Compactness", value=0.8)
Surface_Area = st.sidebar.number_input("Surface Area", value=700.0)
Wall_Area = st.sidebar.number_input("Wall Area", value=300.0)
Roof_Area = st.sidebar.number_input("Roof Area", value=150.0)
Overall_Height = st.sidebar.number_input("Overall Height", value=3.5)
Orientation = st.sidebar.number_input("Orientation", value=2)
Glazing_Area = st.sidebar.number_input("Glazing Area", value=0.2)
Glazing_Distribution = st.sidebar.number_input("Glazing Distribution", value=3)

# ----------------------------------
# Main Prediction Section
# ----------------------------------

if st.button("Predict Cooling Demand"):

    input_data = np.array([[
        Relative_Compactness,
        Surface_Area,
        Wall_Area,
        Roof_Area,
        Overall_Height,
        Orientation,
        Glazing_Area,
        Glazing_Distribution
    ]])

    prediction = model.predict(input_data)[0]

    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.metric("Predicted Cooling Demand", f"{prediction:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Anomaly Detection")

    THRESHOLD = 5  # Adjust based on your residual analysis

    actual_value = st.number_input(
        "Enter Observed Cooling Demand",
        value=float(prediction)
    )

    residual = abs(actual_value - prediction)

    if residual > THRESHOLD:
        st.error("Abnormal Cooling Demand Detected")
        st.info("Suggested Action: Inspect cooling system for possible leakage or inefficiency.")
    else:
        st.success("Cooling System Operating Within Expected Range")
