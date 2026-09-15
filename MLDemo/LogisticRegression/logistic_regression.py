import numpy as np

# Hours studied
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9]])

# Result: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

print("Hours studied:")
print(X)

print("Result:")
print(y)

from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X, y)

print("Model trained successfully!")
# Predict for a student who studied 6.5 hours
new_student = np.array([[6.5]])

prediction = model.predict(new_student)

print("Prediction:", prediction)
# Get probability
probability = model.predict_proba(new_student)

print("Probability:", probability)
students = np.array([[2], [4.5], [6.5]])

print("Predictions:", model.predict(students))
print("Probabilities:")
print(model.predict_proba(students))
import matplotlib.pyplot as plt

# Create values for the X-axis
hours = np.linspace(1, 9, 100).reshape(-1, 1)

# Get probability of Pass (class 1)
pass_probability = model.predict_proba(hours)[:, 1]

# Plot the Logistic Regression curve
plt.plot(hours, pass_probability)

# Plot the original data points
plt.scatter(X, y)

plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.title("Logistic Regression - Pass Probability")

plt.show()
print("Model coefficient:", model.coef_)
print("Model intercept:", model.intercept_)
decision_boundary = -model.intercept_[0] / model.coef_[0][0]

print("Decision Boundary:", decision_boundary)
from sklearn.metrics import accuracy_score

# Predict all training data
predictions = model.predict(X)

# Calculate accuracy
accuracy = accuracy_score(y, predictions)

print("Predictions:", predictions)
print("Actual:", y)
print("Accuracy:", accuracy)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:")
print(X_train)

print("Testing data:")
print(X_test)
# Create a new Logistic Regression model
model2 = LogisticRegression()

# Train only on training data
model2.fit(X_train, y_train)

print("New model trained successfully!")
# Predict the test data
y_pred = model2.predict(X_test)

print("Test predictions:", y_pred)
print("Actual test results:", y_test)
# Create a new Logistic Regression model
model2 = LogisticRegression()

# Train only on training data
model2.fit(X_train, y_train)

print("New model trained successfully!")

# Predict the test data
y_pred = model2.predict(X_test)

print("Test predictions:", y_pred)
print("Actual test results:", y_test)

from sklearn.metrics import accuracy_score

test_accuracy = accuracy_score(y_test, y_pred)

print("Test Accuracy:", test_accuracy)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)
from sklearn.model_selection import cross_val_score

# Create a fresh Logistic Regression model
cv_model = LogisticRegression()

# Perform 5-Fold Cross-Validation
scores = cross_val_score(cv_model, X, y, cv=5)

print("Cross-Validation Scores:", scores)
print("Average Cross-Validation Score:", scores.mean())