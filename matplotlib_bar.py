import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 135, 180, 200, 175]

bars = plt.bar(months, sales)

plt.title("Company Sales - 2026")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")

for bar in bars:
    value = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        str(value),
        ha="center",
        va="bottom"
    )

plt.show()