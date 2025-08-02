import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train_model(data_path="data/diabetes.csv"):
    # Load data
    df = pd.read_csv(data_path)

    # Hitung BMI jika tidak ada
    if 'BMI' not in df.columns and 'Weight' in df.columns and 'Height' in df.columns:
        df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)

    # Drop kolom yang tidak diperlukan
    drop_cols = ['Weight', 'Height']
    for col in drop_cols:
        if col in df.columns:
            df.drop(columns=col, inplace=True)

    # Pastikan target kolom
    target = 'Diabetes_binary'
    X = df.drop(columns=[target])
    y = df[target]

    # Split & train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Eval
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/diabetes_model.pkl")
    print("✅ Model saved to model/diabetes_model.pkl")

    return model, X.columns.tolist()
