import datetime

menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

print("\n Welcome to TechDeepanshi Cafe")
print("\n----------- MENU -----------")
for item, price in menu.items():
    print(f"{item:<10} : Rs {price}")
print("-----------------------------\n")

order_list = []
order_total = 0

while True:
    item = input("Enter item name to order: ").title()

    if item not in menu:
        print("Item not available! Try again.\n")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity! Try again.\n")
        continue

    price = menu[item] * qty
    order_list.append([item, qty, menu[item], price])
    order_total += price

    another = input("Do you want to add another item? (Yes/No): ").lower()
    if another != "yes":
        break


gst_rate = 0.05
gst_amount = order_total * gst_rate

discount = 0
if order_total >= 200:
    discount = order_total * 0.10  # 10% discount

final_amount = order_total + gst_amount - discount

print("\n=========== BILL SUMMARY ===========")
print(f"{'Item':<10}{'Qty':<5}{'Price':<8}{'Total'}")
print("-------------------------------------")

for item, qty, price_each, total_price in order_list:
    print(f"{item:<10}{qty:<5}{price_each:<8}{total_price}")

print("-------------------------------------")
print(f"Subtotal       : Rs {order_total}")
print(f"GST (5%)       : Rs {gst_amount:.2f}")
print(f"Discount       : Rs {discount:.2f}")
print(f"Grand Total    : Rs {final_amount:.2f}")
print("=====================================")


save = input("\nDo you want to save the receipt? (Yes/No): ").lower()
if save == "yes":
    with open("receipt.txt", "w") as file:
        file.write("------ IT Cafe Receipt ------\n")
        file.write(str(datetime.datetime.now()) + "\n\n")
        for item, qty, price_each, total_price in order_list:
            file.write(f"{item} x{qty} - Rs {total_price}\n")
        file.write("\nSubtotal: Rs " + str(order_total))
        file.write("\nGST: Rs " + str(round(gst_amount, 2)))
        file.write("\nDiscount: Rs " + str(round(discount, 2)))
        file.write("\nGrand Total: Rs " + str(round(final_amount, 2)))
        file.write("\n------------------------------")
    print("Receipt saved as 'receipt.txt'")

print("\n Thank you for visiting IT Cafe!")
