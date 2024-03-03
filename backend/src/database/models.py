from sqlalchemy import Column, Integer, String, ForeignKey, Float, MetaData, Table
from sqlalchemy.orm import mapped_column, relationship
from .database import Base
from typing import Optional




#Association table for the many to many relationship
restaurant_cusine_association = Table(
    "restaurant_cusine_association", Base.metadata,
    Column("restaurant_id", ForeignKey("restaurants.id"), primary_key=True),
    Column("cusine_type_id", ForeignKey("cusine_types.id"), primary_key=True)
)
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    streetAddress = Column(String(255), nullable=False)
    city = Column(String(100))
    stateProvice = Column(String(50))
    postalCode = Column(String(20))
    latitude = Column(Float)
    longitude = Column(Float)

    rating = Column(Float)
    description = Column(String)
    websiteURL = Column(String(1024))
    contactInfo = Column(String)

    cusine_types = relationship(
        "CusineType",
        secondary=restaurant_cusine_association,
        backref="restaurants"
    )


class CusineType(Base):
    __tablename__="cusine_ypes"
    id = Column(Integer, primary_key=True, index=True)
    typeName = Column(String(255),nullable=False)



class Menu(Base):
    __tablename__="menus"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = mapped_column(ForeignKey("restaurants.id"))
    name = Column(String(128))
    price = Column(Float)
    imageURL = Column(String(1024))  # Should be limited to a reasonable size
    rating = Column(Float)


class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String(128), nullable=False)
    email = Column(String(100), nullable=False)

