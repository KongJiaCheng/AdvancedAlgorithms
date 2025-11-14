# ======================================================
# 1D ARRAY (PYTHON LIST) INVENTORY SYSTEM
# ======================================================

# Baby Product Entity
class BabyProduct:
    def __init__(self, pid, name, category, price, stock):
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.pid}, Name: {self.name}, Category: {self.category}, Price: RM{self.price}, Stock: {self.stock}"


# ======================================================
# 1D ARRAY (LIST) STRUCTURE
# ======================================================
product_list = []


# Insert product into list
def insert_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))

    new_product = BabyProduct(pid, name, category, price, stock)
    product_list.append(new_product)

    print("\nProduct added successfully!\n")


# Search product by PID
def search_product():
    pid = input("Enter Product ID to Search: ")
    for product in product_list:
        if product.pid == pid:
            print("\nProduct Found:")
            print(product)
            print()
            return product

    print("\nProduct NOT found.\n")
    return None


# Edit product details
def edit_product():
    pid = input("Enter Product ID to Edit: ")

    for product in product_list:
        if product.pid == pid:
            print("\nCurrent Details:")
            print(product)

            print("\nEnter New Details (leave blank to keep current):")

            new_name = input("New Name: ")
            new_category = input("New Category: ")
            new_price = input("New Price: ")
            new_stock = input("New Stock: ")

            if new_name:
                product.name = new_name
            if new_category:
                product.category = new_category
            if new_price:
                product.price = float(new_price)
            if new_stock:
                product.stock = int(new_stock)

            print("\nProduct updated successfully!\n")
            return

    print("\nProduct NOT found.\n")


# Delete product
def delete_product():
    pid = input("Enter Product ID to Delete: ")

    for i, product in enumerate(product_list):
        if product.pid == pid:
            del product_list[i]
            print("\nProduct deleted successfully!\n")
            return

    print("\nProduct NOT found.\n")


# Display all products
def display_products():
    if not product_list:
        print("\nNo products in the inventory.\n")
        return

    print("\n===== ALL PRODUCTS =====")
    for product in product_list:
        print(product)
    print()


# ======================================================
# PRE-DEFINED SAMPLE DATA
# ======================================================
def preload_products():
    samples = [
        BabyProduct("P001", "Baby Shampoo", "Bath", 12.5, 50),
        BabyProduct("P002", "Diapers Size 3", "Diaper", 45.0, 30),
        BabyProduct("P003", "Baby Lotion", "Skincare", 18.0, 25),
    ]
    product_list.extend(samples)


# ======================================================
# MENU
# ======================================================
def menu():
    preload_products()  # Load initial items
    while True:
        print("========== 1D LIST INVENTORY SYSTEM ==========")
        print("1. Insert Product")
        print("2. Search Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Display All Products")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            insert_product()
        elif choice == "2":
            search_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            display_products()
        elif choice == "6":
            print("\nExiting Program...\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


# ======================================================
# RUN PROGRAM
# ======================================================
if __name__ == "__main__":
    menu()
