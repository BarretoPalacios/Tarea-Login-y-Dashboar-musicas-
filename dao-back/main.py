from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import Model, Schema, DaoMusica, DataBase,DaoUser
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create the database tables
Model.Base.metadata.create_all(bind=DataBase.engine)

origins = [
    "*",  # Permitir acceso desde cualquier dominio (usarlo con precaución)
]

# Añadir el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],   # Permitir todos los encabezados
)

def get_db():
    db = DataBase.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login/")
def login(user: Schema.UserBase, db: Session = Depends(get_db)):
    userDao = DaoUser.UserDAO(db)
    db_user = userDao.get_user(user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not db_user.password == user.password:
        raise HTTPException(status_code=404, detail="Credenciales incorrectas")
    return {
        "autorizado":True,
        "user":db_user.email
    }

@app.post("/register/", response_model=Schema.UserCreate)
def create_music(user: Schema.UserCreate, db: Session = Depends(get_db)):
    user_dao = DaoUser.UserDAO(db)
    return user_dao.create_user(user.email,user.password)

@app.post("/music/", response_model=Schema.Music)
def create_music(music: Schema.MusicCreate, db: Session = Depends(get_db)):
    music_dao = DaoMusica.MusicDAO(db)
    return music_dao.create_music(music)

@app.get("/music/{music_id}", response_model=Schema.Music)
def read_music(music_id: int, db: Session = Depends(get_db)):
    music_dao = DaoMusica.MusicDAO(db)
    db_music = music_dao.get_music(music_id)
    if db_music is None:
        raise HTTPException(status_code=404, detail="Music not found")
    return db_music

@app.get("/music/", response_model=list[Schema.Music])
def read_music_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    music_dao = DaoMusica.MusicDAO(db)
    return music_dao.get_music_list(skip=skip, limit=limit)

@app.put("/music/{music_id}", response_model=Schema.Music)
def update_music(music_id: int, music: Schema.MusicUpdate, db: Session = Depends(get_db)):
    music_dao = DaoMusica.MusicDAO(db)
    db_music = music_dao.update_music(music_id, music)
    if db_music is None:
        raise HTTPException(status_code=404, detail="Music not found")
    return db_music

@app.delete("/music/{music_id}", response_model=Schema.Music)
def delete_music(music_id: int, db: Session = Depends(get_db)):
    music_dao = DaoMusica.MusicDAO(db)
    db_music = music_dao.delete_music(music_id)
    if db_music is None:
        raise HTTPException(status_code=404, detail="Music not found")
    return db_music
