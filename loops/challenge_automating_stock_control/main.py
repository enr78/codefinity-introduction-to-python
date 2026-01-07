# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item in inventory.values():
    print(item)

while inventory.values([0]) >= inventory.values(1):
    inventory.values([0]) += inventory.values([2])
print(inventory)













# for i in inventory:
#     while inventory[i][0] < inventory[i][1]:
#         inventory[i][0] += inventory[i][2]
#     print("{key}: {value}")








