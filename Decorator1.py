def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Finished calling '{func.__name__}'")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
