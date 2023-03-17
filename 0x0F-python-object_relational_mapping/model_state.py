#!/usr/bin/python3
"""
a python file that contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SomeClass(Base):
    """
    a blueprint for the states table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True. nullable=False,
                unique=True, autoincrement=True)
    name =  Column(String(128), nullable=False)
