from typing import Optional

# ------------------------------
# 1️⃣ Hash Table with Separate Chaining
# ------------------------------
class HashTable:
    class Node:
        def __init__(self, key, value): #Constructor(Node)
            self.key = key
            self.value = value
            self.next: Optional['HashTable.Node'] = None

    def __init__(self, capacity=10): #Constructor(Hash Table)
        self.capacity = capacity
        self.table: list[Optional['HashTable.Node']] = [None] * capacity  #Python list slot (bucket hold either empty or node)

    def _hash(self, key): #internal helper method to compute index
        return hash(key) % self.capacity #reduce hash to valid bucket index between 0 and capacity

    def insert(self, key, value): #add key
        index = self._hash(key) #computes bucket index
        new_node = self.Node(key, value) #creates new node
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index] #If have collision, pass over linked list
            while True:
                if current.key == key:
                    current.value = value  # update with new value (prevent duplicate key)
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value #return stored value
            current = current.next #continue the search
        return None

    def delete(self, key):
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next #link prev.next to current.next (removes current)
                else:
                    self.table[index] = current.next #Update bucket head
                return True #deletion successful
            prev = current #set prev to current
            current = current.next #move current to current.next
        return False


# ------------------------------
# 2️⃣ Baby Product Entity
# ------------------------------
class BabyProduct:
    def __init__(self, pid: str, name: str, category: str, price: float, stock: int):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock #Attributes

    def __str__(self):
        return f"{self.name} ({self.category}) - RM{self.price:.2f}, Stock: {self.stock}"
#return human-readable string with price of two decimal places

# ------------------------------
# 3️⃣ Local Storage / Pre-defined Products
# ------------------------------
inventory = HashTable(capacity=10) #create 10 buckets

predefined_products = [
    BabyProduct("P001", "Baby Shampoo", "Bath", 12.5, 50),
    BabyProduct("P002", "Diapers Size 3", "Diaper", 45.0, 30),
    BabyProduct("P003", "Baby Lotion", "Skincare", 18.0, 25),
]

# FIX VARIABLE SHADOWING
for prod in predefined_products:
    inventory.insert(prod.pid, prod) #ensuring loop variable name doesn't shadow


# ------------------------------
# 4️⃣ Command-Line Inventory System
# ------------------------------
def menu():
    while True:
        print("\n--- Baby Shop Inventory ---")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Display All Products")
        print("6. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            inventory.insert(pid, BabyProduct(pid, name, category, price, stock))
            print("Product inserted successfully.")

        elif choice == "2":
            pid = input("Enter Product ID to search: ")
            product = inventory.search(pid)
            print("Found:", product) if product else print("Product not found.")

        elif choice == "3":
            pid = input("Enter Product ID to edit: ")
            product = inventory.search(pid)
            if product:
                print("Current:", product)
                name = input(f"New Name [{product.name}]: ") or product.name
                category = input(f"New Category [{product.category}]: ") or product.category

                price = input(f"New Price [{product.price}]: ")
                price = float(price) if price else product.price #input returns string. If non-empty, convert to float/int, otherwise reuse existing value

                stock = input(f"New Stock [{product.stock}]: ")
                stock = int(stock) if stock else product.stock #input returns string. If non-empty, convert to float/int, otherwise reuse existing value

                inventory.insert(pid, BabyProduct(pid, name, category, price, stock))
                print("Product updated successfully.")
            else:
                print("Product not found.")

        elif choice == "4":
            pid = input("Enter Product ID to delete: ")
            print("Deleted successfully.") if inventory.delete(pid) else print("Product not found.")

        elif choice == "5":
            print("\n--- All Products ---")
            for i in range(inventory.capacity): #iterates through every bucket index (0..capacity-1)
                current = inventory.table[i]#for each bucket walks the linked list printing ID: {key}, {value}
                while current:
                    print(f"ID: {current.key}, {current.value}") #current.value calls BabyProduct.__str__ so product printed nicely
                    current = current.next

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
