import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 58, 60, 62, 65, 67, 70,
         72, 74, 75, 78, 80, 82, 85, 88, 90, 95]

plt.hist(marks, bins=10, edgecolor="black", alpha=0.7)

plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()