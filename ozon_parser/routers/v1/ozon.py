from fastapi import APIRouter, Depends

from ozon_parser.schema import (
    CheckTaskStatus,
    CreateTaskParser,
    GetResultParse,
    ReposneIdTask,
    ResponeCheckTask,
)
from ozon_parser.schema.ozon import OzonProduct
from ozon_parser.services.ozon import ParserService, get_parser_service

ozon_router = APIRouter(prefix="/ozon")


@ozon_router.post("/create_parse", response_model=ReposneIdTask)
async def parse_great_offers(
    parse_data: CreateTaskParser,
    parser_service: ParserService = Depends(get_parser_service),
):
    await parser_service.create_task(parse_data)
    return True


# @ozon_router.post("/check_staus", response_model=ResponeCheckTask)
# async def check_status_task(
#     check_data: CheckTaskStatus,
#     parser_service: ParserService = Depends(get_parser_service),
# ):
#     pass


# @ozon_router.post("/get_result/{uuid}", response_model=list[OzonProduct])
# async def get_result_pars(
#     uuid: GetResultParse, parser_service: ParserService = Depends(get_parser_service)
# ):
#     pass
