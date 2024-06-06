# Kebab Shop Project

This project is a simple web application for managing kebab orders. It uses Flask as the web framework and SQLAlchemy for database interactions.

## Features

- View products
- View orders
- Add new orders
- Delete existing orders

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/ElijusButnorius/kebab.git
   cd YourRepository

2. Create a virtual environment:

    python -m venv venv

3. Activate the virtual environment:

    venv\Scripts\activate

4. Install the dependencies:

    pip install -r requirements.txt

# Usage

## Run the applications:

  1. Python init_db.py
  2. Python main_db.py

## Project Structure

- main.py: The main application file containing routes and models.
- ini_db.py: Script to initialize the database with initial data.
- templates/: Contains HTML templates for rendering pages.
- static/: Contains static files like CSS.
- database/: Contains the SQLite database file.

## Routes

- /: Home page
- /products: View all products
- /orders: View all orders
- /add_order: Add a new order
- /delete_order/<order_id>: Delete an order by ID

## Dependencies

- Flask
- Flask-SQLAlchemy