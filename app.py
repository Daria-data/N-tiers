from flask import Flask, request, jsonify, render_template, abort
from persistance import get_inventory, save_inventory, load_inventory
from model import (
    prod_is_available_enough,
    customer_purchased_product,
    customer_purchase_list,
    stock_report
)

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("welcome.html", page_class="welcome")

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.route("/inventory", methods=["GET"])
def get_inventory_route():
    inventory_data = get_inventory()
    return render_template("inventory.html", inventory_data=inventory_data)
   # return jsonify(get_inventory())

@app.route("/availability/<prod_name>/<int:quantity>", methods=["GET"])
def check_availability_route(prod_name, quantity):
    if not prod_name or quantity <= 0:
        abort(400)
    inventory = get_inventory()
    availability = prod_is_available_enough(prod_name, quantity, inventory)
    return render_template("availability.html", prod_name=prod_name, quantity=quantity, availability=availability)

@app.route("/purchase", methods=["POST"])
def purchase_item_route():
    data = request.get_json()
    if not data or "prod_name" not in data or "quantity" not in data:
        abort(400)
    prod_name = request.json["prod_name"]
    quantity = request.json["quantity"]
    if not prod_name or quantity <= 0:
        abort(400)
    inventory = get_inventory()
    try:
        updated_inventory = customer_purchased_product(prod_name, quantity, inventory)
        save_inventory(updated_inventory)
        return jsonify(updated_inventory)
    except ValueError as e:
        return str(e), 400

@app.route("/multi_purchase", methods=["POST"])
def multi_purchase_items_route():
    data = request.get_json()
    if not data or "order_list" not in data:
        abort(400)
    order_list = data["order_list"]
    if not order_list or not isinstance(order_list, list):
        abort(400)
    order_list = request.json["order_list"]
    inventory = get_inventory()
    try:
        updated_inventory = customer_purchase_list(order_list, inventory)
        save_inventory(updated_inventory)
        return jsonify(updated_inventory)
    except ValueError as e:
        return str(e), 400

@app.route("/report", methods=["GET"])
def get_report_route():
    inv = get_inventory()
    report = stock_report(inv)
    return render_template("report.html", inventory=inv, report=report)


if __name__ == "__main__":
    inventory = load_inventory()
    app.run(debug=True)
