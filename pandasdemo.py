import pandas as pd
import numpy as np
marks = pd.Series([85, 92, 76, 88, 95])

print(marks)

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Age": [20, 21, 22, 20],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df[["Name", "Marks"]])
print(df.head())
print(df.info())
print(df.describe())
print(df.iloc[0])
print(df.iloc[:, 0] )
print(df.iloc[1:3, 0:2])
print(df.loc[1])
print(df.loc[1:2, ["Name", "Marks"]])
print(df.loc[1:2, ["Name", "Age"]])
print(df[(df["Age"] == 20) & (df["Marks"] > 80)])
df_sorted = df.sort_values("Marks", ascending=False)
df_sorted = df_sorted.reset_index(drop=True)
df_sorted=df_sorted.reset_index(drop=True)
print(df_sorted)
#print(df.sort_values("Marks", ascending=False, inplace=True))
#print(df.sort_values(["Age", "Marks"]))
df["Result"] = "Pass"
print(df)
df["Bonus"] = df["Marks"] + 10
print(df)
df = df.drop("Bonus", axis=1)
print(df)

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan"],
    "City": ["Pune", "Delhi", "Mumbai", "Pune", "Delhi"],
    "Marks": [85, 92, 76, 88, 78]
})
print(df)
print(df.groupby("City")["Marks"].mean())
print(df.groupby("City")["Marks"].max())
print(df.groupby("City")["Marks"].count())
print(df.groupby("City")["Marks"].agg(
    ["mean", "max", "min", "count"]
))
print(df.groupby("City")["Marks"].sum())
print(df["City"].value_counts())
print(df["City"].unique())
print(df["City"].nunique())
students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4, 6],
    "Name": ["Rahul", "Priya", "Amit","Sneha", np.nan],
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 3,4,5],
    "Marks": [85, 92, 76,np.nan,89]
})

print(pd.merge(students, marks, on="StudentID",how="inner"))
print(pd.merge(students, marks, on="StudentID",how="left"))
print(pd.merge(students, marks, on="StudentID",how="right"))
print(pd.merge(students, marks, on="StudentID",how="outer"))
jan = pd.DataFrame({
    "Name": ["Rahul", "Priya"],
    "Marks": [85, 92]
})
feb = pd.DataFrame({
    "Name": ["Amit", "Sneha"],
    "Marks": [76, 88]
})
all_students = pd.concat([jan, feb])
print(all_students)

df1 = pd.DataFrame({
    "Name": ["Rahul", "Priya"]
})

df2 = pd.DataFrame({
    "Name": ["Amit", "Sneha"]
})

print(pd.concat([df1, df2], ignore_index=True))

df = pd.read_csv("students.csv")

print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df[(df["Marks"] > 80) & (df["City"] == "Pune")])
print(df[df["Marks"] >= 85])
print(df[df["City"].isin(["Pune", "Delhi"])])#"Is this value inside my list?"
print(df[df["City"].isin(["Pune", "Mumbai"])])
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 80 else "Fail"
)
print(df)

def add_bonus(x):
    return x + 5

df["Bonus"] = df["Marks"].apply(add_bonus)
print(df)
df.sort_values(
    ["City", "Marks"],
    ascending=[True, False]
)
print(df)
print(df.duplicated())
df = pd.read_csv("student_performance.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.isnull().sum())
top_students = df.sort_values("Marks", ascending=False)

print(top_students)

top5 = df.sort_values("Marks", ascending=False).head(5)

print(top5[["Name", "Marks", "City"]])
print(df.sort_values("Marks", ascending=False).head(5)[["Name", "Marks"]])
top5 = df.sort_values("Marks", ascending=False).head(5).reset_index(drop=True)

print(top5[["Name", "Marks", "City"]])
city_avg = df.groupby("City")["Marks"].mean()

print(city_avg)
city_analysis = df.groupby("City").agg({
    "Marks": "mean",
    "Attendance": "mean",
    "StudyHours": "mean"
})

print(city_analysis)
df.groupby("City").agg({
    "Marks": ["mean", "max", "min"],
    "Attendance": "mean"
})
print(df["StudyHours"].corr(df["Marks"]))
print(df[df["Marks"] >= 85])
print(df[df["City"].isin(["Pune", "Mumbai"])]
      )
df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 80 else "B"
)
print(df)
df.to_csv("student_performance_cleaned.csv", index=False)