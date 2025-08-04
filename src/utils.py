def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = float(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Value must be at least {min_val}")
                continue
            if max_val is not None and val > max_val:
                print(f"Value must not exceed {max_val}")
                continue
            return val
        except ValueError:
            print("Please enter a valid number.")

def get_user_inputs():
    print("📝 Please answer the following health-related questions:\n")

    return {
        "HighBP": int(input("Do you have high blood pressure? (1 = Yes, 0 = No): ")),
        "HighChol": int(input("Do you have high cholesterol? (1 = Yes, 0 = No): ")),
        "CholCheck": int(input("Have you had a cholesterol check in the past 5 years? (1 = Yes, 0 = No): ")),
        "BMI": 0.0,  # Placeholder, will be calculated
        "Smoker": int(input("Have you smoked at least 100 cigarettes in your life? (1 = Yes, 0 = No): ")),
        "Stroke": int(input("Have you ever had a stroke? (1 = Yes, 0 = No): ")),
        "HeartDiseaseorAttack": int(input("Do you have heart disease or ever had a heart attack? (1 = Yes, 0 = No): ")),
        "PhysActivity": int(input("Do you do any physical activity during a typical week? (1 = Yes, 0 = No): ")),
        "Fruits": int(input("Do you consume fruit at least once per day? (1 = Yes, 0 = No): ")),
        "Veggies": int(input("Do you eat vegetables at least once per day? (1 = Yes, 0 = No): ")),
        "HvyAlcoholConsump": int(input("Do you drink heavily? (1 = Yes, 0 = No): ")),
        "AnyHealthcare": int(input("Do you have any kind of health coverage? (1 = Yes, 0 = No): ")),
        "NoDocbcCost": int(input("Was there a time in the past 12 months you couldn't see a doctor due to cost? (1 = Yes, 0 = No): ")),
        "GenHlth": get_float_input("How do you rate your general health? (1 = Excellent to 5 = Poor): ", 1, 5),
        "MentHlth": get_float_input("How many days during the past 30 was your mental health not good?: ", 0, 30),
        "PhysHlth": get_float_input("How many days during the past 30 was your physical health not good?: ", 0, 30),
        "DiffWalk": int(input("Do you have serious difficulty walking or climbing stairs? (1 = Yes, 0 = No): ")),
        "Sex": int(input("Sex (1 = Male, 0 = Female): ")),
        "Age": get_float_input("Your age in years: ", 1, 120),
        "Education": get_float_input("Your education level (1 = Never attended school, 6 = College graduate): ", 1, 6),
        "Income": get_float_input("Your income level (1 = Low, 8 = High): ", 1, 8),
        "height_cm": get_float_input("Your height in centimeters: ", 50, 250),
        "weight_kg": get_float_input("Your weight in kilograms: ", 10, 300),
    }

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)
