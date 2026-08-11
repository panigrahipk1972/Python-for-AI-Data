import matplotlib.pyplot as plt

departments = ["IT", "HR", "Sales", "Finance"]
sales = [40, 20, 25, 15]

plt.pie(
    sales,
    labels=departments,
    autopct="%1.1f%%"
)

plt.title("Department Sales Distribution")

plt.axis("equal")

plt.show()