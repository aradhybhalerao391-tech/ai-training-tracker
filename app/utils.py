from functools import wraps
def log_function(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Running {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper