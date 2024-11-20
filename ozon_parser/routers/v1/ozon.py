from typing import List

from fastapi import APIRouter, Depends


from ozon_parser.schema.ozon import OzonProduct
from ozon_parser.schema import GreatOfferParser
from ozon_parser.services.ozon import ParserService, get_parser_service

ozon_router = APIRouter(prefix="/ozon")


@ozon_router.post("/parse_great_offers", response_model=List[OzonProduct])
async def parse_great_offers(
    request: GreatOfferParser,
    parser_service: ParserService = Depends(get_parser_service),
):
    pass
