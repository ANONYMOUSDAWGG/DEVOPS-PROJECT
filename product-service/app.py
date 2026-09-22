from flask import Flask, jsonify, abort

app = Flask(__name__)

PRODUCTS = {
    101: {"id": 101, "name": "Wireless Mouse", "price": 599},
    102: {"id": 102, "name": "Mechanical Keyboard", "price": 2499},
    103: {"id": 103, "name": "USB-C Hub", "price": 1299},
}


@app.route("/")
def home():
    return jsonify(service="product-service", status="running")


@app.route("/health")
def health():
    return jsonify(status="UP"), 200


@app.route("/products")
def get_products():
    return jsonify(list(PRODUCTS.values()))


@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        abort(404, description="Product not found")
    return jsonify(product)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
