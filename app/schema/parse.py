from pydantic import BaseModel


class GreatOfferParser(BaseModel):
    limit: int = 10
