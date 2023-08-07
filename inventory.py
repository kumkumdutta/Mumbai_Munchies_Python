import json

SNACK_INVENTORY_FILE = "snack_inventory.json"

def load_inventory():
    try:
        with open(SNACK_INVENTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def save_inventory(inventory):
    with open(SNACK_INVENTORY_FILE, "w") as f:
        json.dump(inventory, f)

def add_snack(inventory):
    snack_id = input("Enter Snack ID: ")
    snack_name = input("Enter Snack Name: ")
    price = float(input("Enter Snack Price: "))
    availability = input("Is the Snack available? (yes/no): ").lower()
    if availability not in ["yes", "no"]:
        print("Invalid input for availability. Please enter 'yes' or 'no'.")
        return
    snack = {
        "id": snack_id,
        "name": snack_name,
        "price": price,
        "availability": availability == "yes"
    }
    inventory.append(snack)
    save_inventory(inventory)
    print("Snack added successfully.")

def remove_snack(inventory):
    snack_id = input("Enter Snack ID to remove: ")
    for snack in inventory:
        if snack["id"] == snack_id:
            inventory.remove(snack)
            save_inventory(inventory)
            print("Snack removed successfully.")
            return
    print("Snack not found.")

def update_availability(inventory):
    snack_id = input("Enter Snack ID to update availability: ")
    for snack in inventory:
        if snack["id"] == snack_id:
            new_availability = input("Is the Snack available? (yes/no): ").lower()
            if new_availability not in ["yes", "no"]:
                print("Invalid input for availability. Please enter 'yes' or 'no'.")
                return
            snack["availability"] = new_availability == "yes"
            save_inventory(inventory)
            print("Availability updated successfully.")
            return
    print("Snack not found.")

def record_sale(inventory):
    snack_id = input("Enter Snack ID for the sale: ")
    for snack in inventory:
        if snack["id"] == snack_id:
            if snack["availability"]:
                snack["availability"] = False
                save_inventory(inventory)
                print("Sale recorded successfully.")
            else:
                print("Snack is not available for sale.")
            return
    print("Snack not found.")

def display_inventory(inventory):
    print("Current Snack Inventory:")
    for snack in inventory:
        print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Availability: {'Yes' if snack['availability'] else 'No'}")

def main():
    inventory = load_inventory()

    while True:
        print("\n========== Welcome to Mumbai Munchies - The Canteen Chronicle ==========")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack Availability")
        print("4. Record Sale")
        print("5. Display Inventory")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")
        if choice == "1":
            add_snack(inventory)
        elif choice == "2":
            remove_snack(inventory)
        elif choice == "3":
            update_availability(inventory)
        elif choice == "4":
            record_sale(inventory)
        elif choice == "5":
            display_inventory(inventory)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
