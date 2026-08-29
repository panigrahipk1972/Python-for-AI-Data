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


class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    city: str | None = None


# -------------------------
# Fake Database
# -------------------------

students = [
    Student(id=1, name="Rahul", age=20, city="Pune"),
    Student(id=2, name="Amit", age=21, city="Delhi"),
    Student(id=3, name="Priya", age=19, city="Mumbai")
]


# -------------------------
# PATCH
# -------------------------

@app.patch("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):

    # 1. Find the student

    for student in students:

        if student.id == student_id:

            # 2. Get only the fields sent by the client

            update_data = student_update.model_dump(
                exclude_unset=True
            )

            # 3. Update those fields

            for field, value in update_data.items():
                setattr(student, field, value)

            # 4. Return updated student

            return student

    # 5. Student not found

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )