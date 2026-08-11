#create a class with object oriented programming
class Car:
    def __init__(self, make, model, year):#Constructor of the class
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")
#Create a Object and Print the Information
my_car = Car("Toyota", "Camry", 2020)
my_car.display_info()
#Use a static method to calculate the area of a rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height


rect = Rectangle(5, 3)
print("Area of rectangle:", Rectangle.area(5, 3))
#Encapsulation: Create a class with private attributes and provide getter and setter methods.
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.") 
   #Create a a object and test the methods
account = BankAccount("123456789", 1000)    
print("Account Number:", account.get_account_number())
print("Initial Balance:", account.get_balance())    
account.deposit(500)
account.withdraw(200)   
print("Final Balance:", account.get_balance())
 #Tell me the difference between public,private and protected attributes in python with example
 # In Python, attributes can be classified as public, private, or protected based on their accessibility and naming conventions. Here's a brief explanation of each type along with examples:      
 # 1. Public Attributes:
# Public attributes are accessible from anywhere, both inside and outside the class. They are defined without any special prefix. By default, all attributes in Python are public unless specified otherwise.
class PublicExample:
    def __init__(self, value):
        self.value = value  # Public attribute
# Example usage:
public_obj = PublicExample(10)      
print(public_obj.value)  # Accessible from outside the class
#private Attributes:
# Private attributes are intended to be accessed only within the class. They are defined with a double underscore prefix (__). Python uses name mangling to make it harder to access private attributes from outside the class, but they can still be accessed if needed.
class PrivateExample:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def get_value(self):
        return self.__value  # Accessing private attribute through a method
    # Example usage:
private_obj = PrivateExample(20)
print(private_obj.get_value())  # Accessing private attribute through a method
# Attempting to access the private attribute directly will raise an AttributeError
# print(private_obj.__value)  # This will raise an AttributeError
# Protected Attributes:
# Protected attributes are intended to be accessed within the class and its subclasses. They are defined with a single underscore prefix (_). While they can still be accessed from outside the class, it is generally discouraged.
class ProtectedExample:
    def __init__(self, value):
        self._value = value  # Protected attribute

    def get_value(self):
        return self._value  # Accessing protected attribute through a method        
# Example usage:
protected_obj = ProtectedExample(30)
print(protected_obj.get_value())  # Accessing protected attribute through a method  
# Attempting to access the protected attribute directly is possible but discouraged
print(protected_obj._value)  # Accessible but discouraged   
#Inheritance: Create a base class and a derived class to demonstrate inheritance.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
    # Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"    
    # Example usage:
dog = Dog("Buddy")      
print(dog.speak())
#Polymorphism: Create a base class and multiple derived classes to demonstrate polymorphism.
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    # Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  
# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())
#Types of Inheritance in Python:
# 1. Single Inheritance: A derived class inherits from a single base class.
#example:
class Parent:
    def greet(self):
        return "Hello from Parent class!"
# Derived class
class Child(Parent):    
    def greet(self):
        return "Hello from Child class!"
# Example usage:
child = Child() 
print(child.greet())  # Output: Hello from Child class!
#2. Multiple Inheritance: A derived class inherits from multiple base classes.
# example:
class Base1:        
    def greet(self):
        return "Hello from Base1 class!"
        
class Base2:
    def greet(self):
        return "Hello from Base2 class!"

class Child(Base1, Base2):
    def greet(self):
        return "Hello from Child class!"
# Example usage:
child = Child() 
print(child.greet())  # Output: Hello from Child class!
#what about other two greet methods from Base1 and Base2? How can we access them?
#In Python, when a derived class inherits from multiple base classes, the 
# method resolution order (MRO)
#determines which method is called when there are methods with the same name in the base classes.
# By default, the method from the first base class listed in the inheritance will be called.
#However, you can explicitly call methods from specific base classes using their class names.
#However, if you want to access the greet methods from Base1 and Base2, 
# you can do so by explicitly calling them using their class names. 
# Here's how you can access the greet methods from Base1 and Base2:
print(Base1.greet(child))  # Output: Hello from Base1 class!
print(Base2.greet(child))  # Output: Hello from Base2 class!
#Multi level Inheritance: A derived class inherits from a base class,
# which in turn inherits from another base class.
#example:
class Grandparent:
    def greet(self):
        return "Hello from Grandparent class!"  
# Derived class
class Parent(Grandparent):
    def greet(self):
        return "Hello from Parent class!"
# Derived class
class Child(Parent):
    def greet(self):
        return "Hello from Child class!"    
