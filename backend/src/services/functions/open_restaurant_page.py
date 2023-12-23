
async def open_restaurant_page(
        CONFIG,
        restaurant_uuid: str=None
):
    return {"response": {"restaurant_uuid": str(restaurant_uuid)}}