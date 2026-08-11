#Decorators in Python are a powerful tool that allows you to modify the behavior
# of functions or classes. They are often used for logging, access control, 
# memoization, and more. A decorator is a function that takes another function
# as an argument and extends or alters its behavior.
#Example of a simple decorator that logs the execution time of a function:
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@log_execution_time
def example_function():
    time.sleep(1)
    print("Function executed")

example_function()

def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
def hello():
    print("Hello World")

hello = decorator(hello)

hello()

def decorator(func):

    def wrapper(a, b):
        print("Adding numbers...")
        func(a, b)
        print("Addition completed")

    return wrapper
@decorator
def add(a, b):
    print(a + b)

add(10, 20)

def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper
@decorator
def multiply(a, b):
    return a * b

print(multiply(5, 4))
#Multiple Decorators
def decorator1(func):

    def wrapper():
        print("Decorator 1 Before")
        func()
        print("Decorator 1 After")

    return wrapper


def decorator2(func):

    def wrapper():
        print("Decorator 2 Before")
        func()
        print("Decorator 2 After")

    return wrapper


@decorator1
@decorator2
def hello():
    print("Hello")

def repeat(n):

    def decorator(func):

        def wrapper():
            for i in range(n):
                func()

        return wrapper

    return decorator
@repeat(3)
def hello():
    print("Hello")

hello()
#Preserving Function Metadata
def log(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log
def square(x):
    return x * x

print(square(5))

import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Time:", end - start)

        return result

    return wrapper
logged_in = True

def login_required(func):

    def wrapper():
        if logged_in:
            func()
        else:
            print("Login Required")

    return wrapper


@login_required
def profile():
    print("Welcome User")

profile()
def positive_only(func):

    def wrapper(x):
        if x < 0:
            print("Negative value not allowed")
            return
        return func(x)

    return wrapper


@positive_only
def square(x):
    print(x * x)

square(5)
square(-3)
#Custom decorators
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            print("Access denied. Please log in.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@require_login
def view_dashboard(user):
    print(f"Welcome {user['name']} to your dashboard!")

user1 = {"name": "Pradeep", "is_logged_in": True}
user2 = {"name": "Guest", "is_logged_in": False}

view_dashboard(user1)  # ✅ Works
view_dashboard(user2)  # ❌ Access denied
import functools
def validate_speed(func):
    @functools.wraps(func)
    def wrapper(self, speed, *args, **kwargs):
        if speed < 0:
            print("Speed cannot be negative!")
            return
        return func(self, speed, *args, **kwargs)
    return wrapper

class HybridCar:
    def __init__(self, model):
        self.model = model
        self.speed = 0

    @validate_speed
    def accelerate(self, speed):
        self.speed += speed
        print(f"{self.model} accelerated to {self.speed} km/h")

car = HybridCar("Toyota Prius")
car.accelerate(50)   # ✅ Works
car.accelerate(-10)  # ❌ Raises ValueError
