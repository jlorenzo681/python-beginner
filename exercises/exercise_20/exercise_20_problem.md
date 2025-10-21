# Exercise 20: Prime Number Finder

## Difficulty: Advanced

## Description
Create a program that finds all prime numbers up to a given number using the Sieve of Eratosthenes algorithm or simple trial division.

## Learning Objectives
- Understand algorithm implementation
- Practice nested loops
- Work with lists and conditions
- Learn about prime numbers and optimization

## Requirements
- Ask the user for a number N
- Find all prime numbers from 2 to N
- Display the prime numbers
- Display the count of primes found
- Bonus: Calculate and display how long it took to find them

## Expected Output
```
Enter a number: 30
Prime numbers up to 30:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
Total primes found: 10
```

## Hints
- A prime number is only divisible by 1 and itself
- Start checking from 2 (the first prime)
- For each number, check if it's divisible by any number from 2 to sqrt(n)
- If no divisors found, it's prime
- Use a function to check if a number is prime
- Use a list to store all primes found

## Challenge
Implement two versions:
1. Simple trial division method
2. Sieve of Eratosthenes (more efficient for large numbers)
