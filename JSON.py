from importlib.resources import path
from itertools import product
import json

from pathlib import Path

product = [
    {"product":"T-Shirt", "Price": 5.99, "Stock Availability": 15},
    {"product":"T-Bag", "Price": 15.99, "Stock Availability": 8},
    {"product":"Jeans", "Price": 10.99, "Stock Availability": 3},
    {"product":"Book", "Price": 7.99, "Stock Availability": 10},

]

products_data = json.dumps(product)
# print(products_data)

#writing the above data to a json file
Path("eccomerce/products.json").write_text(products_data)

# Reading from json data 
json_data = Path("eccomerce/products.json").read_text()
read_able = json.loads(json_data)
print(read_able)
print(read_able[0])
print(read_able[0]['Price'])

