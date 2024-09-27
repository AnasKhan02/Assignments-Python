# Problem 01
# ----------
#
# Let's dive into decorators! You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:
#
#
# +91 xxxxx xxxxx
#
# The given mobile numbers may have ,  or  written before the actual  digit number. Alternatively, there may not be any prefix at all.
#
# Input Format
#
# The first line of input contains an integer , the number of mobile phone numbers.
#  lines follow each containing a mobile number.
#
# Output Format
#
# Print  mobile numbers on separate lines in the required format.
#
# Sample Input
#
# 3
# 07895462130
# 919875641230
# 9195969878
# Sample Output
#
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230
# Concept
#
# Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps here.
# To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.
#
# def wrapper(f):
#     def fun(l):
#         # complete the function
#     return fun
#
# @wrapper
#

# Ans 1-
def wrapper(func):
    def fun(numbers):
        standardized_numbers = []
        for number in numbers:
            # Remove any prefix (like 0 or 91) and standardize the format
            if len(number) == 10:
                standardized_numbers.append(f"+91 {number[:5]} {number[5:]}")
            else:
                number = number.strip()  # Remove any leading/trailing whitespace
                if number.startswith('0'):
                    number = number[1:]  # Remove leading 0
                elif number.startswith('91'):
                    number = number[2:]  # Remove leading 91

                standardized_numbers.append(f"+91 {number[:5]} {number[5:]}")

        return func(sorted(standardized_numbers))

    return fun


@wrapper
def print_sorted_numbers(numbers):
    for number in numbers:
        print(number)


# Sample input processing
if __name__ == "__main__":
    n = int(input())
    mobile_numbers = [input().strip() for _ in range(n)]

    print_sorted_numbers(mobile_numbers)
