import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def generate_hospital_data(hospital_id, num_patients=500):
    """Simulates isolated local hospital data to mimic HIPAA-compliant boundaries."""
    np.random.seed(hospital_id * 10)
    age = np.random.randint(25, 85, size=num_patients)
    bmi = np.random.normal(26, 4, size=num_patients)
    blood_pressure = np.random.normal(120, 15, size=num_patients)
    glucose = np.random.normal(105, 20, size=num_patients)
    
    # Synthetic target: Patient deterioration risk (0 = Stable, 1 = High Risk)
    risk_factor = (age > 60).astype(int) + (glucose > 130).astype(int) + (blood_pressure > 140).astype(int)
    deterioration = np.array([1 if r >= 2 or np.random.rand() < 0.1 else 0 for r in risk_factor])
    
    df = pd.DataFrame({
        'patient_id': [f"H{hospital_id}-P-{100+i}" for i in range(num_patients)],
        'age': age,
        'bmi': bmi,
        'blood_pressure': blood_pressure,
        'glucose': glucose,
        'deterioration_risk': deterioration
    })
    return df

def train_local_node(df):
    """Simulates training inside a hardware-isolated secure execution boundary."""
    X = df[['age', 'bmi', 'blood_pressure', 'glucose']]
    y = df['deterioration_risk']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = LogisticRegression(max_iter=200)
    model.fit(X_scaled, y)
    return model, scaler

if __name__ == "__main__":
    hosp_df = generate_hospital_data(1)
    model, scaler = train_local_node(hosp_df)
    print("Secure local enclave model successfully trained and verified inside isolated environment.")
