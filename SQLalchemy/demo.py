# Practice with ORM in python
# ORM: Object Relational Mapping
# Without writing sql queries, we can create tables in database using ORM
# (Object Relational Mapping) in python.
# ORM is a programming technique for converting data between incompatible
# type systems using object-oriented programming languages.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:umair1234A%40@localhost:5432/school"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Student(Base):
    __tablename__ = "latest_student"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    Base.metadata.create_all(engine)
