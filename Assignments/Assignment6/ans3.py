# timing_decorator.py
import time
from functools import wraps

def timing_decorator(func):
    """Decorator to calculate the time taken by a function to execute."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper
