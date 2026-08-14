import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data_100.csv")

print(df.head())

#Question 1 — Category Performance
#Which category has the highest average customer rating?
sns.barplot(
    data=df,
    x="Category",
    y="Rating"
)

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.show()

#Question 2 — Gender Distribution
#How many orders came from each gender?
sns.countplot(
    data=df,
    x="Gender"
)

plt.title("Orders by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Orders")

plt.show()

#Question 3 — Price Distribution
#How are product prices distributed?
sns.histplot(
    data=df,
    x="UnitPrice",
    bins=20,
    kde=True
)

plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Number of Orders")

plt.show()

#Question 4 — Find Possible Outliers

#Are there unusual product prices?
sns.boxplot(
    data=df,
    y="UnitPrice"
)

plt.title("Unit Price — Outlier Detection")
plt.ylabel("Unit Price")

plt.show()
#Question 5 — Relationship
#Is there any visible relationship between Quantity and UnitPrice?
sns.scatterplot(
    data=df,
    x="Quantity",
    y="UnitPrice",
    hue="Category"
)

plt.title("Quantity vs Unit Price by Category")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")

plt.show()

#Which city has the highest average customer rating?
sns.barplot(
    data=df,
    x="City",
    y="Rating"
)

plt.title("Average Rating by City")
plt.xlabel("City")
plt.ylabel("Average Rating")

plt.show()