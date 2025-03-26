from sqlalchemy import create_engine,Column,Integer,String

from sqlalchemy.orm import declarative_base

db_url="postgresql://postgres:umair1234A%40@localhost:5432/school"

engine=create_engine(db_url)

Base=declarative_base()

class User(Base):

    __tablename__="students_info"

    id=Column(Integer,primary_key=True)

    Name=Column(String)

    Age=Column(String)

Base.metadata.create_all(engine)