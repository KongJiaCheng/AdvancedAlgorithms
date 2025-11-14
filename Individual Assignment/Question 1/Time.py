# ======================================================
# SEARCH TIME COMPARISON FOR:
# 1. HashTable (Separate Chaining)
# 2. 1D Array (Python List)
# ======================================================

import time

# IMPORT YOUR EXISTING HASH TABLE
from HashTable import HashTable, BabyProduct

# ======= 1D ARRAY =========
product_list = []


# Insert product into 1D array
def array_insert(product):
    product_list.append(product)


# Search from 1D array
def array_search(pid):
    for product in product_list:
        if product.pid == pid:
            return product
    return None


# ======================================================
# Load sample data into BOTH structures
# ======================================================
def preload_data(hash_table, count=30):
    for i in range(count):
        pid = f"B{i+1:03}"  # B001, B002, ...
        product = BabyProduct(pid, f"Item{i+1}", "Category", 10 + i, 50)

        # Insert into hash table
        hash_table.insert(pid, product)

        # Insert into 1D array
        array_insert(product)


# ======================================================
# Time measurement wrapper
# ======================================================
def measure_search_time(search_function, key, rounds=10, repetitions=100000):
    times = []
    for _ in range(rounds):
        start = time.perf_counter_ns()
        for _ in range(repetitions):
            search_function(key)
        end = time.perf_counter_ns()
        times.append(end - start)
    return times


# ======================================================
# Main Testing Function
# ======================================================
def compare_search_times():
    hash_table = HashTable(50)
    preload_data(hash_table, count=30)

    search_key = "B010"
    rounds = 10  # now used properly

    print("===== SEARCH TIME COMPARISON =====\n")
    print(f"Testing search for: {search_key}\n")

    hash_times = measure_search_time(lambda k: hash_table.search(k), search_key, rounds)
    array_times = measure_search_time(lambda k: array_search(k), search_key, rounds)

    print("HashTable (Separate Chaining) Times (ns):")
    print(hash_times)
    print(f"Average: {sum(hash_times) / len(hash_times):.2f} ns\n")

    print("1D Array (Python List) Times (ns):")
    print(array_times)
    print(f"Average: {sum(array_times) / len(array_times):.2f} ns\n")


# ======================================================
# RUN PROGRAM
# ======================================================
if __name__ == "__main__":
    compare_search_times()
