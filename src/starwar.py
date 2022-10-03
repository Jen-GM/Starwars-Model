import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(15), nullable=False)
    password = Column(String(20), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(150), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(150), nullable=False)
    gender = Column(String(15), nullable=True)
    hair_color = Column(String(20), nullable=True)
    eye_color = Column(String(20), nullable=True)

class Planets_Favorites(Base):
    __tablename__ = 'planets_favorites'
    
    id = Column(Integer, primary_key=True)    
    
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

class Characters_Favorites(Base):
    __tablename__ = 'characters_favorites'
    
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    
    character_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'starwar.png')