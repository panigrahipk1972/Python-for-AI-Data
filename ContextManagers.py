#Context Managers in Python
#Can be used to manage resources such as file streams,
# network connections, and database connections. They ensure that resources are properly acquired and released, 
# even in the presence of exceptions. The most common way to create a context manager
#  is by using the `with` statement along with the `__enter__` and `__exit__` methods.
#Example of a simple context manager that manages a file resource:
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

#Usage of the FileManager context manager
with FileManager('example.txt', 'w') as f:
    f.write('Hello, World!')
#Second Example
class Library:

    def borrow_book(self):
        print("📚 Book borrowed.")

    def return_book(self):
        print("📚 Book returned.")


library = Library()

library.borrow_book()

print("📖 Reading the book...")

# Uncomment the next line to simulate an error
#print(10 / 0)

library.return_book()

#With Context Manager
class Library:

    def __enter__(self):
        print("📚 Book borrowed.")
        return self

    def read_book(self):
        print("📖 Reading the book...")

    def __exit__(self, exc_type, exc_value, traceback):
        print("📚 Book returned.")


with Library() as book:
    book.read_book()

    # Uncomment this line to simulate an error
    #print(10 / 0)
