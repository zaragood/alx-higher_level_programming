#!/usr/bin/python3
""" Defines a State class
    Inherits from SQLAlchemy Base and links to the MySQL table states
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Represents a state column for a MySQL table
    __table__: the name of the table to store states
    id: the states id
    name: the state's name
    cities: relation attribute
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
