menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]

# Assign a number to each item on the menu
for i, item in enumerate(menu):
    print(f"{i+1}. {item[0]}: {item[1]}")

total_bill = 0
orders = []

while True:
    item_num = input("Which item would you like to order? or press enter to exit.")
    if not item_num:
        break

    item_num = int(item_num)
    if item_num < 1 or item_num > len(menu):
        print("Invalid item number. Please try again.")
        continue
    item = menu[item_num-1][0]
    price = menu[item_num-1][1]
    frequency = int(input("How many would you like to order? "))
    bill = frequency * price
    total_bill += bill
    orders.append((item, frequency, bill))
sum=0
print("Your order: ")
for order in orders:
    print(f"{order[0]} x {order[1]}: {order[2]}")
    sum+= order[1]
print(f"Total items: {sum}")
print(f"Total Bill: {total_bill}")
