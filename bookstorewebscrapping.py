import requests
import pandas as pd

url = "https://fakestoreapi.com/products"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

print(df.head())
df.to_csv('products.csv', index=False)
