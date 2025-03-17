from fastapi import Depends
from app.infrastructure.repository.market_repository import MarketRepository
from app.model.market import Market

class MarketService:

    def __init__(self, repository: MarketRepository = Depends()):
        self.repository = repository

    def get_markets(self):
        return self.repository.get_markets()
    
    def get_market(self, market_id: str):
        params = {"id": market_id}
        return self.repository.get_markets(params=params)