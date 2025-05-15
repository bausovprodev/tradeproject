from pydantic import BaseModel
from typing import Optional

class AuthRequest(BaseModel):
    token: str

class AuthResponse(BaseModel):
    token: str

class Deal(BaseModel):
    id: int
    usdt: float
    rub: float
    status: str

class Balance(BaseModel):
    usdt: float
    rub: float
    in_escrow: float
    profit: float

class TopUpRequest(BaseModel):
    amount: float

class TopUpResponse(BaseModel):
    message: str
    new_balance: float