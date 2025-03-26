#inserting data into demo.py_file table
# Practicing SQLalchemy with Python for creating a database and adding data to it
# This is a test file to add data to the database created in demo.py
# The database table  is created in the demo.py file
# The data is added to the database in this file
# The database is created in the school database in the postgresql
# The table name is students_info
# The columns are ID, Name and Age
# The data is added to the database using ORM
# ORM is a programming technique for converting data between incompatible
from demo import Student,engine

from sqlalchemy.orm import sessionmaker

Session=sessionmaker(bind=engine)

session=Session()

user_1=Student(ID=2085,Name="Mohammad Umair Hafeez",Age=20)

user_2=Student(ID=1711,Name="Umair Baloch",Age=19)

user_3=Student(ID=536,Name="Umair",Age=14)

session.add_all([user_1,user_2,user_3])

session.commit()



