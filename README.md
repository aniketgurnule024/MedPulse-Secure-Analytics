# MedPulse-Secure-Analytics
Secure, HIPAA-compliant cross-hospital predictive analytics platform powered by federated learning principles and designed for confidential computing environments on IBM Z / LinuxONE.

# 🛡️ FraudShield Enterprise: Real-Time AML & Transaction Monitoring

> **IBM Z Datathon (US Hub) Submission** | *Theme: Real-Time AI for Critical Decisions*

## 🚀 Overview
**FraudShield Enterprise** is a high-throughput, low-latency financial fraud detection and Anti-Money Laundering (AML) system. Designed for institutions processing millions of transactions per second, it utilizes unsupervised anomaly detection (Isolation Forest) combined with secure containerized pipelines to catch fraudulent transactions instantly while keeping sensitive data encrypted in transit and in memory.

## 🔑 Key Features
- **Sub-Millisecond Inference:** Rapid transaction scoring optimized for enterprise processor capabilities.
- **Unsupervised Anomaly Detection:** Dynamically flags complex synthetic fraud rings and irregular cash flow behaviors.
- **Live Monitoring Portal:** Interactive Streamlit dashboard tracking throughput (TPS), live risk flags, and anomaly clusters.

## 🛠️ Tech Stack
- **Machine Learning:** Scikit-Learn (Isolation Forest) / XGBoost
- **API & Streaming Simulator:** Python, FastAPI, Uvicorn
- **Dashboard UI:** Streamlit
- **Infrastructure:** Containerized architecture designed for high-performance deployment on IBM Z / LinuxONE.
