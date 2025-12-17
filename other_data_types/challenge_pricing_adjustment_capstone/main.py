grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (grocery_inventory["Eggs"][0], grocery_inventory["Eggs"][1] - 1.0, grocery_inventory["Eggs"][2])
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Grocery Inventory after adding Tomatoes: ", grocery_inventory)

if grocery_inventory["Milk"][2] < 10:
    print("milk needs to be restocked. Increasing stock by 20 units.", grocery_inventory)
    grocery_inventory["Milk"] = (grocery_inventory["Milk"][0], grocery_inventory["Milk"][1], grocery_inventory["Milk"][2] + 20)
else:
    print("Milk has sufficient stock.")

if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")

print("Updated inventory: ", grocery_inventory)



