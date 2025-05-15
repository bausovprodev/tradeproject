from app.schemas import Deal, Balance

TOKEN = "demo-token-1234"

MOCK_DEALS = [
    Deal(id=1, usdt=100.0, rub=10600.0, status="active"),
    Deal(id=2, usdt=150.0, rub=15900.0, status="active"),
    Deal(id=3, usdt=200.0, rub=21200.0, status="confirmed"),
    Deal(id=4, usdt=80.0, rub=8480.0, status="cancelled")
]

MOCK_BALANCE = Balance(
    usdt=500.0,
    rub=53000.0,
    in_escrow=150.0,
    profit=3200.0
)