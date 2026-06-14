def generate_receipt():
    global current_order

    if current_order is None:
        return

    receipt = "===== RECEIPT =====\n"
    receipt += f"Customer: {current_order.customer_name}\n\n"

    order_list.delete(0, END)

    order_list.insert(END, "===== RECEIPT =====")
    order_list.insert(END, f"Customer: {current_order.customer_name}")
    order_list.insert(END, "")

    for item in current_order.items:

        pizza_name = pizza_menu[item.pizza_index][0]

        line = f"{item.quantity} x {pizza_name} ({item.size})"

        # Add to receipt text
        receipt += line + "\n"

        # Add to GUI
        order_list.insert(
            END,
            line
        )

    total = calculate_total(current_order)

    receipt += f"\nTotal: ${total}"

    order_list.insert(
        END,
        ""
    )

    order_list.insert(
        END,
        f"Total: ${total}"
    )

    # Save receipt to a text file
    file = open("receipt.txt", "w")
    file.write(receipt)
    file.close()

    print("Receipt saved!")