from tkinter import END
from priceCalculationV1 import calculate_total


def generate_receipt(order, pizza_menu, order_list):

    receipt = "===== RECEIPT =====\n"
    receipt += f"Customer: {order.customer_name}\n\n"

    order_list.delete(0, END)

    order_list.insert(END, "===== RECEIPT =====")
    order_list.insert(END, f"Customer: {order.customer_name}")
    order_list.insert(END, "")

    for item in order.items:

        pizza_name = pizza_menu[item.pizza_index][0]

        line = f"{item.quantity} x {pizza_name} ({item.size})"

        receipt += line + "\n"

        order_list.insert(
            END,
            line
        )

    total = calculate_total(order, pizza_menu)

    receipt += f"\nTotal: ${total}"

    order_list.insert(END, "")
    order_list.insert(
        END,
        f"Total: ${total}"
    )


    file = open("receipt.txt", "w")
    file.write(receipt)
    file.close()

    print("Receipt saved!")