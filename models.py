from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class DealModel(Base):
    __tablename__ = "deals"
    id = Column(Integer, primary_key=True, index=True)
    usdt = Column(Float)
    rub = Column(Float)
    status = Column(String)

class BalanceModel(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    usdt = Column(Float)
    rub = Column(Float)
    in_escrow = Column(Float)
    profit = Column(Float)