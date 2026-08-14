import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data_100.csv")

print(df.head())

category_sales = df.groupby("Category")["Quantity"].sum()
sns.barplot(data=df, x="Category", y="Quantity")
plt.title("Quantity Sold by Category")
plt.show()
category_sales = (
    df.groupby("Category", as_index=False)["Quantity"]
      .sum()
)

sns.barplot(
    data=category_sales,
    x="Category",
    y="Quantity"
)

plt.title("Total Quantity Sold by Category")
plt.xlabel("Category")
plt.ylabel("Total Quantity")

plt.show()
#Create a Seaborn bar plot showing the average Rating for each Category.
avg_rating = df.groupby("Category")["Rating"].mean()
sns.barplot(data=df, x="Category", y="Rating")

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.show()

sns.countplot(data=df, x="Category")

plt.title("Number of Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.show()

sns.countplot(data=df, x="Gender")

plt.title("Number of Orders by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Orders")

plt.show()

sns.countplot(
    data=df,
    x="Category",
    hue="Gender"
)

plt.title("Category-wise Orders by Gender")
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.show()

sns.histplot(data=df, x="UnitPrice", bins=20, kde=True)

plt.title("Distribution of Unit Price")
plt.xlabel("Unit Price")
plt.ylabel("Number of Orders")

plt.show()

sns.boxplot(data=df, y="UnitPrice")

plt.title("Distribution of Unit Price")
plt.ylabel("Unit Price")

plt.show()

sns.boxplot(
    data=df,
    x="Category",
    y="UnitPrice"
)

plt.title("Unit Price Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Unit Price")

plt.show()

sns.boxplot(data=df, x="Category", y="UnitPrice")

plt.title("Unit Price by Category")
plt.show()

sns.scatterplot(
    data=df,
    x="Quantity",
    y="UnitPrice"
)

plt.title("Quantity vs Unit Price")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")

plt.show()

sns.scatterplot(
    data=df,
    x="Quantity",
    y="UnitPrice",
    hue="Category"
)

plt.title("Quantity vs Unit Price by Category")
plt.show()

df["Date"] = pd.to_datetime(df["Date"])
daily_sales = (
    df.groupby("Date", as_index=False)["Quantity"]
      .sum()
)
sns.lineplot(
    data=daily_sales,
    x="Date",
    y="Quantity"
)

plt.title("Daily Sales Quantity")
plt.xlabel("Date")
plt.ylabel("Quantity Sold")

plt.show()

corr = df[["Quantity", "UnitPrice", "Rating"]].corr()

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f"
)

plt.title("Sales Data Correlation Heatmap")
plt.show()