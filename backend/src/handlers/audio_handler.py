
# Typing hints
from typing import Optional

# Configuration and helpers
from fastapi.encoders import jsonable_encoder
from src.config import CONFIG

# Importing schemas and hints
from src.schemas import ChatRequest

# Utils
import json
import base64
from pydub import AudioSegment
from io import BytesIO


CFG_PROMPTS = CONFIG["prompts"]
CFG_CHAT = CFG_PROMPTS["chat"]
CFG_FUNCTIONS = CFG_PROMPTS["functions"]


# Utils
from pathlib import Path


## Creating handler
class AudioHandler():
    def __init__(
        self,
    ):
        pass

    def extract_audio_segment(self, audio_file):
        """Extracts the audio segment from the audio file"""

        # Extracting the audio segment
        audio_data = base64.b64decode(audio_file)
        audio_segment = AudioSegment.from_file(BytesIO(audio_data))
        return audio_segment, audio_data
