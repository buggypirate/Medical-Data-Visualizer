import pandas as pd
import numpy as np

# Generate sample medical examination data
np.random.seed(42)
n_samples = 70000

data = {
    'age': np.random.randint(10000, 30000, n_samples),  # age in days
    'height': np.random.randint(140, 210, n_samples),  # height in cm
    'weight': np.random.uniform(40, 150, n_samples),  # weight in kg
    'gender': np.random.randint(1, 3, n_samples),  # gender categorical
    'ap_hi': np.random.randint(90, 200, n_samples),  # systolic BP
    'ap_lo': np.random.randint(60, 130, n_samples),  # diastolic BP
    'cholesterol': np.random.randint(1, 4, n_samples),  # 1=normal, 2=above, 3=well above
    'gluc': np.random.randint(1, 4, n_samples),  # 1=normal, 2=above, 3=well above
    'smoke': np.random.randint(0, 2, n_samples),  # binary
    'alco': np.random.randint(0, 2, n_samples),  # binary
    'active': np.random.randint(0, 2, n_samples),  # binary
    'cardio': np.random.randint(0, 2, n_samples),  # binary target
}

df = pd.DataFrame(data)

# Ensure diastolic <= systolic for some records
mask = df['ap_lo'] > df['ap_hi']
df.loc[mask, 'ap_lo'] = df.loc[mask, 'ap_hi'] - np.random.randint(10, 40, mask.sum())

# Save to CSV
df.to_csv('medical_examination.csv', index=False)
print("Sample medical_examination.csv created successfully!")
print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
