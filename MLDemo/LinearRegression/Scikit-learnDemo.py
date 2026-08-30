from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("X_train:", X_train)
print("X_test:", X_test)

print("y_train:", y_train)
print("y_test:", y_test)

model = LinearRegression()

# Train the model
#model.fit(X, y)
model.fit(X_train, y_train)

# Slope and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predictions
#predicted_marks = model.predict(X)
predicted_marks = model.predict(X_test)

print("Predicted Marks:", predicted_marks)
print("\nActual vs Predicted:")

for actual, predicted in zip(y_test, predicted_marks):
    residual = actual - predicted

    print(
        "Actual:", actual,
        "Predicted:", round(predicted, 2),
        "Residual:", round(residual, 2)
    )

# MSE
#mse = mean_squared_error(y, predicted_marks)
mse = mean_squared_error(y_test, predicted_marks)

print("MSE:", mse)


# RMSE
import math

rmse = math.sqrt(mse)

print("RMSE:", rmse)
#r2 = r2_score(y, predicted_marks)
r2 = r2_score(y_test, predicted_marks)

print("R² Score:", r2)



new_study_hours = [[7]]

new_prediction = model.predict(new_study_hours)

print("Predicted marks for 7 study hours:",
      round(new_prediction[0], 2))