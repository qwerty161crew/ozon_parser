from decimal import Decimal

from pydantic import BaseModel


class OzonProduct(BaseModel):
    ozon_id: int
    title: str
    full_price: int
    sale_price: int
    rating: Decimal
    saller: str
