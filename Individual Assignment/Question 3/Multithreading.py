import threading
import time
import math

# ===== FACTORIAL FUNCTION =====
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Reuse math.factorial for faster computation (same as your original code)
def factorial_task(n):
    return math.factorial(n)

# ===== MULTITHREADED RUNNER =====
def run_multithreaded_factorials():
    numbers = [50, 100, 200]
    threads = []
    start_times = {}
    end_times = {}

    def worker(n):
        start_times[n] = time.time_ns()
        factorial_task(n)
        end_times[n] = time.time_ns()

    # Create threads
    for n in numbers:
        t = threading.Thread(target=worker, args=(n,))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    # Total elapsed time
    total_time = max(end_times.values()) - min(start_times.values())
    return total_time


# ===== MULTITHREADED TEST LOOP =====
def test_multithreaded():
    print("=== Multithreaded Factorial Computation ===")
    times = []
    for i in range(10):
        t = run_multithreaded_factorials()
        times.append(t)
        print(f"Round {i+1}: Time taken = {t} ns")
    avg = sum(times) / len(times)
    print(f"\nAverage Time (10 rounds): {avg:.0f} ns")


# ===== RUN IF EXECUTED DIRECTLY =====
if __name__ == "__main__":
    test_multithreaded()