# Example usage:
child = Child()     
print(child.greet())  # Output: Hello from Child class!
#How to call the greet methods from Parent and Grandparent classes?
#To call the greet methods from the Parent and Grandparent classes,you can use the class
# name along with the instance of the derived class. Here's how you can do it:
print(Parent.greet(child))  # Output: Hello from Parent class!
print(Grandparent.greet(child))  # Output: Hello from Grandparent class!    
#Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
#example:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
# Derived class for Dog
class Dog(Animal):
    def speak(self):
        return "Woof!"
# Derived class for Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"      
# Example usage:
dog = Dog() 
print(dog.speak())  # Output: Woof!
cat = Cat()
print(cat.speak())  # Output: Meow!
#Hybrid Inheritance: A combination of two or more types of inheritance.
#example:
class Vehicle:
    def start(self):
        return "Vehicle started."
class Car(Vehicle):
    def start(self):
        return "Car started." 
# Derived class for Boat
class Boat(Vehicle):
    def start(self):
        return "Boat started."  
# Derived class for AmphibiousVehicle (inherits from both Car and Boat)
class AmphibiousVehicle(Car, Boat):
    def start(self):
        return "Amphibious Vehicle started."
# Example usage:
amphibious_vehicle = AmphibiousVehicle()    
print(amphibious_vehicle.start())  # Output: Amphibious Vehicle started.
#Give an example of Hybrid Car like Car runs on CNG and Pterol and also runs on electricitythrough 
#Hybrid Inheritance.
#example:
class Engine:
    def start(self):
        return "Engine started."    
# Derived class for CNG Engine
class CNGEngine(Engine):
    def start(self):
        return "CNG Engine started."    
# Derived class for Petrol Engine       
class PetrolEngine(Engine):
    def start(self):
        return "Petrol Engine started."    
# Derived class for Electric Engine
class ElectricEngine(Engine):
    def start(self):
        return "Electric Engine started."   
# Derived class for Hybrid Car (inherits from CNGEngine, PetrolEngine, and ElectricEngine)
class HybridCar(CNGEngine, PetrolEngine, ElectricEngine):
    def start(self):
        return "Hybrid Car started with multiple engines."  
# Example usage:
hybrid_car = HybridCar()    
print(hybrid_car.start())  # Output: Hybrid Car started with multiple engines.  
#Petrol Engine started.
print(PetrolEngine.start(hybrid_car))  # Output: Petrol Engine started.
#CNG Engine started.
print(CNGEngine.start(hybrid_car))  # Output: CNG Engine started.   
#Electric Engine started.
print(ElectricEngine.start(hybrid_car))  # Output: Electric Engine started.
#Give an example method that decides which engine to use automatically
def decide_engine(hybrid_car, engine_type):
    if engine_type == "CNG":
        return CNGEngine.start(hybrid_car)
    elif engine_type == "Petrol":
        return PetrolEngine.start(hybrid_car)
    elif engine_type == "Electric":
        return ElectricEngine.start(hybrid_car)
    else:
        return "Invalid engine type."
    # Example usage:
print(decide_engine(hybrid_car, "CNG"))      # Output: CNG Engine started.
print(decide_engine(hybrid_car, "Petrol"))   # Output: Petrol Engine started.
print(decide_engine(hybrid_car, "Electric")) # Output: Electric Engine started.
#Expand this into a full demo where you can refuel petrol, refill CNG, recharge battery, and then see how the car decides which engine to start?
class Engine:
    def start(self):
        return "Generic Engine started."

# Petrol Engine
class PetrolEngine(Engine):
    def __init__(self, fuel=0):
        self.__fuel = fuel   # private attribute

    def refuel(self, amount):
        self.__fuel += amount

    def has_fuel(self):
        return self.__fuel > 0

    def start(self):
        if self.__fuel > 0:
            self.__fuel -= 1
            return "Petrol Engine started."
        return "No petrol available!"

# CNG Engine
class CNGEngine(Engine):
    def __init__(self, fuel=0):
        self.__fuel = fuel

    def refill(self, amount):
        self.__fuel += amount

    def has_fuel(self):
        return self.__fuel > 0

    def start(self):
        if self.__fuel > 0:
            self.__fuel -= 1
            return "CNG Engine started."
        return "No CNG available!"

# Electric Engine
class ElectricEngine(Engine):
    def __init__(self, battery=0):
        self.__battery = battery

    def recharge(self, amount):
        self.__battery += amount

    def has_power(self):
        return self.__battery > 0

    def start(self):
        if self.__battery > 0:
            self.__battery -= 1
            return "Electric Engine started."
        return "Battery empty!"

# Hybrid Car
class HybridCar(PetrolEngine, CNGEngine, ElectricEngine):
    def __init__(self, petrol=0, cng=0, battery=0):
        PetrolEngine.__init__(self, petrol)
        CNGEngine.__init__(self, cng)
        ElectricEngine.__init__(self, battery)

    def decide_engine(self):
        if self.has_power():
            return ElectricEngine.start(self)
        elif self.has_fuel():  # Petrol check
            return PetrolEngine.start(self)
        elif CNGEngine.has_fuel(self):
            return CNGEngine.start(self)
        else:
            return "No fuel or battery available!"

