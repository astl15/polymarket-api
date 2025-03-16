from fastapi import Depends
from app.infrastructure.repository.market_repository import MarketRepository
from app.model.market import Market

class MarketService:

    def __init__(self, repository: MarketRepository = Depends()):
        self.repository = repository

    def get_markets(self):
        print("Service")
        return self.repository.get_markets()