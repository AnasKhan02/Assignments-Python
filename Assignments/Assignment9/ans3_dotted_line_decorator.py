from functools import wraps

def dotted_line_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("." * 20)
        result = func(*args, **kwargs)
        print("." * 20)
        return result
    return wrapper