# Demo
car = HybridCar(petrol=2, cng=1, battery=3)

print(car.decide_engine())  # Electric Engine started.
print(car.decide_engine())  # Electric Engine started.
print(car.decide_engine())  # Electric Engine started.
print(car.decide_engine())  # Petrol Engine started.
print(car.decide_engine())  # Petrol Engine started.
print(car.decide_engine())  # CNG Engine started.
print(car.decide_engine())  # No fuel or battery available!
#Please Explain Operator Overloading
#Operator overloading allows you to define how operators behave 
# for objects of a class. In Python, you can overload operators by 
# defining special methods (also known as "dunder" methods) in your class.
# For example, you can overload the addition operator (+) for a custom class 
# by implementing the __add__ method. Here's a simple example:
#example of operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"({self.x}, {self.y})"  
    # Example usage:
p1 = Point(2, 3)        
p2 = Point(4, 5)
result = p1 + p2  # This will call the __add__ method

print(result)  # Output: (6, 8) 
#Example of operator overloading for comparison operators
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return NotImplemented       
# Example usage:
rect1 = Rectangle(4, 5)  # Area = 20
rect2 = Rectangle(3, 6)  # Area = 18
print(rect1 < rect2)  # Output: False
print(rect1 == rect2)  # Output: False
#Example of operator overloading for string representation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"  
    # Example usage:    
person = Person("Alice", 30)
print(person)  # Output: Person(Name: Alice, Age: 30)
#Example of operator overloading for multiplication operator
class Vector:   
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __str__(self):
        return f"Vector({self.x}, {self.y})"  
    # Example usage:
vector = Vector(2, 3)
scaled_vector = vector * 3  # This will call the __mul__ method 
print(scaled_vector)  # Output: Vector(6, 9)
#Example of operator overloading for indexing operator
class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def __len__(self):
        return len(self.elements)  
    # Example usage:
my_list = CustomList([1, 2, 3, 4, 5])
print(my_list[0])  # Output: 1
my_list[0] = 10
print(my_list[0])  # Output: 10
print(len(my_list))  # Output: 5
#Example of operator overloading for call operator
class CallableExample:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        return f"Callable says: {self.message}"  
    # Example usage:
callable_obj = CallableExample("Hello, world!")
print(callable_obj())  # Output: Callable says: Hello, world!
#Example of operator overloading for negation operator
class NegationExample:  
    def __init__(self, value):
        self.value = value

    def __neg__(self):
        return NegationExample(-self.value)

    def __str__(self):
        return f"NegationExample({self.value})"  
    # Example usage:
neg_obj = NegationExample(5)
print(-neg_obj)  # Output: NegationExample(-5)  
#Example of operator overloading for in-place addition operator
class InPlaceAdditionExample:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        if isinstance(other, InPlaceAdditionExample):
            self.value += other.value
            return self
        return NotImplemented

    def __str__(self):
        return f"InPlaceAdditionExample({self.value})"  
    # Example usage:        
obj1 = InPlaceAdditionExample(10)
obj2 = InPlaceAdditionExample(5)
obj1 += obj2
print(obj1)  # Output: InPlaceAdditionExample(15)
#Example of operator overloading for power operator
class PowerExample: 
    def __init__(self, value):
        self.value = value

    def __pow__(self, exponent):
        return PowerExample(self.value ** exponent)

    def __str__(self):
        return f"PowerExample({self.value})"  
    # Example usage:
power_obj = PowerExample(2)
result = power_obj ** 3  # This will call the __pow__ method
print(result)  # Output: PowerExample(8)    
#Example of operator overloading for modulo operator
class ModuloExample:
    def __init__(self, value):
        self.value = value

    def __mod__(self, other):
        if isinstance(other, ModuloExample):
            return ModuloExample(self.value % other.value)
        return NotImplemented

    def __str__(self):
        return f"ModuloExample({self.value})"  
    # Example usage:
modulo_obj1 = ModuloExample(10)
modulo_obj2 = ModuloExample(3)
result = modulo_obj1 % modulo_obj2
print(result)  # Output: ModuloExample(1)
#Example of operator overloading for bitwise AND operator
class BitwiseAndExample:    
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        if isinstance(other, BitwiseAndExample):
            return BitwiseAndExample(self.value & other.value)
        return NotImplemented

    def __str__(self):
        return f"BitwiseAndExample({self.value})"  
    # Example usage:
