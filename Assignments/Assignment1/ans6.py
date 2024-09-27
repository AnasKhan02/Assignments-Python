def is_armstrong(num):
    digits = str(num)
    n = len(digits)

    armstrong_sum = sum(int(digit) ** n for digit in digits)

    return armstrong_sum == num


def generate_armstrong_series(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers


start_range = 1
end_range = 1000 
armstrong_series = generate_armstrong_series(start_range, end_range)

print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_series}")
