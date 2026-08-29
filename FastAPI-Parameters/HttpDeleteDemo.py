from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# -------------------------
# Models
# -------------------------

class Student(BaseModel):
    id: int
    name: str
    age: int
    city: str


# -------------------------
# Fake Database
# -------------------------

students = [
    Student(id=1, name="Rahul", age=20, city="Mumbai"),
    Student(id=2, name="Amit", age=21, city="Delhi"),
    Student(id=3, name="Priya", age=19, city="Mumbai")
]


# -------------------------
# DELETE
# -------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    # Find the student

    for student in students:

        if student.id == student_id:

            # Remove the student

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    # Student not found

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )