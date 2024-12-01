from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ozon_parser.db import StateEnum, Task, get_connection


class TaskRepository:
    def __init__(self, connection: AsyncSession) -> None:
        self.connection = connection

    async def create_task(self, task_id: UUID):
        print(task_id, type(task_id), "4324324324324324234324324324234234324")
        async with self.connection as session:
            task_obj = Task(task_id=task_id, state=StateEnum.RUNNING)
            session.add(task_obj)
            await session.commit()
            return task_obj

    async def get(self, task_id: UUID) -> Task | None:
        query = select(Task).where(Task.task_id == task_id)
        result = await self.connection.scalars(query)
        return result.one_or_none()


async def get_repository():
    connect = await get_connection()
    return TaskRepository(connection=connect)
    return TaskRepository(connection=connect)
