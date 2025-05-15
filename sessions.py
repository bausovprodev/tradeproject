from fastapi import APIRouter

router = APIRouter()

@router.get("/sessions")
def get_sessions():
    return [{"session_id": 1, "ip": "192.168.0.1", "confirmed": True}]