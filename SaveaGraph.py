import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

plt.plot(months, sales, marker="o")

plt.title("Company Sales - 2026")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid()

plt.savefig("monthly_sales.png")

plt.show()