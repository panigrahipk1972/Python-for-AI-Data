import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.shape)
#How many passengers survived vs did not survive?
sns.countplot(data=df, x="survived")

plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")

plt.show()
#Step 1 — Count survivors
print(df["survived"].value_counts())
#Step 2 — Let Pandas calculate the percentage
print(df["survived"].value_counts(normalize=True) * 100)
#normalize=True tells Pandas "Don't give me the counts; give me the proportion."Then * 100 converts the proportion into a percentage.
#Survival by Gender — Male vs Female
sns.countplot(
    data=df,
    x="survived",
    hue="sex"
)

plt.title("Survival by Gender")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")

plt.show()

#What percentage of males vs females survived?
print("Percentage of males who survived:")
print(df[df['sex'] == 'male']['survived'].value_counts(normalize=True) * 100)

print("Percentage of females who survived:")
print(df[df['sex'] == 'female']['survived'].value_counts(normalize=True) * 100)

print("Percentage of survivors by gender:")
print(df.groupby("sex")["survived"].mean() * 100)

survival_by_gender = (
    df.groupby("sex")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(survival_by_gender)

#Did passenger class affect survival?
survival_by_class = (
    df.groupby("pclass")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(survival_by_class)
sns.barplot(
    data=df,
    x="pclass",
    y="survived"
)

plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.show()

survival_by_class = (
    df.groupby("pclass")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(survival_by_class)
#What happens when we combine both factors?Gender + Passenger Class + Survival
sns.barplot(
    data=df,
    x="pclass",
    y="survived",
    hue="sex"
)

plt.title("Survival Rate by Class and Gender")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.show()
print(df.groupby(["pclass", "sex"])["survived"].mean().mul(100).round(2))

#Question 3 — Did Age Affect Survival?
#Compare age of survivors vs non-survivors
sns.boxplot(
    data=df,
    x="survived",
    y="age"
)

plt.title("Age Distribution by Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.show()
#Let's also see the age distribution
sns.histplot(
    data=df,
    x="age",
    hue="survived",
    bins=20,
    kde=True
)

plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.show()
#What percentage of 20–30-year-olds survived?
print("Percentage of 20–30-year-olds who survived:")
print(df[(df['age'] >= 20) & (df['age'] <= 30)]['survived'].value_counts(normalize=True) * 100)
#Age Group vs Survival
#Create age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 30, 50, 80],
    labels=["Child", "Teen", "Young Adult", "Adult", "Senior"]
)
#Calculate survival rate
age_survival = (
    df.groupby("age_group", observed=True)["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(age_survival)
#Visualize it
sns.barplot(
    data=df,
    x="age_group",
    y="survived"
)

plt.title("Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate")

plt.show()
#Next: Age + Gender
#Plot Age Group + Gender
sns.barplot(
    data=df,
    x="age_group",
    y="survived",
    hue="sex"
)

plt.title("Survival Rate by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate")

plt.show()
#Let's get the exact numbers
age_gender_survival = (
    df.groupby(["age_group", "sex"], observed=True)["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(age_gender_survival)
print(df.groupby(["age_group", "sex"], observed=True)["survived"].agg(
    ["count", "sum"]
))
#Next Question: Did Fare Affect Survival?
#Step 1 — Fare distribution
sns.histplot(
    data=df,
    x="fare",
    bins=30,
    kde=True
)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")

plt.show()
#Step 2 — Fare vs Survival
sns.boxplot(
    data=df,
    x="survived",
    y="fare"
)

plt.title("Fare Distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Fare")

plt.show()

print(df.groupby("pclass")["fare"].agg(
    ["mean", "median"]
).round(2))

sns.boxplot(
    data=df,
    x="pclass",
    y="fare",
    hue="survived"
)

plt.title("Fare Distribution by Class and Survival")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.show()

sns.countplot(
    data=df,
    x="embarked"
)

plt.title("Passengers by Embarkation Port")
plt.xlabel("Port")
plt.ylabel("Number of Passengers")

plt.show()

survival_by_port = (
    df.groupby("embarked")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(survival_by_port)
#Next investigation

#Let's look at where passengers boarded.

#The embarked column contains:

#S → Southampton
#C → Cherbourg
#Q → Queenstown
#Did the embarkation port have any relationship with survival?
#Step 1 — Calculate survival rate
survival_by_port = (
    df.groupby("embarked")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(survival_by_port)
#Step 2 — Visualize
sns.barplot(
    data=df,
    x="embarked",
    y="survived"
)

plt.title("Survival Rate by Embarkation Port")
plt.xlabel("Embarkation Port")
plt.ylabel("Survival Rate")

plt.show()
#Next: Family Size
df["family_size"] = df["sibsp"] + df["parch"] + 1 #Because sibsp + parch counts the other family members, but not the passenger themselves.
family_survival = (
    df.groupby("family_size")["survived"]
      .mean()
      .mul(100)
      .round(2)
)

print(family_survival)

numeric_cols = [
    "survived",
    "pclass",
    "age",
    "sibsp",
    "parch",
    "fare",
    "family_size"
]

corr = df[numeric_cols].corr()

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f"
)

plt.title("Titanic Correlation Heatmap")
plt.show()
