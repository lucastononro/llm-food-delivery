import tempfile
import base64   

async def tts(text, CONFIG, client=None):
    """Receives text and returns the audio bytes"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "input": text,
        "model": CFG_OPENAI["model_tts"],
        "voice": CFG_OPENAI["voice_tts"],
        "response_format": "mp3",
    }

    # Calling the engine
    response = client.audio.speech.create(
        **model_args
    )
    
    # Use a temporary file to store the audio file
    with tempfile.NamedTemporaryFile(suffix='.mp3') as tmp_file:
        response.stream_to_file(tmp_file.name)
        tmp_file.seek(0)  # Go to the beginning of the file
        audio_bytes = tmp_file.read()
    
    # return audio_bytes
    return base64.b64encode(audio_bytes).decode('utf-8')
