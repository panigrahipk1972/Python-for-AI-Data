def greet():
    print("Hello! Welcome to Python.")

greet()
def hello():
    print("Hello Everyone!")

hello()
def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")

def square(num):
    return num * num

result = square(6)
print(result)
def student(name, age):
    print(name, age)

student(age=20, name="John")
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Alice")

def total(*numbers):
    print(sum(numbers))

total(10, 20)
total(10, 20, 30, 40)
#Accepts any number of keyword arguments.
def student(**details):
    print(details)

student(name="John", age=20, city="Delhi")
#To modify a global variable inside a function:
x = 10
def change():
    global x
    x = 50

change()

print(x)

#Recursive function: A recursive function is a function that calls itself in order to solve a problem. It is used to break down complex problems into simpler sub-problems. A recursive function typically has a base case that stops the recursion and prevents infinite loops.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
#Anonymous (Lambda) Functions
square = lambda x: x * x
print(square(6))    
#Function Documentation (Docstrings)
def greet(name="Guest"):
    """This function greets the person with the provided name."""
    print("Hello", name) 

greet("Alice") 

#Nested Functions
def outer_function():
    print("Hello from outer function!")
    def inner_function():
        print("Hello from inner function!")
    inner_function()

outer_function()

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division

add, sub, mul, div = calculate(20, 10)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
#Write a function is_even(n) that checks if a number is even, and then use a loop to print results for numbers 1 to 10.
def is_even(n):
    return n % 2 == 0

for i in range(1, 11):
    print(f"{i} is even: {is_even(i)}")
#Try extending this by writing another function list_even_numbers(limit) that returns a list of all even numbers up to a given limit.    
def list_even_numbers(limit):
    return [i for i in range(1, limit + 1) if is_even(i)]

print(list_even_numbers(20))

def list_even_numbers(limit):
    evens = []
    for i in range(1, limit + 1):
        if is_even(i):
            evens.append(i)
    return evens

print(list_even_numbers(20))
#shorter using list comprehensions
print([i for i in range(1, 21) if is_even(i)])

#functions + list comprehensions to filter numbers in different ways.
def filter_numbers(numbers, condition):
    return [num for num in numbers if condition(num)]   
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_multiple_of_five(n):
    return n % 5 == 0

numbers = list(range(1, 21))

print("Even:", filter_numbers(numbers, is_even))
print("Odd:", filter_numbers(numbers, is_odd))
print("Multiples of 5:", filter_numbers(numbers, is_multiple_of_five))

numbers = list(range(1, 21))

# Using lambda
print("Greater than 10:", filter_numbers(numbers, lambda n: n > 10))
print("Divisible by 3:", filter_numbers(numbers, lambda n: n % 3 == 0))
#Use your filter_numbers function with a lambda to get all numbers between 1–50 that are: Multiples of 7        Greater than 20
print("Multiples of 7:", filter_numbers(numbers, lambda n: n % 7 == 0))
print("Greater than 20:", filter_numbers(numbers, lambda n: n > 20))

numbers = list(range(1, 51))
filtered_multiples_of_7 = filter_numbers(numbers, lambda n: n % 7 == 0)
print("Multiples of 7:", filtered_multiples_of_7)
print("Greater than 20:", filter_numbers(numbers, lambda n: n > 20))
#combining multiple conditions in a single lambda
print("Multiples of 7 and greater than 20:", filter_numbers(numbers, lambda n: n % 7 == 0 and n > 20))  
#passing different lambdas on the fly
print("Odd and < 15:", filter_numbers(numbers, lambda n: n % 2 != 0 and n < 15))
print("Divisible by 3 or 5:", filter_numbers(numbers, lambda n: n % 3 == 0 or n % 5 == 0))
# custom filter_numbers compares with Python’s built-in filter()
print("Custom filter (even):", filter_numbers(numbers, is_even))
print("Built-in filter (even):", list(filter(is_even, numbers)))

