import uuid

from pydantic import BaseModel


class CreateTaskParser(BaseModel):
    product_type: str | None = None
    start_url: str


class ReposneIdTask(BaseModel):
    task_id: uuid.uuid4


class CheckTaskStatus(BaseModel):
    task_id: uuid.uuid4


class ResponeCheckTask(CheckTaskStatus):
    result_url: str | None


class GetResultParse(BaseModel):
    task_id: uuid.uuid4
