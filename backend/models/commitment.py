from pydantic import BaseModel

class Commitment(BaseModel):
    asset_class: str
    amount: int
