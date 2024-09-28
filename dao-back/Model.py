from sqlalchemy import Column, Integer, String, Date, Float
from DataBase import Base

class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    album = Column(String)
    genre = Column(String)
    release_date = Column(Date)
    duration = Column(Float)  

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
