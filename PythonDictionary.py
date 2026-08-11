student = {
    "name": "Adyasha",
    "age": 19,
    "course": "BBA"
}
print(student["name"])
print(student["age"])
print(student["course"])    

#dictionaries maintain the order in which items are inserted.
print(student)
#Dictionary elements can be changed after creation.
student["age"] = 20
print(student)
#Duplicate keys are not allowed.
student["age"] = 21
print(student)
student = {
    "name": "Rahul",
    "name": "Amit"
}

print(student)#The last value replaces the previous one.
marks = {
    "Math": 90,
    "Science": 90,
    "English": 90
}

print(marks)#this will print the dictionary as it is.
student = dict(name="Ankit", age=20)

print(student)
print(student.get("age"))
print(student.get("city", "City not found"))
del student["age"]
print(student)
student.pop("name")
print(student)
#student.popitem()
print(student)
student = {
    "name":"A",
    "age":20,
    "city":"Delhi"
}

print(len(student))
#print key and value together
for key, value in student.items():
    print(key, value)
#update
student.update({"age": 21}) 
print(student)
copy_student = student.copy()
print(copy_student)
#Nested Dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}
print(students) 
#Dictionary Comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)
#with condition
even_squared_numbers = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squared_numbers)
#Membership Operators
print("name" in student)  # True    
print("city" in student)  # False
#Mini Project: Student Management System Using Dictionary
#Objective

#Create a program that stores student information using a dictionary and allows the user to:


#Add a student
#View all students

#Search for a student
#Update student details
#Delete a student
#Exit the program
# Student Management System using Dictionary

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Student already exists!")
        else:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            students[roll] = {
                "Name": name,
                "Age": age,
                "Course": course
            }

            print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("-" * 40)
            for roll, details in students.items():
                print("Roll Number:", roll)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Course:", details["Course"])
                print("-" * 40)

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")

        if roll in students:
            print("\nStudent Found")
            print(students[roll])
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to Update: ")

        if roll in students:
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            course = input("Enter New Course: ")

            students[roll]["Name"] = name
            students[roll]["Age"] = age
            students[roll]["Course"] = course

            print("Student updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        roll = input("Enter Roll Number to Delete: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")