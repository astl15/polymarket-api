from typing import List
from fastapi import APIRouter, Depends
from app.model.market import Market
from app.services.market_service import MarketService

MARKETS_PREFIX = "/markets"

router = APIRouter()

@router.get(MARKETS_PREFIX)
def get_markets(service: MarketService = Depends()):
        return service.get_markets()

