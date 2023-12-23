# Services

## Functions


- `add_food_to_cart(CONFIG, restaurant_uuid, food_id, quantity)`: Adds a food item to the cart. Returns a dictionary containing the restaurant UUID, food ID, and quantity.
- `find_restaurant_pages(CONFIG, name_of_restaurant, type_of_restaurant, food_requested, other_information, quantity)`: Finds restaurant pages based on the given parameters. Returns a list of restaurant metadata.
- `get_query(name_of_restaurant, type_of_restaurant, food_requested, other_information)`: Returns a query for the restaurant page based on the given parameters.
- `get_menu_of_restaurant(CONFIG, restaurant_uuid)`: Retrieves the menu of a given restaurant. Returns a dictionary containing the raw and formatted menu.
- `open_restaurant_page(CONFIG, restaurant_uuid)`: Opens a restaurant page. Returns a dictionary containing the restaurant UUID.
- `remove_food_from_cart(CONFIG, restaurant_uuid, food_id)`: Removes a food item from the cart. Returns a dictionary containing the restaurant UUID and food ID.

## OpenAI Services

- `chat_completion(messages, CONFIG, functions, client)`: Receives the chatlog from the user and answers. Returns the response from the OpenAI API.
- `embeddings(content, CONFIG, client)`: Receives a content in text and embeds it. Returns the embedded content.
- `tts(text, CONFIG, client)`: Receives text and returns the audio bytes. Returns the audio in base64 format.
- `whisper(audio_file, CONFIG, client)`: Receives an audio file and returns the transcript. Returns the transcribed text.