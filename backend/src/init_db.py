from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from database.models import Base  # Import your SQLAlchemy Base

DATABASE_URL = "mysql+pymysql://root:789745@localhost/favmenus"

def init_db():
    # Create a synchronous engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Drop all tables (comment this out if you don't want to drop tables every time)
    Base.metadata.drop_all(engine)

    # Create all tables
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
