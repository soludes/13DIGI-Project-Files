#This function stores the orders and remembers the selections
class OrderItem:
    def __init__(self, pizza_index, size, stuffed_crust, quantity):
        self.pizza_index = pizza_index
        self.size = size
        self.stuffed_crust = stuffed_crust
        self.quantity = quantity

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
