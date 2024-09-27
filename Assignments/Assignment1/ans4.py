
def fact(n):
    if n==0:
        return 1
    if n==1 or n==2:
        return n
    return n*fact(n-1)

def sum_of_digit_factorials(n):
    return sum(fact(int(digit)) for digit in str(n))

def next_num(start):
    cur = start + 1
    while True:
        if cur == sum_of_digit_factorials(cur):
            return cur
        cur += 1
next_number = next_num(145)
print(next_number)

