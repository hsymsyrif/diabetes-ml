# src/preprocessing.py
def prepare_features(df):
    X = df.drop("Diabetes_binary", axis=1)
    y = df["Diabetes_binary"]
    return X, y
