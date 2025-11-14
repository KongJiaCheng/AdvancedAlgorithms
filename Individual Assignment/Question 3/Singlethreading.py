import time
import math#for math.factorial()

# ===== FACTORIAL FUNCTION =====
def factorial(n):
    result = 1
    for i in range(1, n + 1): #loops from 1 to n
        result *= i
    return result

def factorial_task(n):
    return math.factorial(n)

# ===== SINGLE-THREADED RUNNER =====
def run_singlethreaded_factorials(): #a function that runs all factorial calculations sequentially (one after another)
    numbers = [50, 100, 200]
    start = time.time_ns() #record start time in ns
    for n in numbers:
        factorial_task(n) #computes factorial one at a time (no threading, no concurrency, no parallelism)
    end = time.time_ns() #record end time after all factorials finish
    return end - start


# ===== SINGLE-THREADED TEST LOOP =====
def test_singlethreaded():
    print("\n=== Single-threaded Factorial Computation ===")
    times = [] #create an empty list to store the time from each round
    for i in range(10):
        t = run_singlethreaded_factorials() #calls run_singlethreaded_factorials()
        times.append(t) #store the time in the times list
        print(f"Round {i+1}: Time taken = {t} ns") #print the time for that round
    avg = sum(times) / len(times)
    print(f"\nAverage Time (10 rounds): {avg:.0f} ns")


# ===== RUN IF EXECUTED DIRECTLY =====
if __name__ == "__main__":
    test_singlethreaded()
