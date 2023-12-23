from src.utils import get_retriever
from llama_index.vector_stores.types import ExactMatchFilter


async def find_restaurant_pages(
        CONFIG,
        name_of_restaurant=None,
        type_of_restaurant=None,
        food_requested=None,
        other_information=None,
        quantity=1,
    ):
    """Opens the restaurant page"""

    query = get_query(
        name_of_restaurant=name_of_restaurant,
        type_of_restaurant=type_of_restaurant,
        food_requested=food_requested,
        other_information=other_information,
    )

    retriever = get_retriever(
        index_name="auto-food-order",
        CONFIG=CONFIG,
        top_k=quantity,
        filter=[ExactMatchFilter(key="search_type", value="restaurant")]
    )

    response = retriever.retrieve(query)
    
    # return dict(dict(response[0])["node"])["metadata"]
    for i in range(len(response)):
        response[i] = dict(dict(response[i])["node"])["metadata"]
    return response


def get_query(
        name_of_restaurant: str=None,
        type_of_restaurant: str="",
        food_requested: list=[],
        other_information:str ="",
    ):
    """Returns the query for the restaurant page"""
    name_of_restaurant_query = f"""
    Name: {name_of_restaurant}
    """ if name_of_restaurant else ""

    type_of_restaurant_query = f"""
    Type of restaurant: {type_of_restaurant}
    """ if type_of_restaurant else ""

    food_requested_query = f"""
    Food requested: {food_requested}
    """ if food_requested else ""

    other_information_query = f"""
    Other information: {other_information}
    """ if other_information else ""

    return f"""
    {name_of_restaurant_query}
    {type_of_restaurant_query}
    {food_requested_query}
    {other_information_query}
    """