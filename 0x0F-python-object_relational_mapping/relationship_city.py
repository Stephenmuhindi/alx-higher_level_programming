#!/usr/bin/python3
"""
relationship tableau for cities using decla
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_city import City
from relationship_state import Base

class City(Base):
    """tableau de cities"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
