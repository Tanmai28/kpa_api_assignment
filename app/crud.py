from sqlalchemy.orm import Session
from .models import User, FormData

def authenticate_user(db: Session, phone: str, password: str):
    return db.query(User).filter(User.phone == phone, User.password == password).first()

def get_all_formdata(db: Session):
    return db.query(FormData).all()