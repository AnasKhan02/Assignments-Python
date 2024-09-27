# 03  Example of Using multiple decorators on a single function

def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("Anas Khan")
