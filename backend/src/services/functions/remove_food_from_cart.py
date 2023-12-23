from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
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