def is_prime(n):
    if n<=1: return False
    for i in range(2,int(n**0.5) + 1):
        if(n % i == 0):
            return False
    return True

def printall_prime(start,end):
    primes = []
    for nums in range(start,end):
        if is_prime(nums):
            primes.append(nums)
    return primes

start = 50
end = 150

print(printall_prime(start,end))

count_prime = len(printall_prime(start,end))

print(count_prime)
