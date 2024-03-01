from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from database.models import Base  # Import your SQLAlchemy Base
import asyncio

DATABASE_URL = "mysql+aiomysql://root:example@localhost/mydatabase"

async def init_db(engine: AsyncEngine):
    async with engine.begin() as conn:
        # Drop all tables if you want a clean start, comment this out otherwise
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    # Create an async engine instance
    engine = create_async_engine(DATABASE_URL, echo=True)
    
    # Run the init_db function using asyncio
    asyncio.run(init_db(engine))
