from fastapi.responses import JSONResponse
import requests
from dotenv import load_dotenv
import os
from app.model.market import Market

class PolymarketGammaClient:

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("POLYMARKET_GAMMA_URL")
        self.markets_prefix = "/markets"


    def get_markets(self):
        url = self.base_url + self.markets_prefix
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return [Market(**market) for market in data]
        else:
            return Exception("Failed to fetch market data")