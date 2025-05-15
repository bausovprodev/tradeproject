from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def get_statistics():
    return {
        "total_deals": 25,
        "rub_received": 120000,
        "usdt_spent": 1100,
        "average_rate": 109.09,
        "profit": 3500
    }