async def remove_food_from_cart(
        CONFIG,
        restaurant_uuid: str=None,
        food_id: str=None,
):
    return {
        "response": {
            "restaurant_uuid": str(restaurant_uuid),
            "food_id": str(food_id),
        }
    }