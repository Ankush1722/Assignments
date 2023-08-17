import random as random
import math

# Create a list of 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

# (i) print all odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print("\nodd numbers:", odd_numbers)

# (ii) print all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print("\nEven numbers:", even_numbers)

# (iii) print all prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print("\nPrime numbers:", prime_numbers)

