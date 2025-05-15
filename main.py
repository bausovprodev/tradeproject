from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as trader_router
from app.auth import router as auth_router

app = FastAPI(title="Trader Panel Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(trader_router, prefix="/trader", tags=["Trader"])

@app.get("/")
def root():
    return {"message": "Trader Panel API is running"}