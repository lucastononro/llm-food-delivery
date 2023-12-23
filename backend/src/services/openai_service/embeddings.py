import openai
from fastapi.encoders import jsonable_encoder
from typing import Optional

async def embeddings(content, CONFIG, client=None):
    """Receives a content in text and embeds it"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "model": CFG_OPENAI["embedding_model"],
    }

    # Calling the engine
    model_args["input"] = content

    # response = openai.Embedding.create(
    #     **model_args
    # )["data"][0]["embedding"]
    
    response = client.embeddings.create(**model_args)["data"][0]["embedding"]

    return response