# Cafe simulation

# Define the menu items and their respective prices
menu = {
    'coffee': 2.50,
    'sandwich': 5.75,
    'cake': 3.25,
    'tea': 2.00
}

# Define the stock of each item
stock = {
    'coffee': 100,
    'sandwich': 50,
    'cake': 75,
    'tea': 120
}

# Calculate the total stock worth
total_stock_worth = 0.0
for item in menu:
    item_value = stock[item] * menu[item]
    total_stock_worth += item_value

# Print the total stock worth
print(f"The total stock worth in the cafe is: ${total_stock_worth:.2f}")
