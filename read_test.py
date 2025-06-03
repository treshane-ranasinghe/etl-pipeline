import pandas as pd

# Try reading with ISO-8859-1 encoding
data = pd.read_csv('sales_data_sample.csv', encoding='ISO-8859-1')
print(data.head())
