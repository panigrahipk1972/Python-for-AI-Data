print("Hello, Fullstack AI! \n ")
print("Welcome to the world of AI and programming.")
print("Here's a simple recipe for making bread:\n1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print("Enjoy your homemade bread!")
# Assigning values
name = "Pradeep"
age = 25
is_developer = True

print(name, age, is_developer)
x = 10
print(type(x))

x = "Hello"
print(type(x))
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
x = y = z = 100

print(x)
print(y)
print(z)
a = 10
b = a

print(a)
print(b)
print(id(a))
print(id(b))

def demo():
    x = 10
    print(x)

demo()
x = 10

def change():
    global x
    x = 50

change()

print(x)
x = 100

del x
x=10
age = 20

print(type(age))
# A List is an ordered, mutable (changeable) collection that can 
#store different data types. Lists are one of the most versatile data structures in Python.
fruits = ["Apple", "Banana", "Orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])
numbers = [10,20,30,40,50]

print(numbers[1:4])
fruits[1] = "Mango"
print(fruits)
fruits.append("Grapes")
print(fruits)   
fruits.insert(1,"Kiwi")
print(fruits)
fruits.remove("Kiwi") 
print(fruits)
fruits.pop(2)
print(fruits)   
fruits.extend(["Pineapple","Papaya"])
print(fruits)
len(numbers)
max(numbers)
min(numbers)
sum(numbers)

numbers.sort()
numbers.reverse()
#A Tuple is an ordered but immutable (unchangeable) collection.
#Ordered
#Immutable
#Allows duplicates
#Supports indexing
#Faster than lists for read-only data
colors = ("Red","Green","Blue")

print(colors)
print(colors[0])
print(colors[-1])
numbers = (10,20,30,40,50)

print(numbers[1:4])
#colors[1] = "Yellow"
numbers = (1,2,2,3,2)

print(numbers.count(2))
#A Set is an unordered, mutable collection of unique elements. It automatically removes duplicate values.
unique_numbers = {1, 2, 2, 3, 2}
print(unique_numbers)
numbers = {1,2,2,3,3,4}

print(numbers)
numbers = {1,2,3}

numbers.add(4)

print(numbers)
numbers.update([5,6,7])
print(numbers)
numbers.remove(2)
print(numbers)
numbers.discard(3)  
print(numbers)
numbers.discard(10)     
print(numbers)
numbers.pop()
print(numbers)
A = {1,2,3}
B = {3,4,5}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
numbers = {1,2,3,4}

print(3 in numbers)
