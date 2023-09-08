from persistance import get_inventory, save_inventory, load_inventory
import os
import json
import pytest


@pytest.fixture
def temporary_inventory_file():
    filename = 'inventory_data.json'
    yield filename
#    if os.path.exists(filename):
#        os.remove(filename)
#    print("Temporary file removed:", not os.path.exists(filename))

def test_get_inventory():
    inventory = get_inventory()
    assert isinstance(inventory, dict)
    assert "apple" in inventory
    assert "banana" in inventory

def test_save_inventory(temporary_inventory_file):
    inventory = {"apple": 50, "banana": 25, "orange": 33}
    save_inventory(inventory)
    print("Current working directory:", os.getcwd())

    with open(temporary_inventory_file, 'r') as file:
        file_contents = file.read()
        print("File contents:", file_contents)

    assert os.path.exists(temporary_inventory_file)

    with open(temporary_inventory_file, 'r') as file:
        saved_inventory = json.load(file)
    assert saved_inventory == inventory

