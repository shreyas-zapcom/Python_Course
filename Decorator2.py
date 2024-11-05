import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of '{func.__name__}': {end_time - start_time} seconds")
        return result
    return wrapper

@timer_decorator
def compute_square(n):
    return [i * i for i in range(n)]

compute_square(100000)
