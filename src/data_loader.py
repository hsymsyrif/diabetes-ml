# src/data_loader.py
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
