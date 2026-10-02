from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"})


@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        category = category.lower()

        filtered_products = [
            product
            for product in products
            if product["category"].lower() == category
        ]

        return jsonify(filtered_products), 200

    return jsonify(products), 200

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)