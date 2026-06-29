from tkinter import *
from tkinter import ttk

from storeOrdersV1 import Order, OrderItem
from pizzaMenuV1 import pizza_menu
from priceCalculationV1 import calculate_total
from recieptMakerV1 import generate_receipt


current_order = None


def start_order():
    global current_order

    customer_name = name_entry.get()

    if customer_name != "":
        current_order = Order(customer_name)

        order_list.delete(0, END)
        order_list.insert(END, f"Order for {customer_name}")


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


def make_receipt():
    if current_order is not None:
        generate_receipt(
            current_order,
            pizza_menu,
            order_list
        )


window = Tk()
window.title("Pizza Ordering System V2")
window.geometry("500x500")


Label(window, text="Customer Name").pack()

name_entry = Entry(window)
name_entry.pack()

Button(
    window,
    text="Start Order",
    command=start_order
).pack(pady=5)


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


Label(window, text="Size").pack()

size_box = ttk.Combobox(
    window,
    values=["Small", "Medium", "Large"]
)

size_box.current(0)
size_box.pack()


stuffed_var = BooleanVar()

Checkbutton(
    window,
    text="Stuffed Crust",
    variable=stuffed_var
).pack()


Label(window, text="Quantity").pack()

quantity_spinbox = Spinbox(
    window,
    from_=1,
    to=10
)

quantity_spinbox.pack()


Button(
    window,
    text="Add Pizza",
    command=add_pizza
).pack(pady=10)


Button(
    window,
    text="Generate Receipt",
    command=make_receipt
).pack(pady=10)


Label(window, text="Current Order").pack()

order_list = Listbox(
    window,
    width=50,
    height=10
)

order_list.pack()


window.mainloop()
