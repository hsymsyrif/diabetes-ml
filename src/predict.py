import joblib
import numpy as np
import pandas as pd

FEATURE_NAMES = [
    'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack',
    'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare',
    'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age',
    'Education', 'Income'
]

def load_model(path="model.pkl"):
    return joblib.load(path)

def predict_from_input(model, input_data: list):
    # Validasi panjang input
    if len(input_data) != len(FEATURE_NAMES):
        raise ValueError(f"Jumlah fitur tidak sesuai. Diperlukan {len(FEATURE_NAMES)}, tetapi diberikan {len(input_data)}.")

    # Validasi tipe angka
    try:
        input_data = [float(i) for i in input_data]
    except ValueError:
        raise ValueError("Semua input harus berupa angka.")

    input_df = pd.DataFrame([input_data], columns=FEATURE_NAMES)
    prediction = model.predict(input_df)
    return prediction[0]
