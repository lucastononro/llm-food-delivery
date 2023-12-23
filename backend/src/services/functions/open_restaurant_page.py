
from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def open_restaurant_page(
        CONFIG,
        restaurant_uuid: str=None
):
    return {"response": {"restaurant_uuid": str(restaurant_uuid)}}