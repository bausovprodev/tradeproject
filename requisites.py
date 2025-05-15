from fastapi import APIRouter

router = APIRouter()

@router.get("/requisites")
def get_requisites():
    return [{"id": 1, "method": "card", "number": "****1234", "status": "active"}]