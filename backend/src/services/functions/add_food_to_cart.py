async def add_food_to_cart(
        CONFIG,
        restaurant_uuid: str=None,
        food_id: str=None,
        quantity: int=1,
):
    return {
        "response": {
            "restaurant_uuid": str(restaurant_uuid),
            "food_id": str(food_id),
            "quantity": int(quantity)
        }
    }