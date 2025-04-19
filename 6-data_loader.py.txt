import pandas as pd

def load_csv_data(filepath):
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")
        return pd.DataFrame()
