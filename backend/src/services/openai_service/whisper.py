import openai
from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def whisper(audio_file, CONFIG, client=None):
    """Receives an audio file and returns the transcript"""

    # Initializing the openai configuration
    CFG_OPENAI = CONFIG["openai"]

    model_args = {
        "file": audio_file,
        "model": CFG_OPENAI["model_transcript"],
        "language": CFG_OPENAI["model_transcript_language"]
    }

    # Calling the engine
    response = client.audio.transcriptions.create(
        **model_args
    )

    # Returning processed response
    return response.text
