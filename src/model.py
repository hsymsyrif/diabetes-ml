import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MODEL_PATH = "model/diabetes_model.pkl"
DATA_PATH = "data/diabetes.csv"

def train_model_if_needed():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    print("Training model...")

    df = pd.read_csv(DATA_PATH)

    X = df.drop("Diabetes_012", axis=1)
    y = df["Diabetes_012"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print(f"Model trained and saved to '{MODEL_PATH}'")
    print(f"Accuracy on test set: {accuracy_score(y_test, model.predict(X_test)):.2f}")

    return model
