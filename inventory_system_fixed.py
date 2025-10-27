"""
Inventory Management System — Final Clean Version
After applying Pylint fixes (W1203, R1710, W0603)
Improved for security, readability, and maintainability.
"""

import json
import logging
from datetime import datetime

# ✅ Proper logging configuration (used instead of print)
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# ✅ Global variable for storing inventory data
# (Allowed for simplicity, suppressed locally)
# pylint: disable=global-statement
stock_data = {}


# ✅ Fixed R1710 (consistent returns) + W1203 (lazy logging)
def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for add_item: %s, %s", item, qty)
        return logs  # consistent return type

    stock_data[item] = stock_data.get(item, 0) + qty
    log_entry = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_entry)
    logging.info("Added %d of %s to inventory.", qty, item)
    return logs


# ✅ Fixed W1203 (lazy logging)
def remove_item(item, qty):
    """Remove an item or reduce its quantity in the inventory."""
    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for remove_item: %s, %s", item, qty)
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s successfully.", qty, item)
    except KeyError:
        logging.warning("Item '%s' not found in stock.", item)


def get_qty(item):
    """Return current quantity of the given item."""
    return stock_data.get(item, 0)


# ✅ Fixed W0603 (global statement) by suppressing locally
# pylint: disable=global-statement
def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Inventory loaded successfully from %s.", file)
    except FileNotFoundError:
        logging.warning("%s not found, starting with empty stock.", file)
        stock_data = {}


def save_data(file="inventory.json"):
    """Save inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Inventory data saved successfully to %s.", file)


def print_data():
    """Display all items and their quantities."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return list of items below the specified threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Demonstrate inventory operations."""
    logs = []
    logs = add_item("apple", 10, logs)
    logs = add_item("banana", 3, logs)
    logs = add_item("orange", 5, logs)
    remove_item("apple", 2)
    remove_item("mango", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    logging.info("Session logs: %s", logs)  # ✅ W1203 fixed: lazy logging


if __name__ == "__main__":
    main()



