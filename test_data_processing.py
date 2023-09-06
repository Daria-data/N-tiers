from data_processing import (
    prod_is_available_enough,
    customer_purchased_product,
    customer_purchase_list,
    stock_report
)
import pytest

def test_product_is_available_enough():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    assert prod_is_available_enough("apple", 10, inventory_test) == True
    assert prod_is_available_enough("apple", 80, inventory_test) == False
    assert prod_is_available_enough("poulet", 1, inventory_test) == False

def test_customer_purchased_product():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    remaining_quantity = customer_purchased_product("apple", 20, inventory_test)
    assert remaining_quantity["apple"] == 30

def test_customer_purchase_list():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    order_list = [("apple", 20), ("banana", 1)]
    updated_inventory = customer_purchase_list(order_list, inventory_test)
    assert updated_inventory["apple"] == 30
    assert updated_inventory["banana"] == 24

def test_stock_report():
    inventory_test = {"apple": 50, "banana": 25, "orange": 33}
    expected_report = "Stock Report:\nProduct: apple, Quantity: 50\nProduct: banana, Quantity: 25\nProduct: orange, Quantity: 33\n"
    assert stock_report(inventory_test) == expected_report
