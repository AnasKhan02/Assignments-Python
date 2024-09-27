# 02. Write a Python program that implements a decorator to measure the memory usage of a function.

from memory_profiler import memory_usage

def memory_profiler(func):
    def wrapper(*args, **kwargs):
        mem_usage = memory_usage((func, args, kwargs))
        print(f"Memory usage (in MiB): {max(mem_usage) - min(mem_usage)}")
        return func(*args, **kwargs)
    return wrapper

@memory_profiler
def example_function(n):
    # Example function that uses a list
    return [i for i in range(n)]

if __name__ == "__main__":
    # Example usage
    example_function(1000000)
