# ======================================================
# 1D ARRAY (PYTHON LIST) INVENTORY SYSTEM
# ======================================================

# Baby Product Entity
class BabyProduct:
    def __init__(self, pid, name, category, price, stock): #Constructor (BabyProduct)
        self.pid = pid
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.pid}, Name: {self.name}, Category: {self.category}, Price: RM{self.price}, Stock: {self.stock}"
#convert object to a string

# ======================================================
# 1D ARRAY (LIST) STRUCTURE
# ======================================================
product_list = [] #empty python list hold BabyProduct objects (1D array)


# Insert product into list
def insert_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: ")) #convert input string into float
    stock = int(input("Enter Stock: ")) #convert input string into int

    new_product = BabyProduct(pid, name, category, price, stock) #create instance of BabyProduct with collected values
    product_list.append(new_product) #append new BabyProduct object to end of the product_list

    print("\nProduct added successfully!\n")


# Search product by PID
def search_product():
    pid = input("Enter Product ID to Search: ")
    for product in product_list: #iterates every BabyProduct stored in the list
        if product.pid == pid: #check whether current pid matches input pid
            print("\nProduct Found:")
            print(product)
            print()
            return product #returns matched BabyProduct object to the caller and exits immediately

    print("\nProduct NOT found.\n")
    return None


# Edit product details
def edit_product():
    pid = input("Enter Product ID to Edit: ")

    for product in product_list: #iterate to check for matching pid
        if product.pid == pid:
            print("\nCurrent Details:")
            print(product)

            print("\nEnter New Details (leave blank to keep current):")

            new_name = input("New Name: ")
            new_category = input("New Category: ")
            new_price = input("New Price: ")
            new_stock = input("New Stock: ")

            if new_name: #if new name is not empty, assign it to product.name
                product.name = new_name
            if new_category:#if new name is not empty, assign it to product.category
                product.category = new_category
            if new_price:#if new name is not empty, assign it to product.price and convert it to float
                product.price = float(new_price)
            if new_stock:#if new name is not empty, assign it to product.stock and convert it to int
                product.stock = int(new_stock)

            print("\nProduct updated successfully!\n")
            return

    print("\nProduct NOT found.\n")


# Delete product
def delete_product():
    pid = input("Enter Product ID to Delete: ")

    for i, product in enumerate(product_list): #iterates with index i and item product. Enumerate used as deleting by index is convenient
        if product.pid == pid:
            del product_list[i] #remove item at index i and shift items to the left
            print("\nProduct deleted successfully!\n")
            return

    print("\nProduct NOT found.\n")


# Display all products
def display_products():
    if not product_list: #check whether the list is empty
        print("\nNo products in the inventory.\n")
        return

    print("\n===== ALL PRODUCTS =====")
    for product in product_list: #iterates over every product in product_list and print(product)
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
def menu(): #defines interactive CLI main loop
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
