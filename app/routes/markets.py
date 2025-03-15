from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MARKETS_PREFIX = "/markets"

router = APIRouter()

@router.get(MARKETS_PREFIX)
def get_markets():
    url = os.getenv("POLYMARKET_GAMMA_URL") + MARKETS_PREFIX  # Read URL from .env file
    response = requests.get(url)
    if response.status_code == 200:
        return JSONResponse(content=response.json(), status_code=200)
    else:
        return JSONResponse(content={"error": "Failed to fetch data from Polymarket"}, status_code=response.status_code)

