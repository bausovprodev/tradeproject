from fastapi import APIRouter, HTTPException
from app.schemas import Deal, Balance, TopUpRequest, TopUpResponse
from app.mock_data import MOCK_DEALS, MOCK_BALANCE

router = APIRouter()

@router.get("/deals/active", response_model=list[Deal])
def get_active_deals():
    return [d for d in MOCK_DEALS if d.status == "active"]

@router.get("/deals/history", response_model=list[Deal])
def get_deal_history(status: str = None):
    if status:
        return [d for d in MOCK_DEALS if d.status == status]
    return MOCK_DEALS

@router.post("/deals/confirm/{deal_id}")
def confirm_deal(deal_id: int):
    for deal in MOCK_DEALS:
        if deal.id == deal_id:
            deal.status = "confirmed"
            return {"message": "Deal confirmed"}
    raise HTTPException(status_code=404, detail="Deal not found")

@router.get("/balance", response_model=Balance)
def get_balance():
    return MOCK_BALANCE

@router.post("/balance/topup", response_model=TopUpResponse)
def topup_balance(data: TopUpRequest):
    MOCK_BALANCE.usdt += data.amount
    return TopUpResponse(message="Balance topped up", new_balance=MOCK_BALANCE.usdt)