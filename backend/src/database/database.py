# configuring database connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+aiomysql://root:798745@172.21.0.3:3306/favmenus"

engine = create_async_engine(DATABASE_URL, echo = True)

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()
