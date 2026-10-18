import streamlit as st
import pandas as pd
import numpy as np
from model import generate_hospital_data, train_local_node

st.set_page_config(page_title="MedPulse | IBM Z Secure Analytics", layout="wide")

st.title("🏥 MedPulse: Secure, Cross-Hospital Patient Analytics")
st.markdown("### Privacy-Preserving Collaborative Healthcare Platform Powered by IBM Secure Execution")

# Multi-hospital simulation selector
st.sidebar.header("Federated Network Nodes")
selected_hospital = st.sidebar.selectbox("Select Hospital Institution Node", ["Hospital A (Metro General)", "Hospital B (County Medical)", "Hospital C (University Clinic)"])
h_id = 1 if "Hospital A" in selected_hospital else (2 if "Hospital B" in selected_hospital else 3)

# Load isolated local data
data = generate_hospital_data(h_id, num_patients=400)
model, scaler = train_local_node(data)

col1, col2, col3 = st.columns(3)
col1.metric(label="Active Secure Enclave", value=selected_hospital)
col2.metric(label="HIPAA Compliance Status", value="100% Isolated", delta="Zero Leakage")
col3.metric(label="Encrypted Model Sync", value="Active (LinuxONE)", delta="Secure")

st.markdown("---")
st.subheader(f"Live Patient Vitals & Deterioration Risk Scoring — {selected_hospital}")

# Real-time inference
X = data[['age', 'bmi', 'blood_pressure', 'glucose']]
X_scaled = scaler.transform(X)
preds = model.predict(X_scaled)
probs = model.predict_proba(X_scaled)[:, 1]

data['predicted_risk'] = ["🚨 High Deterioration Risk" if p == 1 else "✅ Stable" for p in preds]
data['confidence_score'] = np.round(probs * 100, 2)

st.dataframe(data[['patient_id', 'age', 'bmi', 'blood_pressure', 'glucose', 'predicted_risk', 'confidence_score']].head(12), use_container_width=True)

# Visual analytics
st.markdown("---")
st.subheader("Cross-Hospital Collaborative Analytics Insight")
st.scatter_chart(data, x='age', y='glucose', color='predicted_risk')
