
# Typing hints
from typing import Optional

# Configuration and helpers
from fastapi.encoders import jsonable_encoder
from src.config import CONFIG


# Utils
import json


CFG_PROMPTS = CONFIG["prompts"]
CFG_CHAT = CFG_PROMPTS["chat"]
CFG_FUNCTIONS = CFG_PROMPTS["functions"]

## Creating handler
class VectorDBHandler():
    def __init__(
        self,
    ):
        pass

    def prepare_response(self, response):
        """Formats the response from the system"""
        fit_responses = []
        for rep in response:
            text = rep.node.text
            metadata = rep.node.metadata

            fit_responses.append(
                {
                    "text": text,
                    "metadata": metadata,
                }
            )

        return fit_responses 

    


