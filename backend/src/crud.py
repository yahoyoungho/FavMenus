from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Restaurant
from database.database import SessionLocal

async def get_restaurants(skip: int = 0, limit: int = 10):
    async with SessionLocal() as session:
        async with session.begin():
            query = select(Restaurant).offset(skip).limit(limit)
            result = await session.execute(query)
            restaurants = result.scalars().all()
            return restaurants
