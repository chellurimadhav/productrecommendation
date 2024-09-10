# backend.py
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

CSV_FILE_PATH = 'models/clean_data.csv'

@app.route('/api/products', methods=['GET'])
def get_products():
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Select the first 10 products
    df = df.head(10)
    
    # Convert data to a dictionary format for JSON response
    products = []
    for index, row in df.iterrows():
        product = {
            'image': row['ImageURL'],
            'name': row['Name'],
            'brand': row['Brand'],
            'rating': row['Rating'],
            'reviewCount': row['ReviewCount']
        }
        products.append(product)
    
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
