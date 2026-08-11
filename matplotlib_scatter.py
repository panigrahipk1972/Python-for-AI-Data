import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 55, 65, 72, 80]

plt.scatter(study_hours, marks, alpha=0.7)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()