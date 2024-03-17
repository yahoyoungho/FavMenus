from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from database.models import Base, Role  # Import your SQLAlchemy Base

DATABASE_URL = "mysql+pymysql://root:789745@localhost/favmenus"


def add_sample_data(sessionlocal):
    db = sessionlocal()
    try:
        sample_roles = [
            Role(role_name="GOD"),
            Role(role_name="User"),
        ]
        db.add_all(sample_roles)

        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()



def init_db():
    # Create a synchronous engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Drop all tables (comment this out if you don't want to drop tables every time)
    Base.metadata.drop_all(engine)

    # Create all tables
    Base.metadata.create_all(engine)

    # create a sessionlocal class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    add_sample_data(SessionLocal)
if __name__ == "__main__":
    init_db()
