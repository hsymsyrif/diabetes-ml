import numpy as np

def predict_from_input(model, input_data):
    # Prepare feature list in correct order
    features = [
        "HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke",
        "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies",
        "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth",
        "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"
    ]
    
    input_array = np.array([[input_data[feature] for feature in features]])
    prediction = model.predict(input_array)
    return prediction[0]
