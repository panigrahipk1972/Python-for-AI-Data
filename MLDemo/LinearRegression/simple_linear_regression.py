import matplotlib.pyplot as plt

# Dataset
study_hours = [1, 2, 3, 4, 5, 6]
marks = [42, 48, 65, 68, 78, 85]

# Calculate means
x_mean = sum(study_hours) / len(study_hours)
y_mean = sum(marks) / len(marks)

# Calculate slope
numerator = 0
denominator = 0

for x, y in zip(study_hours, marks):
    numerator += (x - x_mean) * (y - y_mean)
    denominator += (x - x_mean) ** 2

slope = numerator / denominator

# Calculate intercept
intercept = y_mean - slope * x_mean

# Make predictions
predicted_marks = [
    intercept + slope * x
    for x in study_hours
]

# Display results
print("X Mean:", x_mean)
print("Y Mean:", y_mean)
print("Slope:", slope)
print("Intercept:", intercept)

# Calculate residuals
for actual, predicted in zip(marks, predicted_marks):
    residual = actual - predicted
    print("Actual:", actual,
          "Predicted:", round(predicted, 2),
          "Residual:", round(residual, 2))
    # Calculate squared errors
squared_errors = []

for actual, predicted in zip(marks, predicted_marks):
    residual = actual - predicted
    squared_error = residual ** 2

    squared_errors.append(squared_error)

    print(
        "Residual:", round(residual, 2),
        "Squared Error:", round(squared_error, 2)
    )

# Calculate MSE
mse = sum(squared_errors) / len(squared_errors)

print("MSE:", round(mse, 2))

# Calculate RMSE
import math

rmse = math.sqrt(mse)

print("RMSE:", round(rmse, 2))

# Plot actual data points
plt.scatter(
    study_hours,
    marks,
    label="Actual Data"
)

# Plot regression line
plt.plot(
    study_hours,
    predicted_marks,
    label="Regression Line"
)

# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression")

plt.legend()
plt.show()