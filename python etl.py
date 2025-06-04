import pandas as pd
from pymongo import MongoClient

# Correct encoding to avoid UnicodeDecodeError
data = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')


if '_id' in data.columns:
    data = data.drop(columns=['_id'])

# Connect to MongoDB
mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient['demo']
collection = db['sales']

# Convert DataFrame to list of dicts and insert
jsondata = data.to_dict(orient='records')
collection.insert_many(jsondata)

print("✅ Data inserted successfully.")
