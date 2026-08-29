from fastapi import Request
from fastapi.responses import JSONResponse


# -----------------------------------
# Global Exception Handler
# -----------------------------------

async def global_exception_handler(
    request: Request,
    exc: Exception
):

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An unexpected error occurred",
            "path": str(request.url)
        }
    )