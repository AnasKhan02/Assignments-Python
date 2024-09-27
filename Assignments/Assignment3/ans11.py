# 11. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

result = is_prime(11)
print(result)  # Output: True
