#from fastapi import APIRouter, Form

#router = APIRouter(prefix="/auth", tags=["Authentication"])

#@router.post("/login")
#async def login(username: str = Form(...), password: str = Form(...)):
 #   return {"message": f"User {username} attempted login"}
 
from fastapi import APIRouter, Form, HTTPException, status
from datetime import timedelta

from user import authenticate_user, register_user
from security import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

# POST /auth/register
@router.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    success = register_user(username, password)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists.")
    return {"message": f"User '{username}' registered successfully."}

# POST /auth/login
@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    # Create JWT token for authenticated user
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)

    return {
        "access_token": token,
        "token_type": "bearer",
        "message": f"Welcome back, {username}!"
    }

