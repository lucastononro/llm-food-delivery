import openai
from fastapi.encoders import jsonable_encoder
from typing import Optional
from datetime import datetime

async def chat_completion(messages, CONFIG, functions=[], client=None):
    """Receives the chatlog from the user and answers"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "model": CFG_OPENAI.get("chat_model", "gpt-4"),
        "temperature": CFG_OPENAI.get("temperature", 0),
        "max_tokens": CFG_OPENAI.get("max_tokens", 512),
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "messages": messages
    }

    # Incrementing in cases of function calling
    if len(functions) > 0:
        model_args["functions"] = functions
        model_args["function_call"] = "auto"

    response = client.chat.completions.create(**model_args)

    # Returning raw response
    return response