# Inventory Management System
## Introduction
The Inventory Management System is a web-based application built using Flask, a Python web framework. It allows users to manage and track product inventory, check product availability, make single or multiple purchases, and generate stock reports. This project serves as an educational endeavor to practically explore the concept of clean architecture and the organization of code into different n-tiers.

## Clean Architecture
Clean architecture, also known as a layered or n-tier architecture, is a software design model that organizes a computer system into multiple distinct levels or layers, each with a specific role in processing information. This architectural approach promotes separation of concerns and modularity, making the codebase more maintainable, testable, and adaptable.

In the context of this project, clean architecture separates the application into layers, such as presentation, business logic, and data access, allowing for flexibility and scalability. It helps ensure that each component has a clear responsibility and can be developed, tested, and modified independently.

## Features
View Inventory: Get a list of available products and their quantities.

Check Availability: Check if a specific product is available in the desired quantity.

Make a Purchase: Purchase a single product, and the inventory will be updated accordingly.

Multiple Purchases: Buy multiple products in a single request and manage your inventory efficiently.

Stock Reports: Generate stock reports to keep track of your inventory status.


## Usage
Access the application in your web browser at http://localhost:5000.
Navigate to /inventory to view the current inventory.

Use the /availability/<product_name>/<quantity> route to check product availability.

Make a purchase by sending a POST request to /purchase with a JSON body containing prod_name and quantity.

Perform multiple purchases by sending a POST request to /multi_purchase with a JSON body containing an order_list.

Access stock reports by visiting the /report route.

## Error Handling
The application includes error handling for 400 (Bad Request) errors and 404 (Not Found) errors to ensure that invalid requests are appropriately handled.

