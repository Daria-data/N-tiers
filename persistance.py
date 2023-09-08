from typing import Dict
import json


def get_inventory() -> Dict[str, int]:
    inventory ={"apple": 50,
         "banana": 25,
         "orange": 33}
    return inventory

def save_inventory(inventory: Dict[str, int]):
    with open('inventory_data.json', 'w') as file:
        json.dump(inventory, file)

def load_inventory() -> Dict[str, int]:
    try:
        with open('inventory_data.json', 'r') as file:
            inventory = json.load(file)

    except FileNotFoundError:
        print("Inventory file not found.")
        inventory = {}
    return inventory



