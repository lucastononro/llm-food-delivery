# Prompts

## Chat

By editing [system.txt](./chat/system.txt) you can change the chatbot personality

## Functions

In (config.yaml)[/functions/config.yaml] you can edit the functions prompts:

```
functions:
 name: open_restaurant_page
    description: This function opens the page of a given restaurant, it can only open one restaurant at a time. Always confirm with the user that you are going to search and open a restaurant page with the information provided before calling the function. This function can only be called after the function get_restaurant_pages.
    parameters:
      type: object
      properties:
        restaurant_uuid:
          type: string
          description: The number of the restaurant page that comes in the function get_restaurant_pages previously called
    required: [restaurant_uuid]
    allow: true
```

This will recreate a [signatures.json](functions/signatures.json) file (that should not be touched). You can activate and deactivate a function using the `allow` flag. This will make the function invisible to the [chat_completion](../services/openai_service/chat_completion.py) api call


You can play with creating new functions by following the steps:

- Create a function in the (config.yaml)[/functions/config.yaml]
- Create a new function service like this [mock/dummy function](../services/functions/dummy_function.py)
- Import it in the [__init__.py](../services/functions/__init__.py)
- Add the function to the [routers.py](../endpoints/routers.py#72) in the `function_call` endpoint
```
available_function = {
    ... # Existent functions
    "new_function": lambda _: functions.new_function
}
```
- Edit the frontend [AppContainer.vue](../../../frontend/src/components/AppContainer.vue)
    - Add new method to handle the function they way you would like (e.g. [handleOpenRestaurant](../../../frontend/src/components/AppContainer.vue#379))
    - Add it to the [handleFunctionCall](../../../frontend/src/components/AppContainer.vue#314)