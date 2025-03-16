import datetime
from typing import Optional
from pydantic import BaseModel

class Event(BaseModel):
    id: str
    question: Optional[str] = None
    liquidity: float
    endDate: Optional[datetime.datetime] = None
    ticker: str