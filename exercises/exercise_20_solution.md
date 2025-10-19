# Exercise 20: Solution

## Solution 1: Trial Division Method
```python
def is_prime(n):
    """Check if a number is prime using trial division."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Main program
n = int(input("Enter a number: "))

primes = []
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

print(f"Prime numbers up to {n}:")
print(primes)
print(f"Total primes found: {len(primes)}")
```

## Solution 2: Sieve of Eratosthenes (More Efficient)
```python
def sieve_of_eratosthenes(n):
    """Find all primes up to n using Sieve of Eratosthenes."""
    if n < 2:
        return []

    # Create a boolean array and initialize all as True
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # Start with 2, mark all its multiples as not prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    # Collect all numbers that are still marked as prime
    primes = [num for num in range(n + 1) if is_prime[num]]
    return primes

# Main program
n = int(input("Enter a number: "))

primes = sieve_of_eratosthenes(n)

print(f"Prime numbers up to {n}:")
print(primes)
print(f"Total primes found: {len(primes)}")
```

## Solution 3: With Timing
```python
import time

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Main program
n = int(input("Enter a number: "))

start_time = time.time()

primes = [num for num in range(2, n + 1) if is_prime(num)]

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Prime numbers up to {n}:")
print(primes)
print(f"Total primes found: {len(primes)}")
print(f"Time taken: {elapsed_time:.4f} seconds")
```

## Explanation

### Trial Division Method
- For each number, we check if it has any divisors
- We only need to check up to the square root of the number
- We skip even numbers after 2 (optimization)
- If no divisors are found, the number is prime

### Sieve of Eratosthenes
- Create a list marking all numbers as potentially prime
- For each prime found, mark all its multiples as not prime
- Much more efficient for finding many primes
- Time complexity: O(n log log n)

## Key Concepts
- **Prime numbers**: Natural numbers greater than 1 with no divisors except 1 and itself
- **Square root optimization**: Only need to check divisors up to √n
- **Algorithm efficiency**: Different approaches have different performance
- **List comprehensions**: Creating lists efficiently
- **Time module**: Measuring execution time

## Why Check Only to Square Root?
If n = a × b and a ≤ b, then a ≤ √n.
So if n has a divisor, at least one will be ≤ √n.

Example: 36 = 6 × 6
- Divisors: 1, 2, 3, 4, 6, 9, 12, 18, 36
- √36 = 6
- We only need to check 2, 3, 4, 5, 6 to find all divisor pairs

## Performance Comparison
```python
import time

def compare_methods(n):
    # Trial division
    start = time.time()
    primes1 = [num for num in range(2, n+1) if is_prime(num)]
    time1 = time.time() - start

    # Sieve
    start = time.time()
    primes2 = sieve_of_eratosthenes(n)
    time2 = time.time() - start

    print(f"Trial division: {time1:.4f}s")
    print(f"Sieve: {time2:.4f}s")
    print(f"Sieve is {time1/time2:.2f}x faster")

compare_methods(10000)
```

## Interactive Version
```python
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print("Prime Number Finder")
print("-" * 40)

while True:
    try:
        n = int(input("\nEnter a number (0 to quit): "))

        if n == 0:
            print("Goodbye!")
            break

        if n < 2:
            print("Please enter a number greater than 1.")
            continue

        primes = [num for num in range(2, n + 1) if is_prime(num)]

        print(f"\nPrime numbers up to {n}:")
        if len(primes) <= 20:
            print(primes)
        else:
            print(f"First 10: {primes[:10]}")
            print(f"Last 10: {primes[-10:]}")

        print(f"Total primes found: {len(primes)}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")
```

## Common Prime-Related Functions
```python
def nth_prime(n):
    """Find the nth prime number."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

def prime_factors(n):
    """Find prime factors of n."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

print(f"10th prime: {nth_prime(10)}")  # 29
print(f"Prime factors of 60: {prime_factors(60)}")  # [2, 2, 3, 5]
```
