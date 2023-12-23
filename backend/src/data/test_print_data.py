import pandas as pd
from sqlalchemy.orm import Session

from database import SessionLocal
from data_models import Restaurant, Foods

def get_restaurants(db: Session):
    return db.query(Restaurant).all()

def get_foods(db: Session):
    return db.query(Foods).all()

def main():
    db = SessionLocal()

    # Fetch data from the restaurants table
    restaurants = get_restaurants(db)

    # Convert the data to a pandas DataFrame
    restaurant_data = [{"id": r.id, "name": r.name, "description": r.description, "image": r.image} for r in restaurants]
    restaurant_df = pd.DataFrame(restaurant_data)

    # Print the Restaurants DataFrame
    print("Restaurants:")
    print(restaurant_df)

    # Fetch data from the foods table
    foods = get_foods(db)

    # Convert the data to a pandas DataFrame
    food_data = [{"id": f.id, "restaurant_id": f.restaurant_id, "name": f.name, "description": f.description, "image": f.image, "price": f.price} for f in foods]
    food_df = pd.DataFrame(food_data)

    # Print the Foods DataFrame
    print("\nFoods:")
    print(food_df)
    breakpoint()

if __name__ == "__main__":
    main()