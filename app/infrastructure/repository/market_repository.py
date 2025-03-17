from typing import List
from fastapi import Depends
from app.infrastructure.client.polymarket_gamma_client import PolymarketGammaClient
from app.model.market import Market


class MarketRepository:

    def __init__(self, client: PolymarketGammaClient = Depends()):
        self.client = client

    def get_markets(self, params=None):
        return self.client.get_markets(params=params)