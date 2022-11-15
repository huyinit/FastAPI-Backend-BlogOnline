from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2


SQLALCHEMY_DATABASE_URL = "postgresql://ynmjafwmqtbjgr:adfbd98927ce2a05b53c4d64e89d2d34682f070b8c5d9cb78dc39b136d399a0b@ec2-52-1-17-228.compute-1.amazonaws.com:5432/dbohqden2q1u41"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         cnx = mysql.connector.connect(
#             user='root', password='22062001', host='127.0.0.1', database='test')
#         print("Database connection was succesfull!")
#         cursor = cnx.cursor(dictionary=True)
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
