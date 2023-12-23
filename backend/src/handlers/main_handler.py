# Handlers 
from .prompt_handler import PromptHandler
from .audio_handler import AudioHandler
from .vectordb_handler import VectorDBHandler

# Abstract class creation
from abc import ABC, abstractmethod

# Typing hints
from typing import Optional

# CONFIG
from ..config import CONFIG

# OpenAI
import openai

## Creating main handler
class MainHandler(ABC):
    def __init__(self,):
        self.openai_client = openai.OpenAI(api_key=CONFIG["openai"]["api_key"])
        self.prompt_handler = PromptHandler()
        self.audio_handler = AudioHandler()
        self.vectordb_handler = VectorDBHandler()