bitwise_and_obj1 = BitwiseAndExample(5)
bitwise_and_obj2 = BitwiseAndExample(3)
result = bitwise_and_obj1 & bitwise_and_obj2
print(result)  # Output: BitwiseAndExample(1)       
#Example of operator overloading for bitwise OR operator
class BitwiseOrExample: 
    def __init__(self, value):
        self.value = value

    def __or__(self, other):
        if isinstance(other, BitwiseOrExample):
            return BitwiseOrExample(self.value | other.value)
        return NotImplemented

    def __str__(self):
        return f"BitwiseOrExample({self.value})"  
    # Example usage:        
bitwise_or_obj1 = BitwiseOrExample(5)
bitwise_or_obj2 = BitwiseOrExample(3)
result = bitwise_or_obj1 | bitwise_or_obj2  
print(result)  # Output: BitwiseOrExample(7)    
#Example of operator overloading for bitwise XOR operator
class BitwiseXorExample:    
    def __init__(self, value):
        self.value = value

    def __xor__(self, other):
        if isinstance(other, BitwiseXorExample):
            return BitwiseXorExample(self.value ^ other.value)
        return NotImplemented

    def __str__(self):
        return f"BitwiseXorExample({self.value})"  
    # Example usage:    
bitwise_xor_obj1 = BitwiseXorExample(5)
bitwise_xor_obj2 = BitwiseXorExample(3)
result = bitwise_xor_obj1 ^ bitwise_xor_obj2
print(result)  # Output: BitwiseXorExample(6)
#Example of Super() function in Python
#The `super()` function in Python is used to call methods from a 
#parent class (also known as a superclass) in a derived class (subclass).
#It allows you to access and invoke methods from the parent class without explicitly naming it, 
# which is especially useful in multiple inheritance scenarios.
#Example of using super() in single inheritance:
class Parent:
    def greet(self):
        return "Hello from Parent class!"   
    # Derived class
class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()  # Call the greet method from Parent class
        return f"{parent_greeting} Hello from Child class!"  
    # Example usage:
child = Child()
print(child.greet())  # Output: Hello from Parent class! Hello from Child class!
#Example of using super() in multiple inheritance:
class Base1:
    def greet(self):
        return "Hello from Base1 class!"    
class Base2:
    def greet(self):
        return "Hello from Base2 class!"    
class Child(Base1, Base2):
    def greet(self):
        base1_greeting = super().greet()  # Call the greet method from Base1 class
        return f"{base1_greeting} Hello from Child class!"  
    # Example usage:    
child = Child()
print(child.greet())  # Output: Hello from Base1 class! Hello from Child class
#Abstraction in Python is a fundamental concept in object-oriented programming (OOP) 
# that focuses on exposing only the essential features of an object while hiding the 
# unnecessary details. It allows you to create abstract classes and methods that define 
# a blueprint for derived classes, ensuring that they implement specific functionality 
# without revealing the implementation details.
#Example of Abstraction using Abstract Base Classes (ABC):
from abc import ABC, abstractmethod
# Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    # Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
# Derived class for Rectangle
class Rectangle(Shape): 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
# Example usage:
circle = Circle(5)  
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())  
rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())
#Function Overloading in Python:
#Function overloading is a feature in some programming languages that allows 
# you to define multiple functions with
# the same name but different parameter lists (different number or types of parameters).
# However, Python does not support traditional function overloading like some other languages   
# Instead, Python allows you to achieve similar functionality using default arguments,
#variable-length arguments, or by checking the types of arguments within a single function.
#Example of Function Overloading using Default Arguments:
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")    
#Function Overriding in Python:  
# Function overriding is a feature in object-oriented programming (OOP) 
# that allows a subclass (derived class) to provide a specific implementation 
# of a method that is already defined in its superclass (base class).
# When a method in the subclass has the same name, return type, 
# and parameters as a method in the superclass, the subclass's method overrides 
# the superclass's method. This allows for polymorphism, where the behavior of an 
# object can change based on its actual type at runtime.      
#Example of Function Overriding:
class Animal:
    def speak(self):
        return "Animal makes a sound."

class Dog(Animal):
    def speak(self):
        return "Dog barks."

class Cat(Animal):
    def speak(self):
        return "Cat meows."     
# Example usage:
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # Output: Animal makes a sound.
print(dog.speak())     # Output: Dog barks.
print(cat.speak())     # Output: Cat meows.
#Build a contact manager app through object oriented programming in python with features
# like add contact, view contacts, search contact, update contact, delete contact and 
# exit the program.
#Example of a simple Contact Manager App using Object-Oriented Programming in Python:
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
# Contact Manager Class
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Contact not found.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.") 
        # Example usage of the Contact Manager App
if __name__ == "__main__":  
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            manager.search_contact(name)
        elif choice == '4':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            manager.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '5':
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")      
    