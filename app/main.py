from fastapi import FastAPI
from app.routes.markets import router as markets_router

app = FastAPI(
        title="PolymarketClient"
)

app.include_router(markets_router)      

@app.get("/")
def ping():
        return {"status": "RUNNING"}