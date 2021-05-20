def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, number in inventory.items():
        print(number, item)
        item_total += number

    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, items_to_add):
    for item in items_to_add:
        inventory.setdefault(item, 0)
        inventory[item] += 1


dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = {"gold coin": 42, "rope": 1}
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
