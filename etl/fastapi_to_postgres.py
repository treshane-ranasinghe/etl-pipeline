import requests
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Fetch data from FastAPI
def extract_data(api_url: str) -> pd.DataFrame:
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return pd.DataFrame(data)

# Step 2: (Optional) Transform data
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # You can clean or transform here if needed
    return df

# Step 3: Load into PostgreSQL warehouse
def load_to_postgres(df: pd.DataFrame, db_url: str, table_name: str):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"Loaded {len(df)} records into {table_name}.")

# Main pipeline function
def run_pipeline():
    # Source API (FastAPI)
    api_url = "http://127.0.0.1:8000/posts/"
    
    # Target PostgreSQL (Data Warehouse)
    db_url = "postgresql://treshaneranasinghe:Dahami224466@localhost:5432/warehouse_db"
    table_name = "posts"

    print("Extracting data...")
    df = extract_data(api_url)
    
    print("Transforming data...")
    df = transform_data(df)
    
    print("Loading data into warehouse...")
    load_to_postgres(df, db_url, table_name)

if __name__ == "__main__":
    run_pipeline()
