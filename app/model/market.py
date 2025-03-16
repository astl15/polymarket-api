import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.model.event import Event

class Market(BaseModel):
    id: str
    question: str
    endDate: datetime.datetime
    category: str
    liquidity: float
    events: List[Event]
   