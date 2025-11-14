from typing import TypeVar, Generic, Optional, List, Tuple

# ======================================================
# HashTableArray (Linear Probing)
# ======================================================

K = TypeVar('K')
V = TypeVar('V')

class HashTableArray(Generic[K, V]):
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.table: List[Optional[Tuple[K, V]]] = [None] * capacity
        self.size = 0

    def _hash(self, key: K) -> int:
        return hash(key) % self.capacity

    # ADD (insert only if not exists)
    def add(self, key: K, value: V) -> bool:
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print(f"⚠️ Add failed: key '{key}' already exists.")
                return False
            index = (index + 1) % self.capacity
            if index == start_index:
                print("⚠️ Hash table is full.")
                return False
        self.table[index] = (key, value)
        self.size += 1
        return True

    # EDIT (update only if key exists)
    def edit(self, key: K, new_value: V) -> bool:
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, new_value)
                return True
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        print(f"⚠️ Edit failed: key '{key}' not found.")
        return False

    # SEARCH
    def search(self, key: K) -> Optional[V]:
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        return None

    # DELETE
    def delete(self, key: K) -> bool:
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.capacity
            if index == start_index:
                break
        print(f"⚠️ Delete failed: key '{key}' not found.")
        return False


# ======================================================
# Baby Product Entity
# ======================================================

class BabyProduct:
    def __init__(self, pid: str, name: str, category: str, price: float, stock: int):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.category}) - RM{self.price:.2f}, Stock: {self.stock}"


# ======================================================
# Initialize Inventory with Predefined Products
# ======================================================

def initialize_inventory():
    inventory = HashTableArray(capacity=100)

    sample_products = [
        ("P001", "Baby Wipes", "Hygiene", 15.90, 100),
        ("P002", "Milk Bottle", "Feeding", 25.50, 50),
        ("P003", "Pacifier", "Accessories", 9.99, 200)
    ]

    for pid, name, category, price, stock in sample_products:
        inventory.add(pid, BabyProduct(pid, name, category, price, stock))

    return inventory


# ======================================================
# Command-Line Inventory System
# ======================================================

def menu():
    inventory = initialize_inventory()   # ← No shadowing

    while True:
        print("\n------ BABY PRODUCT INVENTORY SYSTEM ------")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Display All Products")
        print("6. Exit")

        choice = input("Enter option: ")

        # INSERT
        if choice == "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price (RM): "))
            stock = int(input("Stock: "))

            success = inventory.add(pid, BabyProduct(pid, name, category, price, stock))
            print("Product added." if success else "Failed to add product.")

        # SEARCH
        elif choice == "2":
            pid = input("Enter Product ID to search: ")
            product = inventory.search(pid)
            print(f"Found: {product}" if product else "❌ Product not found.")

        # EDIT
        elif choice == "3":
            pid = input("Product ID to edit: ")
            product = inventory.search(pid)

            if product:
                print("Current:", product)
                name = input(f"New Name [{product.name}]: ") or product.name
                category = input(f"New Category [{product.category}]: ") or product.category

                price_input = input(f"New Price [{product.price}]: ")
                price = float(price_input) if price_input else product.price

                stock_input = input(f"New Stock [{product.stock}]: ")
                stock = int(stock_input) if stock_input else product.stock

                updated_product = BabyProduct(pid, name, category, price, stock)
                inventory.edit(pid, updated_product)

                print("Product updated successfully.")
            else:
                print("❌ Product not found.")

        # DELETE
        elif choice == "4":
            pid = input("Product ID to delete: ")
            deleted = inventory.delete(pid)
            print("Deleted." if deleted else "❌ Product not found.")

        # DISPLAY ALL
        elif choice == "5":
            print("\n------ ALL PRODUCTS ------")
            for slot in inventory.table:
                if slot is not None:
                    print(f"ID: {slot[0]} → {slot[1]}")

        # EXIT
        elif choice == "6":
            print("Exiting system...")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Run only when executed directly
if __name__ == "__main__":
    menu()
