from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from database.models import Base, Role, User , Restaurant, Menu # Import your SQLAlchemy Base

DATABASE_URL = "mysql+pymysql://root:789745@localhost/favmenus"


def add_sample_roles(sessionlocal):
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


def add_sample_users(sessionlocal):
    db = sessionlocal()
    try:
        sample_users = [
            User(hashed_password="$2b$12$78nr5lkjZglzgTzbYg0hweWgvAT7JD0yHvQye9EZWdYkPIAce8HUa",
                    username="test1@example.com",
                    first_name="test",
                    last_name="user"),
            User(hashed_password="$2b$12$78nr5lkjZglzgTzbYg0hweWgvAT7JD0yHvQye9EZWdYkPIAce8HUa",
                    username="test2@example.com",
                    first_name="test",
                    last_name="user")
                    ]
        db.add_all(sample_users)
        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

def add_sample_restaurants(sessionlocal):
    db = sessionlocal()
    try:
        sample_restaurants = [
            Restaurant(role_name="GOD"),
            Restaurant(role_name="User"),
        ]
        db.add_all(sample_restaurants)

        db.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

def add_sample_cusinetypes(sessionlocal):
    ...

def add_sample_menus(sessionlocal):
    ...



def init_db():
    # Create a synchronous engine
    engine = create_engine(DATABASE_URL, echo=True)

    # Drop all tables (comment this out if you don't want to drop tables every time)
    Base.metadata.drop_all(engine)

    # Create all tables
    Base.metadata.create_all(engine)

    # create a sessionlocal class
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    add_sample_roles(SessionLocal)
    add_sample_users(SessionLocal)

if __name__ == "__main__":
    init_db()
