from fastapi import FastAPI,status
from pydantic import BaseModel, Field

app = FastAPI()
class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(gt=0, lt=100)
    course: str = Field(min_length=2, max_length=50)

class StudentResponse(BaseModel):
    id: int
    name: str
    course: str


@app.get("/")
def home():
    return {"message": "FastAPI Parameters Demo"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id
    }


#@app.get("/students")
#def get_students(city: str | None = None):
   # return {
    #    "city": city
    #}

#@app.get("/students")
#def get_students(city: str | None = None, age: int | None = None):
 #   return {
   #     "city": city,
   #     "age": age
    #}

@app.get("/students")
def get_students(city: str | None = None, age: int | None = None,course:str | None=None):
    return {
        "city": city,
        "age": age,
        "course":course
    }

#@app.post("/students")
#def create_student(student: Student):
 #   return {
 #       "message": "Student created successfully",
  #      "student": student
 #   }

#@app.post("/students", response_model=StudentResponse)
#def create_student(student: Student):
 #   return {
  #      "id": 1,
   #     "name": student.name,
    #    "age": student.age,
     #   "course": student.course
    #}
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: Student):
    return {
        "id": 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }