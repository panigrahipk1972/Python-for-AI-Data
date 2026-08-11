import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# MATPLOTLIB + PANDAS SALES ANALYSIS
# ============================================================

# 1. Read the dataset
df = pd.read_csv("sales_data_100.csv")

print("========== ORIGINAL DATA ==========")
print(df.head())


# ============================================================
# 2. Create Sales column
# Sales = Quantity × UnitPrice
# ============================================================

df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("\n========== DATA WITH SALES ==========")
print(df.head())


# ============================================================
# 3. Convert Date column to datetime
# ============================================================

df["Date"] = pd.to_datetime(df["Date"])


# ============================================================
# 4. SALES BY CITY
# ============================================================

city_sales = df.groupby("City")["Sales"].sum()

print("\n========== SALES BY CITY ==========")
print(city_sales)

plt.figure()

plt.bar(city_sales.index, city_sales.values)

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 5. SALES BY CATEGORY
# ============================================================

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

plt.figure()

plt.bar(category_sales.index, category_sales.values)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()


# ============================================================
# 6. DAILY SALES TREND
# ============================================================

daily_sales = df.groupby("Date")["Sales"].sum()

print("\n========== DAILY SALES ==========")
print(daily_sales.head())

plt.figure()

plt.plot(
    daily_sales.index,
    daily_sales.values,
    marker="o"
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.grid()

plt.tight_layout()
plt.show()


# ============================================================
# 7. SALES BY PRODUCT
# ============================================================

product_sales = df.groupby("Product")["Sales"].sum()

print("\n========== SALES BY PRODUCT ==========")
print(product_sales)

plt.figure()

plt.barh(
    product_sales.index,
    product_sales.values
)

plt.title("Total Sales by Product")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.show()


# ============================================================
# 8. SALES DISTRIBUTION
# ============================================================

plt.figure()

plt.hist(df["Sales"], bins=10)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()


# ============================================================
# END
# ============================================================

print("\n========== ANALYSIS COMPLETE ==========")