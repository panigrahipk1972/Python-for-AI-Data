import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

# Hours studied
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9]
])

# Result: 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

print("Hours studied:")
print(X)

print("Results:")
print(y)


# --------------------------------------------------
# 2. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print(X_train)

print("\nTesting data:")
print(X_test)


# --------------------------------------------------
# 3. Create and Train Model
# --------------------------------------------------

model = LogisticRegression()

model.fit(X_train, y_train)

print("\nModel trained successfully!")


# --------------------------------------------------
# 4. Make Predictions
# --------------------------------------------------

y_pred = model.predict(X_test)

print("\nTest predictions:")
print(y_pred)

print("Actual test results:")
print(y_test)


# --------------------------------------------------
# 5. Accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nTest Accuracy:", accuracy)


# --------------------------------------------------
# 6. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 7. Precision, Recall and F1-Score
# --------------------------------------------------

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nPrecision:", precision)
print("Recall:", recall)
print("F1-Score:", f1)


# --------------------------------------------------
# 8. Cross-Validation
# --------------------------------------------------

cv_model = LogisticRegression()

scores = cross_val_score(
    cv_model,
    X,
    y,
    cv=4
)

print("\nCross-Validation Scores:")
print(scores)

print("Average Cross-Validation Score:")
print(scores.mean())


# --------------------------------------------------
# 9. Predict a New Student
# --------------------------------------------------

new_student = np.array([[6.5]])

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("\nNew Student: 6.5 hours")

print("Prediction:", prediction)

print("Probability:")
print(probability)
# --------------------------------------------------
# 10. Predict Multiple New Students
# --------------------------------------------------

new_students = np.array([
    [2],
    [4],
    [4.5],
    [5],
    [6.5],
    [8]
])

predictions = model.predict(new_students)
probabilities = model.predict_proba(new_students)

print("\nMultiple Student Predictions:")

for i in range(len(new_students)):
    hours = new_students[i][0]
    prediction = predictions[i]
    pass_probability = probabilities[i][1]

    result = "Pass" if prediction == 1 else "Fail"

    print(
        f"{hours} hours -> "
        f"{result} "
        f"(Pass Probability: {pass_probability:.2%})"
    )