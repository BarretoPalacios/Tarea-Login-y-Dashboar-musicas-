from sqlalchemy.orm import Session
import Model,Schema

class UserDAO:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, email: int):
        return self.db.query(Model.User).filter(Model.User.email == email).first()
    
    def create_user(self, email: str, password: str):
        db_user = Model.User(email=email, password=password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user