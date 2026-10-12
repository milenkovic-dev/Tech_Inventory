import json

with open('products.json') as file:
    products = json.load(file)
    print(products)



