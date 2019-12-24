items = []

item_name = input("Item (enter 'done' when finished): ")

while item_name != 'done':
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    items.append({"name": item_name, "price": price, "quantity": quantity})

    item_name = input("Item (enter 'done' when finished): ")

print("\nReceipt:\n")

total = 0
for i in items:
	print(str(i["quantity"]) +" "+ i["name"] +" "+ str(i['quantity']*i['price']) + " KD")
	total = total + i["price"]*i["quantity"]

print("\nYour total is %s" %str(total) + " KD")