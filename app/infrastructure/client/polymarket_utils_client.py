from dotenv import load_dotenv
import os
import requests

class PolymarketUtilsClient:
    def __init__(self):
        load_dotenv()
        self.clob_url = os.getenv("POLYMARKET_CLOB_URL")

    def ping(self):
        response = requests.get(self.clob_url)
        return {"status": "RUNNING"} if response.status_code == 200 else {"status": "DOWN"}
        
