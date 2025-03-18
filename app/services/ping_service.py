from fastapi import Depends
from app.infrastructure.client.polymarket_utils_client import PolymarketUtilsClient

class PingService:
    def __init__(self, utilsClient: PolymarketUtilsClient = Depends()):
        self.client = utilsClient
    
    def ping(self):
        return self.client.ping()