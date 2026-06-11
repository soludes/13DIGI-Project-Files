def generate_receipt():
    global current_order

    if current_order is None:
        return

    order_list.delete(0, END)

    order_list.insert(END, "===== RECEIPT =====")
    order_list.insert(END, f"Customer: {current_order.customer_name}")
    order_list.insert(END, "")

    for item in current_order.items:

        pizza_name = pizza_menu[item.pizza_index][0]

        order_list.insert(
            END,
            f"{item.quantity} x {pizza_name} ({item.size})"
        )

    order_list.insert(END, "")
    order_list.insert(
        END,
        f"Total: ${calculate_total(current_order)}"
    )
