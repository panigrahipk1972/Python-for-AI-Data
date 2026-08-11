#Student Marks Analysis System (NumPy)
#Create marks data using NumPy arrays
#Calculate total, average, highest, lowest
#Find topper
#Subject-wise statistics
#Pass/fail analysis
#Grade distribution
#Learn how NumPy solves real-world data analysis problems
import numpy as np
from PIL import Image
import cv2

students = np.array([
    "Amit",
    "Priya",
    "Ravi",
    "Sneha",
    "Karan"
])

subjects = np.array([
    "Math",
    "Science",
    "English",
    "History"
])

marks = np.array([
    [78, 85, 90, 66],
    [92, 88, 76, 95],
    [56, 72, 80, 60],
    [89, 94, 91, 87],
    [70, 65, 68, 74]
])

total_marks = marks.sum(axis=1)
average_marks = marks.mean(axis=1)
highest_marks = marks.max(axis=1)
lowest_marks = marks.min(axis=1)
#Studednt wise
for i in range(len(students)):
    print(f"{students[i]}")
    print(f"Total   : {total_marks[i]}")
    print(f"Average : {average_marks[i]:.2f}")
    print(f"Highest : {highest_marks[i]}")
    print(f"Lowest  : {lowest_marks[i]}")
    print("-" * 30)
# Topper
topper_index = total_marks.argmax()
topper_name = students[topper_index]
print(f"Topper: {topper_name} with total marks {total_marks[topper_index]}")
# Subject-wise
subject_total = marks.sum(axis=0)
subject_average = marks.mean(axis=0)
subject_highest = marks.max(axis=0)
subject_lowest = marks.min(axis=0)
for i in range(len(subjects)):
    print(f"{subjects[i]}")
    print(f"Total   : {subject_total[i]}")
    print(f"Average : {subject_average[i]:.2f}")
    print(f"Highest : {subject_highest[i]}")
    print(f"Lowest  : {subject_lowest[i]}")
    print("-"*30)
pass_fail = np.where(average_marks >= 40, "Pass", "Fail")
for i in range(len(students)):
    print(f"{students[i]} : {pass_fail[i]}")

def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"
grades = [grade(avg) for avg in average_marks]


#Represent images as NumPy arrays
#Crop images
#Resize (basic concepts)
#Flip horizontally/vertically
#Rotate
#Convert to grayscale
#Adjust brightness and contrast
#Apply simple filters
# Load image using PIL and convert to NumPy array
image =cv2.imread("Capture.jpg")
print(image.shape)
print(image.dtype)

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

crop = image[100:400, 200:600]

cv2.imshow("Crop", crop)
horizontal = np.fliplr(image)
vertical = np.flipud(image)

rotate90 = np.rot90(image)

rotate180 = np.rot90(image,2)

rotate270 = np.rot90(image,3)

bright = np.clip(image + 50,0,255).astype(np.uint8)

dark = np.clip(image - 50,0,255).astype(np.uint8)

contrast = np.clip(image*1.4,0,255).astype(np.uint8)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
negative = 255-image
blur = cv2.blur(image,(5,5))
edges = cv2.Canny(image,100,200)
cv2.imwrite("edited.jpg",bright)