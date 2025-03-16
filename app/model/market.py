import datetime
from pydantic import BaseModel

class Market(BaseModel):
    id: str
    question: str
    endDate: datetime.datetime
    category: str
    liquidity: float
   