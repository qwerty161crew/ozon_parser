from typing import List

from fastapi import APIRouter, Depends, Query
from schema.ozon import OzonProduct

ozon_router = APIRouter(prefix="/ozon")


@ozon_router.post("/parse_great_offers", response_model=List[OzonProduct])
async def parse_great_offers(limit: int = Query(None), parse_service):
    pass
