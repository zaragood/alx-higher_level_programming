#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""create the base class using declarative_base() function"""
Base = declarative_base()

"""class definition of a State and an instance Base = declarative_base()"""


class State(Base):
    """mysql table states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
