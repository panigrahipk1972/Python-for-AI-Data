#Generators in Python
#A generator in Python is a special type of function that produces values one at a time, 
#Only when needed, instead of creating and storing all values in memory at once.
#Unlike a normal function, which returns a value using return and then stops, 
#A generator uses the yield keyword to return values one by one and remembers its state between calls.

def numbers():
    yield 1
    yield 2
    yield 3
print(numbers())
def numbers():
    yield 1
    yield 2
    yield 3

g = numbers()

print(next(g))
print(next(g))
print(next(g))
#Instead of repeatedly calling next(), use a loop:
def fruits():
    yield "Apple"
    yield "Banana"
    yield "Mango"

for fruit in fruits():
    print(fruit)
#Generator Expression
squares = [x*x for x in range(5)]

print(squares)
#Generator Expression
squares = (x*x for x in range(5))
for value in squares:
 print(value)
#Infinite Generator-Generators can produce an unlimited sequence.
def infinite():
    n = 1
    while True:
        yield n
        n += 1

# Create the generator once
g = infinite()

for i in range(5):
    print(next(g))

#Fibonacci Generator
def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)
#Reading a Large File
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

for line in read_file("PythonNotes.txt"):
    print(line)