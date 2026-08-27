from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# -----------------------------------
# JWT Configuration
# -----------------------------------

SECRET_KEY = "my-super-secret-key-change-this"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# -----------------------------------
# Password Hashing
# -----------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# -----------------------------------
# OAuth2 Configuration
# -----------------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# -----------------------------------
# Hash Password
# -----------------------------------

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# -----------------------------------
# Verify Password
# -----------------------------------

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# -----------------------------------
# Create JWT Access Token
# -----------------------------------

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# -----------------------------------
# Get Current User From JWT Token
# -----------------------------------

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")
        username = payload.get("username")

        if user_id is None or username is None:
            raise credentials_exception

        return {
            "user_id": user_id,
            "username": username
        }

    except JWTError:
        raise credentials_exception