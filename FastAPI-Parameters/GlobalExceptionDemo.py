from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# -------------------------
# Global Exception Handler
# -------------------------

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "status": 500,
            "message": "An unexpected error occurred."
        }
    )


# -------------------------
# Normal Endpoint
# -------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }


# -------------------------
# Test Exception
# -------------------------

@app.get("/test-error")
def test_error():

    result = 10 / 0

    return {
        "result": result
    }


# -------------------------
# Expected Error
# -------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": 1,
        "name": "Rahul"
    }