from fastapi import FastAPI

app = FastAPI()


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

@app.get("/students")
def get_students(city: str | None = None, age: int | None = None):
    return {
        "city": city,
        "age": age
    }