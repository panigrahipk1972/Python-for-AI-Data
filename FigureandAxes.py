import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

fig, ax = plt.subplots()

ax.plot(months, sales, marker="o")

ax.set_title("Company Sales - 2026")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (Units)")
ax.grid()

plt.show()