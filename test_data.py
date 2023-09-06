from data import get_inventory

def test_get_inventory():
    inventory = get_inventory()
    assert isinstance(inventory, dict)
    assert "apple" in inventory
    assert "banana" in inventory