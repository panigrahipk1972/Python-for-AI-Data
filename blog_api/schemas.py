from pydantic import BaseModel, EmailStr


# -----------------------------------
# User Schemas
# -----------------------------------

class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):

    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


# -----------------------------------
# Login Schema
# -----------------------------------

class LoginRequest(BaseModel):

    username: str
    password: str


# -----------------------------------
# Post Schemas
# -----------------------------------

class PostCreate(BaseModel):

    title: str
    content: str


class PostResponse(BaseModel):

    id: int
    title: str
    content: str
    author_id: int

    class Config:
        from_attributes = True