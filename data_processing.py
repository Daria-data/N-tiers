from typing import Dict, List, Tuple


def prod_is_available_enough(prod_name: str, quantity: int, inventory: Dict[str, int]) -> bool:
    try:
        if prod_name in inventory and inventory[prod_name] >= quantity:
            return True
        else:
            return False
    except Exception as e:
        raise e

def customer_purchased_product(prod_name: str, quantity: int, inventory: Dict[str, int]) -> Dict[str, int]:
    try:

        if prod_is_available_enough(prod_name, quantity, inventory):
            inventory[prod_name] -= quantity
        else:
            raise ValueError(
                "Your order product-quantity is greater than the quantity in stock. It cannot be validated"
        )
        return inventory
    except Exception as e:
        raise e

def customer_purchase_list(
    order_list: List[Tuple[str, int]], inventory: Dict[str, int]
) -> Dict[str, int]:
    for prod_name, quantity in order_list:
        if prod_is_available_enough(prod_name, quantity, inventory):
            inventory[prod_name] -= quantity
        else :
            raise ValueError(f"Product '{prod_name}' not available in sufficient quantity")
    return inventory


def stock_report(inv: Dict[str, int]) -> str:
    report_str = "Stock Report:\n"
    for k, v in inv.items():
        report_str += f"Product: {k}, Quantity: {v}\n"
    return report_str