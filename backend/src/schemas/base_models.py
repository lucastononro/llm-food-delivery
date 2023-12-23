from pydantic import BaseModel
from typing import Optional, List, Any, Dict

## OpenAI schema for Chat Completion
class FunctionCall(BaseModel):
    name: str
    arguments: str

class Message(BaseModel):
    content: str
    role: str
    function_call:FunctionCall
    
class Choices(BaseModel):
    finish_reason: str
    index: int
    message: Message

class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class OpenAIChatCompletionResponse(BaseModel):
    choices: Message
    created: int
    id: str
    model: str
    object: str
    usage: Usage

## Message System
class InputMessage(BaseModel):
    role: str
    content: Any
    name: Optional[str] = None

class InputChatHistory(BaseModel):
    history: List[InputMessage]

class ChatRequest(BaseModel):
    query: InputChatHistory
    function_call: bool=True


## Audio system
class AudioTranscriptRequest(BaseModel):
    audio: str
class AudioResponse(BaseModel):
    message: str

class AudioTTSRequest(BaseModel):
    text: str