from fastapi import APIRouter, Depends

from ozon_parser.schema import GreatOfferParser
from ozon_parser.schema.ozon import OzonProduct
from ozon_parser.services.ozon import ParserService, get_parser_service

ozon_router = APIRouter(prefix="/ozon")


@ozon_router.post("/parse_great_offers", response_model=list[OzonProduct])
async def parse_great_offers(
    parse_data: GreatOfferParser,
    parser_service: ParserService = Depends(get_parser_service),
):
    await parser_service.get_great_offers_in_ozon(parse_data)
    return True
