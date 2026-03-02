# Building Cooling Load Prediction System

## Overview

This project presents a machine learning–based system for predicting building cooling energy demand using architectural design parameters. The model is trained on the UCI Energy Efficiency dataset and deployed using Streamlit as an interactive web application.

The objective of this project is to demonstrate an end-to-end machine learning workflow, including data preprocessing, regression modeling, performance evaluation, model serialization, and deployment.

---

## Problem Statement

During the building design phase, architects and engineers must estimate the expected cooling energy demand to:

- Optimize HVAC system sizing
- Reduce long-term energy costs
- Improve sustainability and energy efficiency
- Support green building certifications

This project predicts **Cooling Load** based on structural and geometric building features.

---

## Dataset

The model is trained using the **Energy Efficiency Dataset** from the UCI Machine Learning Repository.

The dataset contains simulated building configurations with the following features:

- Relative Compactness  
- Surface Area  
- Wall Area  
- Roof Area  
- Overall Height  
- Orientation  
- Glazing Area  
- Glazing Area Distribution  

Target Variables:
- Heating Load
- Cooling Load (used in this project)

---

## Methodology

### 1. Data Preprocessing
- Column renaming for clarity
- Feature-target separation
- Train-test split

### 2. Model Selection
- Random Forest Regressor
- Evaluation using:
  - Mean Absolute Error (MAE)
  - R² Score

Model Performance:
- R² ≈ 0.96 (approximate, may vary slightly)

### 3. Anomaly Detection Layer
A simple residual-based anomaly detection mechanism compares:

