import pandas as pd

def ingest_data():
    data = pd.read_csv('data/raw/dataset.csv')
    data = data.dropna()  # Remove missing values
    data.to_csv('data/processed/processed_dataset.csv', index=False)
    print("Data Ingestion Complete")