import pandas as pd
from sqlalchemy.orm import Session

try:
    from database import SessionLocal
    from data_models import Restaurant, Foods
except:
    from .database import SessionLocal
    from .data_models import Restaurant, Foods


def get_restaurants(db: Session):
    return db.query(Restaurant).all()

def get_foods(db: Session):
    return db.query(Foods).all()

def get_menu_of_given_restaurant(db: Session, restaurant_id: int):
    return db.query(Foods).filter(Foods.restaurant_id == restaurant_id).all()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
