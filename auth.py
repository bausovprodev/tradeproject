from fastapi import APIRouter, HTTPException
from app.schemas import AuthRequest, AuthResponse
from app.mock_data import TOKEN

router = APIRouter()

@router.post("/login", response_model=AuthResponse)
def login(data: AuthRequest):
    if data.token == TOKEN:
        return AuthResponse(token=TOKEN)
    raise HTTPException(status_code=401, detail="Invalid token")