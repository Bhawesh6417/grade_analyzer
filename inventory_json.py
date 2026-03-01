import json

# Task 1: Read inventory
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total number of books:", len(inventory))

# Task 2: Add new book
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)

# Task 3: Display updated inventory
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
