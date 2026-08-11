import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

marks = [45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

study_hours = [1, 2, 3, 4, 5, 6]
student_marks = [45, 50, 55, 65, 72, 80]

fig, axes = plt.subplots(2, 2)

# Line
axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Monthly Sales")

# Bar
axes[0, 1].bar(months, sales)
axes[0, 1].set_title("Sales Comparison")

# Histogram
axes[1, 0].hist(marks, bins=5)
axes[1, 0].set_title("Marks Distribution")

# Scatter
axes[1, 1].scatter(study_hours, student_marks)
axes[1, 1].set_title("Study Hours vs Marks")

fig.tight_layout()

plt.show()