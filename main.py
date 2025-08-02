import joblib
import os
from src.model import train_model
from src.predict import predict_from_input

def main():
    # Train or Load model
    model_path = "model/diabetes_model.pkl"
    if not os.path.exists(model_path):
        print("📦 Model not found, training...")
        model, feature_names = train_model()
    else:
        print("📥 Loading saved model...")
        model = joblib.load(model_path)
        # Feature names harus disimpan manual saat ini (atau bisa pakai joblib dump tuple)
        # Sementara kita panggil train_model agar dapet feature_names
        _, feature_names = train_model()

    # Contoh input user
    input_data = {
        "HighBP": 1,
        "HighChol": 1,
        "CholCheck": 1,
        "BMI": 30.0,   # atau gunakan Weight & Height di bawah
        # "Height": 170,
        # "Weight": 75,
        "Smoker": 0,
        "Stroke": 0,
        "HeartDiseaseorAttack": 0,
        "PhysActivity": 1,
        "Fruits": 1,
        "Veggies": 1,
        "HvyAlcoholConsump": 0,
        "AnyHealthcare": 1,
        "NoDocbcCost": 0,
        "GenHlth": 3,
        "MentHlth": 5,
        "PhysHlth": 3,
        "DiffWalk": 0,
        "Sex": 1,
        "Age": 9,
        "Education": 4,
        "Income": 5
    }

    result = predict_from_input(model, input_data, feature_names)
    print("🧪 Prediksi Diabetes:", "POSITIF" if result == 1 else "NEGATIF")

if __name__ == "__main__":
    main()
