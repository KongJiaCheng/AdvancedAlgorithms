import time
import math

# ===== FACTORIAL FUNCTION =====
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Reuse math.factorial like your original design
def factorial_task(n):
    return math.factorial(n)

# ===== SINGLE-THREADED RUNNER =====
def run_singlethreaded_factorials():
    numbers = [50, 100, 200]
    start = time.time_ns()
    for n in numbers:
        factorial_task(n)
    end = time.time_ns()
    return end - start


# ===== SINGLE-THREADED TEST LOOP =====
def test_singlethreaded():
    print("\n=== Single-threaded Factorial Computation ===")
    times = []
    for i in range(10):
        t = run_singlethreaded_factorials()
        times.append(t)
        print(f"Round {i+1}: Time taken = {t} ns")
    avg = sum(times) / len(times)
    print(f"\nAverage Time (10 rounds): {avg:.0f} ns")


# ===== RUN IF EXECUTED DIRECTLY =====
if __name__ == "__main__":
    test_singlethreaded()
