import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

plt.barh(months, sales)

plt.title("Company Sales - 2026")
plt.xlabel("Sales (Units)")
plt.ylabel("Month")

plt.show()