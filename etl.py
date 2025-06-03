import pandas as pd 
from pymongo import MongoClient

data = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')


mongoClient = MongoClient('mongodb://localhost:27017/') 
 
db = mongoClient['demo'] 
collection = db['sales']

jsondata = data.to_dict(orient='records')
collection.insert_many(jsondata)
