import numpy as np

marks = np.array([80,90,75,95])

print(marks)
print(type(marks))
print(marks.size)
print(marks.ndim)
print(marks + 5)


data = np.array([
    [80,90,85],
    [70,75,80]
])

print(data)

arr = np.empty((2,3))

print(arr)

arr = np.full((3,4), 7)

print(arr)

a = np.ones((1000, 1000))
del a

b = np.empty((5,5))
print(b)
import numpy as np

arr = np.arange(5)

print(arr)
arr = np.arange(2, 20, 2)

print(arr)

arr = np.arange(10, 0, -1)

print(arr)

arr = np.arange(0, 1, 0.2)

print(arr)

arr = np.linspace(1, 10, 5)

print(arr)

import numpy as np

arr = np.identity(3)

print(arr)

arr = np.identity(4, dtype=int)

print(arr)

arr = np.eye(3, 5)

print(arr)

arr = np.eye(4, k=1)

print(arr)

arr = np.eye(5, k=-2)
print(arr)

arr = np.arange(12)
arr.reshape(3,-1)
print(arr)
arr.reshape(-1,2)
print(arr)
arr=np.array([[1,2],[3,4]])
x=arr.flatten()
print(x)
x[0]=100
print(x)
x=arr.ravel()
print(x)
arr=np.arange(20)
print(arr.reshape(4,-1))
arr=np.arange(15)

print(arr.reshape(5,3))
arr=np.arange(15)

#print(arr.reshape(4,4))
arr=np.array([[10,20],[30,40]])

x=arr.ravel()

x[1]=99

print(arr)
arr = np.arange(24)

print(arr.reshape(2, 3, 4))
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arr[:,1])
arr=np.array([10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[::-1])
print(arr[::2])
#write a two dimansional array and print the first two rows and last two columns
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print(arr[:2, -2:])
arr=np.array([10,20,30,40,50])

print(arr[1:5:2])#what does it means
arr=np.array([5,10,15,20,25])

print(arr[::-1])
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(arr[:,2])

arr = np.array([10,20,30,40,50])

print(arr[[0,2,4]])

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(arr[[0,2],[1,2]])
arr = np.array([10,20,30,40,50])
print(arr > 25)
print(arr[arr > 25])
arr = np.array([10,20,30,40])

print(arr[[3,1]])
arr = np.array([2,4,6,8])

print(arr[arr % 4 == 0])

arr = np.array([[10,20],
                [30,40]])

print(arr[[0,1],[1,0]])

marks = np.array([70,80,90,60])

print(marks + 5)

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([10, 20, 30])

print(A + B)

A = np.array([[10],
              [20]])

B = np.array([[1, 2, 3]])

print(A + B)

a = np.random.rand()
print(a)
a = np.random.rand(2,3)
print(a)
a = np.random.randint(1,10,5)
print(a)
a = np.random.randint(10,20,(2,3))
print(a)
a = np.random.randn(5)
print(a)

a = np.random.choice([10, 20, 30, 40])
print(a)
A = np.array([[2, 3],
              [1, 4]])

print(np.linalg.det(A))
#

