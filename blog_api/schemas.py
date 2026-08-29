from pydantic import BaseModel, EmailStr, Field


# -----------------------------------
# User Schemas
# -----------------------------------

class UserCreate(BaseModel):

    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Username must be between 3 and 50 characters"
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Password must be between 6 and 100 characters"
    )


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

    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    password: str = Field(
        ...,
        min_length=6,
        max_length=100
    )

# -----------------------------------
# Author Response
# -----------------------------------

class AuthorResponse(BaseModel):

    id: int
    username: str

    class Config:
        from_attributes = True


# -----------------------------------
# Post Schemas
# -----------------------------------

class PostCreate(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=200,
        description="Post title must be between 3 and 200 characters"
    )

    content: str = Field(
        ...,
        min_length=10
    )


class PostResponse(BaseModel):

    id: int
    title: str
    content: str
    author_id: int
    author: AuthorResponse

    class Config:
        from_attributes = True
