from decimal import Decimal

from pydantic import BaseModel


class OzonProduct(BaseModel):
    id: int
    ozon_id: int
    title: str
    full_price: int
    sale_price: int
    rating: Decimal
    saller: str
