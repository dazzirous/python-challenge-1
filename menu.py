# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            menu_options = menu[menu_category_name]

            # Loop through menu options and display
            for index, (item_name, item_price) in enumerate(menu_options.items(), start=1):
                if isinstance(item_price, dict):
                    for variant, variant_price in item_price.items():
                        print(f"{index}.{variant} - {item_name}: ${variant_price}")
                else:
                    print(f"{index}. {item_name}: ${item_price}")

            # Ask the customer to input the menu item number
            menu_item_number = input("Enter the item number: ")

            # Check if the customer's input is a number
            if menu_item_number.isdigit():
                menu_item_number = int(menu_item_number)
                if 1 <= menu_item_number <= len(menu_options):
                    # Get the selected menu item
                    selected_item_name, selected_item_price = list(menu_options.items())[menu_item_number - 1]
                    if isinstance(selected_item_price, dict):
                        # If the selected item has variants, ask for the variant
                        print("Available variants:")
                        for variant, variant_price in selected_item_price.items():
                            print(f"{variant}: ${variant_price}")
                        selected_variant = input("Select a variant: ")
                        if selected_variant in selected_item_price:
                            selected_variant_price = selected_item_price[selected_variant]
                            selected_item_name = f"{selected_variant} {selected_item_name}"
                            selected_item_price = selected_variant_price
                        else:
                            print("Invalid variant selection. Defaulting to the base item.")
                    # Ask the customer for the quantity of the menu item
                    quantity = input("Enter quantity: ")
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    # Add the item name, price, and quantity to the order list
                    order_list.append({"Item": selected_item_name, "Price": selected_item_price, "Quantity": quantity})
                    print(f"{quantity} {selected_item_name}(s) added to your order.")
                else:
                    print("Invalid item number.")
            else:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid menu number.")
    else:
        print("Invalid input. Please enter a number.")

    # Ask the customer if they would like to keep ordering
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ")
    if keep_ordering.lower() != 'y':
        place_order = False

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order and print details
for order_item in order_list:
    item_name = order_item["Item"]
    price = order_item["Price"]
    quantity = order_item["Quantity"]

    # Calculate the total price for this item
    total_price = price * quantity

    # Print the item name, price, and quantity
    print(f"{item_name.ljust(26)}| ${price:.2f}  | {quantity}")

# Calculate the total cost of the order
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
print(f"\nTotal Cost: ${total_cost:.2f}")
