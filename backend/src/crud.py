from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Restaurant, User
from database.database import SessionLocal

async def get_restaurants(skip: int = 0, limit: int = 10):
    """queries restaurnts

    Args:
        skip (int, optional): rows to skip. Defaults to 0.
        limit (int, optional): rows to query. Defaults to 10.

    Returns:
        _type_: _description_
    """
    async with SessionLocal() as session:
        async with session.begin():
            query = select(Restaurant).offset(skip).limit(limit)
            result = await session.execute(query)
            restaurants = result.scalars().all()
            return restaurants

async def get_user(username):
    # need to format by {username: {userinfo}}
    """queries a single user that has a matching username

    Args:
        username (str): username of the account

    Returns:
        dict: dictionary with key as username and dictionary value
    """
    async with SessionLocal() as session:
        async with session.begin():
            stmt = select(User).where(User.username == username)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return {username : user}
    

