from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Float
from sqlalchemy.orm import mapped_column
from .database import Base
from typing import Optional


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    streetAddress = Column(String)
    city = Column(String)
    stateProvice = Column(String)
    postalCode = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    cuisine_type = Column(String)
    rating = Column(Float)
    description = Column(String)
    websiteURL = Column(String)
    contactInfo = Column(String)



class Menus(Base):
    __tablename__="menus"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = mapped_column(ForeignKey("restaurants.id"))
    name = Column(String)
    price = Column(Numeric)
    imageURL = Column(String)
    rating = Column(Float)


class Users(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String)
    email = Column(String)

