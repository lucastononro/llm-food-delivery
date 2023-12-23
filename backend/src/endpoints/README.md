# README.md

## routers.py

### Purpose

This file contains the API routes for the application. It includes routes for sending messages, calling functions, transcribing audio, generating text-to-speech, and retrieving data from the database.

### Functions

- `create_router(handler: MainHandler, CONFIG)`: Creates the router object and defines the API routes.

### Endpoints

- `POST /chat/send_message`: Receives the chatlog from the user and answers. It takes a `ChatRequest` object as input and returns a response.
- `POST /chat/function_call`: Receives the function call from the frontend and executes it. It takes a `FunctionCall` object as input and returns a response.
- `POST /chat/transcribe`: Receives the audio file from the frontend and transcribes it. It takes an `AudioTranscriptRequest` object as input and returns a response.
- `POST /chat/tts`: Receives the text from the frontend and generates the audio file. It takes an `AudioTTSRequest` object as input and returns a response.
- `GET /restaurants/`: Retrieves all restaurants from the database. It doesn't require any input and returns a list of `Restaurant` objects.
- `GET /restaurants/{restaurant_id}/foods/`: Retrieves all foods from a specific restaurant. It takes a `restaurant_id` as input and returns a list of `Foods` objects.
