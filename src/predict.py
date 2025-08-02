import numpy as np
import pandas as pd

def predict_from_input(model, input_data_dict, feature_names):
    # Hitung BMI jika Height dan Weight ada
    if 'BMI' not in input_data_dict and 'Weight' in input_data_dict and 'Height' in input_data_dict:
        height = input_data_dict.pop('Height')
        weight = input_data_dict.pop('Weight')
        input_data_dict['BMI'] = weight / ((height / 100) ** 2)

    # Konversi ke DataFrame agar sesuai urutan feature
    input_df = pd.DataFrame([input_data_dict], columns=feature_names)

    prediction = model.predict(input_df)
    return prediction[0]
