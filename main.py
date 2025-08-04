import os
from src.model import train_model_if_needed
from src.predict import predict_from_input
from src.utils import get_user_inputs, calculate_bmi

def main():
    print("Welcome to Diabetes Prediction CLI App!\n")

    # Load or train model
    model = train_model_if_needed()

    # Get user input
    user_data = get_user_inputs()

    # Calculate BMI
    bmi = calculate_bmi(user_data["weight_kg"], user_data["height_cm"])
    user_data["BMI"] = bmi

    print(f"\nYour calculated BMI: {bmi:.2f}")

    # Run prediction
    result = predict_from_input(model, user_data)

    print("\nPrediction Result:")
    if result == 1:
        print("High chance of having diabetes. Please consult a doctor.")
    else:
        print("Low chance of having diabetes. Keep maintaining a healthy lifestyle!")

if __name__ == "__main__":
    main()
