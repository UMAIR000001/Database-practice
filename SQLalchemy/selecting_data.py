from requests import Session
from demo import Student,engine
from sqlalchemy.orm import sessionmaker
Session=sessionmaker(bind=engine)
session=Session()


result=session.query(Student).all()
for row in result:
    print("ID:",row.ID,"Name:",row.Name,"Age:",row.Age)