from sqlalchemy.orm import Session
import Model,Schema

class MusicDAO:
    def __init__(self, db: Session):
        self.db = db

    def create_music(self, music:Schema.MusicCreate):
        db_music = Model.Music(**music.dict())
        self.db.add(db_music)
        self.db.commit()
        self.db.refresh(db_music)
        return db_music

    def get_music(self, music_id: int):
        return self.db.query(Model.Music).filter(Model.Music.id == music_id).first()

    def get_music_list(self, skip: int = 0, limit: int = 10):
        return self.db.query(Model.Music).offset(skip).limit(limit).all()

    def update_music(self, music_id: int, music:Schema.MusicUpdate):
        db_music = self.db.query(Model.Music).filter(Model.Music.id == music_id).first()
        if db_music:
            for key, value in music.dict().items():
                setattr(db_music, key, value)
            self.db.commit()
            self.db.refresh(db_music)
        return db_music

    def delete_music(self, music_id: int):
        db_music = self.db.query(Model.Music).filter(Model.Music.id == music_id).first()
        if db_music:
            self.db.delete(db_music)
            self.db.commit()
        return db_music


