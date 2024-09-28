from pydantic import BaseModel
from typing import Optional
from datetime import date

class MusicBase(BaseModel):
    title: str
    artist: str
    album: str
    genre: str
    release_date: date
    duration: float

class MusicCreate(MusicBase):
    pass

class MusicUpdate(MusicBase):
    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    genre: Optional[str] = None
    release_date: Optional[date] = None
    duration: Optional[float] = None

class Music(MusicBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email:str
    password:str

class UserCreate(UserBase):
    pass

