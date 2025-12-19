import functools

class MathService:

    @staticmethod
    def log_execution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Calling method: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    @log_execution
    def add(self, a, b):
        return a + b

m = MathService()
print(m.add(5,10))