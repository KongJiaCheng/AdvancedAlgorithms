import threading #allows to create and run multiple threads concurrently
import time
import math#for math.factorial()

# ===== FACTORIAL FUNCTION =====
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Reuse math.factorial for faster computation
def factorial_task(value):
    return math.factorial(value)

# ===== MULTITHREADED RUNNER =====
def run_multithreaded_factorials(): #A function that will create multiple threads, run factorial computations in parallel and measure how long the entire multi-thread run takes
    numbers = [50, 100, 200]
    threads = [] #list to store thread objects
    start_times = {} #dictionary storing start time for each number (key = number)
    end_times = {} #dictionary storing end time for each number

    def worker(task_value):
        start_times[task_value] = time.time_ns() #record the time in ns when this thread starts
        factorial_task(task_value) #Perform factorial computation
        end_times[task_value] = time.time_ns() #Record when the thread finishes

    # Create threads
    for n_value in numbers:
        t = threading.Thread(target=worker, args=(n_value,))#Create a new thread that will call worker(n)
        threads.append(t)#Store thread in list for later joining
        t.start()#Start the thread - execution begins immediately

    # Wait for all threads
    for t in threads: #.join() blocks the main thread until each worker thread completes
        t.join() #ensures all factorials are finished before measuring total time

    # Total elapsed time
    total_time = max(end_times.values()) - min(start_times.values())
    return total_time

# ===== MULTITHREADED TEST LOOP =====
def test_multithreaded():
    print("=== Multithreaded Factorial Computation ===")
    times = [] #creates a list to save each round's total execution time
    for i in range(10):
        t = run_multithreaded_factorials() #calls run_multithreaded_factorials() each round
        times.append(t) #stores each time value in times
        print(f"Round {i+1}: Time taken = {t} ns") #prints execution time for that round
    avg = sum(times) / len(times) #computes average time over the 10 runs
    print(f"\nAverage Time (10 rounds): {avg:.0f} ns")

# ===== RUN IF EXECUTED DIRECTLY =====
if __name__ == "__main__":
    test_multithreaded()
