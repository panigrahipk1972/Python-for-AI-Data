import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
np.random.seed(42)

X = np.linspace(0, 10, 30)

y = 2 * X**2 + 3 * X + 10 + np.random.normal(0, 15, 30)

np.random.normal(0, 15, 30)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train.reshape(-1, 1), y_train)

y_train_pred = model.predict(X_train.reshape(-1, 1))
y_test_pred = model.predict(X_test.reshape(-1, 1))#Turn this into one column, with however many rows are necessary.
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

print("Training R²:", train_r2)
print("Testing R²:", test_r2)

print("Training MSE:", train_mse)
print("Testing MSE:", test_mse)
poly_model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)
overfit_model = make_pipeline(
    PolynomialFeatures(degree=15),
    LinearRegression()
)

overfit_model.fit(X_train.reshape(-1, 1), y_train)

y_train_pred_overfit = overfit_model.predict(X_train.reshape(-1, 1))
y_test_pred_overfit = overfit_model.predict(X_test.reshape(-1, 1))
poly_model.fit(X_train.reshape(-1, 1), y_train)

y_train_pred_poly = poly_model.predict(X_train.reshape(-1, 1))
y_test_pred_poly = poly_model.predict(X_test.reshape(-1, 1))
train_r2_poly = r2_score(y_train, y_train_pred_poly)
test_r2_poly = r2_score(y_test, y_test_pred_poly)

train_mse_poly = mean_squared_error(y_train, y_train_pred_poly)
test_mse_poly = mean_squared_error(y_test, y_test_pred_poly)

print("\nPolynomial Regression (Degree 2)")
print("Training R²:", train_r2_poly)
print("Testing R²:", test_r2_poly)

print("Training MSE:", train_mse_poly)
print("Testing MSE:", test_mse_poly)
train_r2_overfit = r2_score(y_train, y_train_pred_overfit)
test_r2_overfit = r2_score(y_test, y_test_pred_overfit)

train_mse_overfit = mean_squared_error(y_train, y_train_pred_overfit)
test_mse_overfit = mean_squared_error(y_test, y_test_pred_overfit)

print("\nPolynomial Regression (Degree 15)")
print("Training R²:", train_r2_overfit)
print("Testing R²:", test_r2_overfit)

print("Training MSE:", train_mse_overfit)
print("Testing MSE:", test_mse_overfit)
print("\n--- Comparing Polynomial Degrees ---")

for degree in [1, 2, 3, 5, 10, 15]:
    
    model = make_pipeline(
        PolynomialFeatures(degree=degree),
        LinearRegression()
    )

    model.fit(X_train.reshape(-1, 1), y_train)

    train_prediction = model.predict(X_train.reshape(-1, 1))
    test_prediction = model.predict(X_test.reshape(-1, 1))

    train_score = r2_score(y_train, train_prediction)
    test_score = r2_score(y_test, test_prediction)

    print(
        f"Degree {degree}: "
        f"Train R² = {train_score:.3f}, "
        f"Test R² = {test_score:.3f}"
    )
    # Create values for a smooth regression curve
X_curve = np.linspace(0, 10, 200).reshape(-1, 1)

# Degree 1 model
model_1 = make_pipeline(
    PolynomialFeatures(degree=1),
    LinearRegression()
)
model_1.fit(X_train.reshape(-1, 1), y_train)

# Degree 2 model
model_2 = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)
model_2.fit(X_train.reshape(-1, 1), y_train)

# Degree 10 model
model_10 = make_pipeline(
    PolynomialFeatures(degree=10),
    LinearRegression()
)
model_10.fit(X_train.reshape(-1, 1), y_train)

# Predictions for smooth curve
y_curve_1 = model_1.predict(X_curve)
y_curve_2 = model_2.predict(X_curve)
y_curve_10 = model_10.predict(X_curve)
plt.scatter(
    X,
    y,
    label="Actual Data"
)

plt.plot(
    X_curve,
    y_curve_1,
    label="Degree 1"
)

plt.plot(
    X_curve,
    y_curve_2,
    label="Degree 2"
)

plt.plot(
    X_curve,
    y_curve_10,
    label="Degree 10"
)

plt.xlabel("X")
plt.ylabel("y")
plt.title("Underfitting vs Good Fit vs Overfitting")

plt.legend()
plt.show()