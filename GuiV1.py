# This is the GUI opens when you run main.py
from tkinter import *
from tkinter import ttk


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


pizza_menu = [
    ["Hawaiian", [12, 15, 18], [15, 18, 21]],
    ["Pepperoni", [13, 16, 19], [16, 19, 22]],
    ["Meat Lovers", [14, 17, 20], [17, 20, 23]],
    ["BBQ Chicken", [14, 17, 20], [17, 20, 23]],
    ["Vegetarian", [12, 15, 18], [15, 18, 21]],
    ["Cheese", [11, 14, 17], [14, 17, 20]]
]

current_order = None


def start_order():
    global current_order

    customer_name = name_entry.get()

    if customer_name != "":
        current_order = Order(customer_name)

        order_list.delete(0, END)
        order_list.insert(END, f"Order for {customer_name}")

        print("Order created")


def add_pizza():
    global current_order

    if current_order is None:
        return

    pizza_index = pizza_box.current()
    size = size_box.get()
    stuffed = stuffed_var.get()
    quantity = int(quantity_spinbox.get())

    item = OrderItem(
        pizza_index,
        size,
        stuffed,
        quantity
    )

    current_order.add_item(item)

    pizza_name = pizza_menu[pizza_index][0]

    order_list.insert(
        END,
        f"{pizza_name} | {size} | x{quantity}"
    )


# GUI

window = Tk()
window.title("Pizza Ordering System")
window.geometry("500x500")

# Customer Name

Label(window, text="Customer Name").pack()

name_entry = Entry(window)
name_entry.pack()

Button(
    window,
    text="Start Order",
    command=start_order
).pack(pady=5)

# Pizza Selection

Label(window, text="Pizza").pack()

pizza_box = ttk.Combobox(
    window,
    values=[
        "Hawaiian",
        "Pepperoni",
        "Meat Lovers",
        "BBQ Chicken",
        "Vegetarian",
        "Cheese"
    ]
)

pizza_box.current(0)
pizza_box.pack()

# Size Selection

Label(window, text="Size").pack()

size_box = ttk.Combobox(
    window,
    values=["Small", "Medium", "Large"]
)

size_box.current(0)
size_box.pack()

# Stuffed Crust

stuffed_var = BooleanVar()

Checkbutton(
    window,
    text="Stuffed Crust",
    variable=stuffed_var
).pack()    

# Quantity

Label(window, text="Quantity").pack()

quantity_spinbox = Spinbox(
    window,
    from_=1,
    to=10
)

quantity_spinbox.pack()

# Add Pizza Button

Button(
    window,
    text="Add Pizza",
    command=add_pizza
).pack(pady =10)

# Order Display

Label(window, text="Current Order").pack()

order_list = Listbox(
    window,
    width=50,
    height=10
)

order_list.pack()

window.mainloop()