import sqlite3
import json
from pathlib import Path

products = json.loads(Path("eccomerce/products.json").read_text())
# print(products)

