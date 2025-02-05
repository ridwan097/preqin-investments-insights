from pydantic import BaseModel

class Investor(BaseModel):
    id: int
    name: str
    total_commitment: int