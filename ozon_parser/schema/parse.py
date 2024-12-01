from uuid import UUID

from pydantic import BaseModel, ConfigDict

from ozon_parser.db import StateEnum


class CreateTaskParser(BaseModel):
    product_type: str | None = None
    start_url: str


class ResponseIdTask(BaseModel):
    task_id: UUID


class CheckTaskStatus(BaseModel):

    task_id: UUID


class ResponeCheckTask(CheckTaskStatus):
    model_config = ConfigDict(from_attributes=True)
    task_id: UUID
    state: StateEnum
    message: str | None


class GetResultParse(BaseModel):
    task_id: UUID
    task_id: UUID
