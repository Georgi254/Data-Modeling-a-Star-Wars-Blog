import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()
class People(Base):
    __tablename__ = 'people'
    name = Column(Integer, primary_key=True)
    height = Column(String(100))
    mass = Column(String(100))
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    homeworld = Column(String(100))

    posts = relationship("Planets",)
    comments = relationship("Comment")
class Planets(Base):
    __tablename__ = 'planets'
    name = Column(Integer, primary_key=True)
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(100))
    gravity = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(String(100))
    population = Column(String(100))
    residents = Column(String(100), ForeignKey('people.name'))
    resident = relationship("People")
    comments = relationship("Vehicles")
class Species(Base):
    __tablename__ = 'species'
    name = Column(Integer, primary_key=True)
    classification = Column(String(200))
    designation = Column(String(255))
    average_height = Column(String(100))
    skin_colors = Column(String(250))
    hair_colors = Column(String(250))
    eye_colors = Column(String(250))
    average_lifespan = Column(String(100))
    homeworld = Column(Integer, ForeignKey('planets.name'))
    homeworlds = relationship(Planets)
    people = relationship(People)
class Vehicles(Base):
    __tablename__ = 'vehicles'
    name = Column(Integer, primary_key=True)
    model = Column(String(100))
    manufracturer = Column(Integer, ForeignKey('planets.name'))
    cost_in_credits = Column(String(100))
    length = Column(String(100))
    max_atmosphering_speed = Column(String(100))
    crew = Column(String(100))
    passengers = Column(String(100))
    cargo_capacity = Column(String(100))
    consumables = Column(String(100))
    vehicle_class = Column(String(100))
    pilots = Column(Integer, ForeignKey('people.name'))
    pilot = relationship(People)
    manufracturer = relationship(Planets)
class Spaceships(Base):
    __tablename__ = 'spaceships'
    name = Column(Integer, primary_key=True)
    model = Column(String(100))
    manufracturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(100))
    max_atmosphering_speed = Column(String(100))
    crew = Column(String(100))
    passengers = Column(String(100))
    cargo_capacity = Column(String(100))
    consumables = Column(String(100))
    hyperdrive_rating = Column(String(100))
    MGLT = Column(String(100))
    starship_class = Column(String(200))
    pilots = Column(Integer, ForeignKey('people.name'))
    pilot = relationship(People)
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e