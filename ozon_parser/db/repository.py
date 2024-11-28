from uuid import UUID

from aiormq import connect
from sqlalchemy.ext.asyncio import AsyncSession

from ozon_parser.db import StateEnum, Task, get_connection


class TaskRepository:
    def __init__(self, connection: AsyncSession) -> None:
        self.connection = connection

    async def create_task(self, task_id: UUID):
        async with self.connection as session:
            task_obj = Task(task_id=task_id, state=StateEnum.RUNNING)
            session.add(task_obj)
            await session.commit()
            return task_obj


async def get_repository():
    connect = await get_connection()
    return TaskRepository(connection=connect)
