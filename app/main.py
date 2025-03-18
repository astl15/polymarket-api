from fastapi import Depends, FastAPI
from app.routes.markets import router as markets_router
from app.services.ping_service import PingService

STATUS_RUNNING = "RUNNING"
STATUS_PARTIAL_OUTAGE = "PARTIAL OUTAGE"

app = FastAPI(
        title="PolymarketClient"
)

app.include_router(markets_router)      

@app.get("/")
def ping(utilsService: PingService = Depends()):
        polymarketStatus = utilsService.ping()
        if polymarketStatus["status"] == STATUS_RUNNING:
                return {"status": STATUS_RUNNING}
        else:
                return {"status": STATUS_PARTIAL_OUTAGE}