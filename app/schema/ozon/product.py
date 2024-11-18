from pydantic import BaseModel


from decimal import Decimal


class OzonProduct(BaseModel):
    id: int
    ozon_id: int
    title: str
    full_price: int
    sale_price: int
    rating: Decimal
    saller: str
