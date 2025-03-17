from fastapi.responses import JSONResponse
import requests
from dotenv import load_dotenv
import os
from app.model.event import Event
from app.model.market import Market

class PolymarketGammaClient:

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("POLYMARKET_GAMMA_URL")
        self.markets_prefix = "/markets"


    def get_markets(self, params=None):
        url = self.base_url + self.markets_prefix
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            markets = []
            for market in data:
                if 'events' in market:
                    market['events'] = [Event(**event) for event in market['events']]
                markets.append(Market(**market))
            return markets
        else:
            return Exception("Failed to fetch market data")