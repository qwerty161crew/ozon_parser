from pydantic import BaseModel


class GreatOfferParser(BaseModel):
    limit: int = 10
    product_type: str | None = None
