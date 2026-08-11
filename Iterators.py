#An iterator is an object in Python that allows you to traverse (iterate through) elements of a collection one at a time.
#It remembers its current position and returns the next element whenever requested.
#In simple words:
#An iterator is an object that provides one value at a time from a sequence until all values are exhausted.
#Behind the scenes, Python converts the list into an iterator and repeatedly calls next() until there are no more elements.
names = ["A", "B", "C"]

iterator = iter(names)

print(iterator)

numbers = [100, 200, 300]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

#print(next(it))
numbers = [1, 2, 3]

it = iter(numbers)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

    text = "Python"

it = iter(text)

print(next(it))
print(next(it))
print(next(it))

student = {
    "Name": "Rahul",
    "Age": 20,
    "City": "Delhi"
}

it = iter(student)

print(next(it))
print(next(it))
print(next(it))
#Creating Your Own Iterator.A class becomes an iterator when it implements:_iter__()__next__()
class Counter:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

counter = Counter(5)
for num in counter:
    print(num)