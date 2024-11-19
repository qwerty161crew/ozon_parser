from typing import List

from fastapi import APIRouter, Depends


from schema.ozon import OzonProduct
from schema import GreatOfferParser
from app.services.ozon import ParserService, get_parser_service

ozon_router = APIRouter(prefix="/ozon")


@ozon_router.post("/parse_great_offers", response_model=List[OzonProduct])
async def parse_great_offers(
    request: GreatOfferParser,
    parser_service: ParserService = Depends(get_parser_service),
):
    pass
