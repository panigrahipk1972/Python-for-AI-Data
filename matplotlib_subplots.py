import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

marks = [45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

departments = ["IT", "HR", "Sales", "Finance"]
department_sales = [40, 20, 25, 15]

study_hours = [1, 2, 3, 4, 5, 6]
student_marks = [45, 50, 55, 65, 72, 80]


# Chart 1 — Line
plt.subplot(2, 2, 1)

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")


# Chart 2 — Bar
plt.subplot(2, 2, 2)

plt.bar(months, sales)

plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")


# Chart 3 — Histogram
plt.subplot(2, 2, 3)

plt.hist(marks, bins=5)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")


# Chart 4 — Scatter
plt.subplot(2, 2, 4)

plt.scatter(study_hours, student_marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")


plt.tight_layout()

plt.show()