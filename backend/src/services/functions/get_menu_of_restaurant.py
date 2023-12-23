
from ...data.database import SessionLocal
from ...data.data_utils import get_menu_of_given_restaurant


async def get_menu_of_restaurant(CONFIG, restaurant_uuid: int=None):
    # Loads menu
    db = SessionLocal()
    menu = get_menu_of_given_restaurant(db, restaurant_uuid)

    # Formats the menu
    menu_formatted = []
    for food in menu:
        food_formatted = {
            "food_id": food.id,
            "name": food.name,
            "description": food.description,
            "price": food.price,
            "image": food.image,
        }
        menu_formatted.append(food_formatted)

    menu_formatted_text = f"Menu of restaurant {restaurant_uuid}:" + "\n" + "\n\n---\n".join(
        [f"{food['name']}:\nDescription: {food['description']} \nPrice: {food['price']} \nID: {food['food_id']}" for food in menu_formatted]
    )

    return {"raw": menu_formatted, "formatted": menu_formatted_text}
    # return {"response": menu_formatted_text}