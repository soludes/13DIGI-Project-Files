def calculate_total(order, pizza_menu):
    total = 0

    for item in order.items:

        # Determine which price list to use
        if item.stuffed_crust:
            prices = pizza_menu[item.pizza_index][2]
        else:
            prices = pizza_menu[item.pizza_index][1]

        # Convert size to list index
        if item.size == "Small":
            size_index = 0
        elif item.size == "Medium":
            size_index = 1
        else:
            size_index = 2

        total += prices[size_index] * item.quantity

    return total

