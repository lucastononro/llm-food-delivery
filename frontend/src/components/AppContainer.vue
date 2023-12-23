<template>
  <nav-bar :shopping-cart="shoppingCart" @open-cart="openCart"></nav-bar>
  <shopping-cart
    v-if="isCartOpen"
    ref="shoppingCart"
    :shopping-cart="shoppingCart"
    @close-cart="closeCart"
    @clear-shopping-cart="clearCart"
    @remove-from-cart="removeFromCart"
    @registerAction="registerAction"
  >
  </shopping-cart>

  <div >
    <div class="row justify-content-center">
        <div>
          <div class="app-container">
            <restaurants-container ref="restaurantsContainer"  
              @add-to-cart="addToCart"
              @register-action="registerAction"
            >
            </restaurants-container>
            <chat-container 
              ref="chatContainer"
              :isChatOpen="isChatOpen"
              :config="config"
              :messages="messages"
              :isRecordingFlag="isRecordingFlag"
              :recordedVoiceURL="recordedVoiceURL"
              :timeRecorded="timeRecorded"
              :botTyping="botTyping"
              :botTypingMsg="botTypingMsg"
              :userTranscribing="userTranscribing"
              :handsFreeFlag="handsFreeFlag"
              @send-message="sendMessage"
              @toggle-recording="toggleRecording"
              @cancel-audio="cancelAudio"
              @toggle-chatbot="toggleChatBot"
              @toggle-handsfree="toggleHandsFree"
            >
            </chat-container>
          </div>
        </div>      
    </div>
  </div>
  
</template>

  <script>
  import NavBar from "./Navbar/NavBar.vue"
  import ShoppingCart from "./ShoppingCart/ShoppingCart.vue"
  import ChatContainer from "./Chatbot/ChatContainer.vue";
  import RestaurantsContainer from "./Restaurants/RestaurantsContainer.vue"
  import './styles/common.css'
  import config from "./general_config.json";
  import axios from "axios";

  export default {
    name: "AppContainer",
    components: {
      NavBar,
      ShoppingCart,
      ChatContainer,
      RestaurantsContainer
    },
    data() {
      return {
        // Init
        config,
        isCartOpen: false,
        shoppingCart: [],
        baseApiUrl: import.meta.env.VITE_APP_API_URL + "/api/",
        baseChatApiUrl: import.meta.env.VITE_APP_API_URL + "/api/chat",
        handsFreeFlag: false,

        // Chatbot
        isChatOpen: false,
        messages: [
          {
            role: "assistant",
            content: config.fstMsg,
            logs: {
              time: null
            }
          }
        ],

        // User performed actions logger
        actions: [],
        
        // Audio
        isRecordingFlag: false,
        recordedVoiceURL: null,
        lastestAudioBlob: null,
        timeRecorded: 0,
        
        // Typing
        botTyping: false,
        botTypingMsg: null,
        userTranscribing: false,
      }
    },
    methods: {
      // -- Shopping Cart --
      openCart() {
        let flag_register_new_action = true;
        if (this.isCartOpen) {
          flag_register_new_action = false;
        }

        this.isCartOpen = true;
        // registering action
        if (flag_register_new_action) {
          this.registerAction("the shopping cart was opened")
        }
        
      },
      closeCart() {
        let flag_register_new_action = true;
        if (!this.isCartOpen) {
          flag_register_new_action = false;
        }
        this.isCartOpen = false;
        // registering action
        if (flag_register_new_action) {
          this.registerAction("the shopping cart was closed")
        }
      },
      clearCart() {
        this.shoppingCart.forEach(foodItem => {
          foodItem.fadeAway = true;
          setTimeout(() => {
            this.shoppingCart = this.shoppingCart.filter(item => item !== foodItem);
          }, 200); // Remove the item after 0.2 seconds (200 milliseconds)
          foodItem.fadeAway = false;
        });
        this.registerAction("removed all items from the shopping cart, it is now empty")
      },
      addToCart(foodItem){
        // Should check if the foodItem name is already in the cart
        // If so, increment the quantity

        if (this.shoppingCart.length === 0){
          this.shoppingCart.push(foodItem)
          // registering action
          this.registerAction(foodItem.name + " was added to the shopping cart")
        }
        else {
          const index = this.shoppingCart.findIndex(
            (item) => item.name === foodItem.name
          );
          if (index === -1){
            this.shoppingCart.push(foodItem)
            // registering action
            this.registerAction(foodItem.name + " was added to the shopping cart")
          }
          else {
            this.shoppingCart[index].quantity += 1
            // registering action
            this.registerAction(this.shoppingCart[index].name + " was added again to the shopping cart, totalizing " + this.shoppingCart[index].quantity + " items")
          }
        }
        // console.log(this.shoppingCart)
      },
      removeFromCart(foodItem) {
        const index = this.shoppingCart.findIndex(
          (item) => item.id === foodItem.id
        );
        this.shoppingCart[index].fadeAway = true;
        // registering action
        this.registerAction(this.shoppingCart[index].name + " was removed completely from the shopping cart")

        setTimeout(() => {
          this.shoppingCart[index].fadeAway = false;
          this.shoppingCart.splice(index, 1);
        }, 200); // Remove the item after the animation duration

        
      },

      // -- Messages management --

      // Chatbot
      toggleChatBot() {
        this.isChatOpen = !this.isChatOpen;
      },
      // Handsfree
      toggleHandsFree() {
        this.handsFreeFlag = !this.handsFreeFlag;
        console.log("Handsfree toggled: " + this.handsFreeFlag)

      },
      // Messages handling
      sendMessage: async function(textMessage) {
        /*Sends message to backend*/ 

        // If theres a new audio
        if (!(this.recordedVoiceURL == null)) {
          try {
            textMessage = await this.sendAudio(this.lastestAudioBlob);
            console.log(textMessage)
          } catch (error) {
            console.log(error);
            return;
          }
        }

        // Checking for empty string
        if (textMessage){
          if (
            !textMessage.replace(/\s/g, '').length &&
            !this.recordedVoiceURL
          ) {
            return
          }
        }

        // Adding message to list
        this.messages.push(
          {
            role: "user",
            content: textMessage,
            logs: {
              time: this.getCurrentTime()
            }
          }
        )
        
        // This creates the chathistory removing the logs from the message
        // TODO this could be done in a better way (maybe with a computed property)
        let chatHistory = this.getChatHistory()

        // Scrolling down
        this.scrollDown()

        // Parallelizing calls to backend
        Promise.all(
          this.generateAnswer(chatHistory),
        ).then(() => {
          console.log("Successfully sent message")
        }).catch(error => {
          console.log(error)
        })
      },
      generateAnswer: async function(chatHistory, function_call = true, ){
        // Message backend interaction
        this.botTyping = true
        axios.post(
          this.baseChatApiUrl + "/send_message", {
            query: {
              history: chatHistory
            },
            function_call: function_call
          }
        )
        .then(response => {
          console.log(response)
          let responseObject = response.data
          let answer = responseObject.response
          let functionCallSignal = responseObject.function_call

          // If we don't have to function call it will return the answer
          if (functionCallSignal == false || functionCallSignal == null) {
            this.botTypingMsg = null
            this.messages.push(
              {
                role: "assistant",
                content: answer,
                logs: {
                  time: this.getCurrentTime(),
                }
              }
            )
            this.botTyping = false
            this.scrollDown()
          }
          // if there's a function call, we call the function and get the answer, incorporate to the history and  call the function again
          else {
            this.handleFunctionCall(functionCallSignal)
              .then((functionCallOutput) => {
                // Then we need to call generateAnswer but with function call deactivated and a new parameter:
                this.messages.push(
                  functionCallOutput
                )
                this.generateAnswer(
                  chatHistory=this.getChatHistory(),
                  // function_call=false,
                  function_call=true,
                )
              })
              .catch((error) => {
                console.log("Error in function call:", error);
                this.botTyping=false
              });
          }

        }).catch(error => {
          console.log(error)
          this.messages.push(
            {
              role: "assistant",
              content: "<span style='color:red;'>Error:</span> Please try again later.<br/> Description: " + error,
            }
          )
        
        }).finally(() => {
        })
        
        return 
      },
      // Function calling
      handleFunctionCall: function(functionCallSignal) {
        return new Promise(async (resolve, reject) => {
          try {
            let functionCallResponse = await axios.post(
              `${this.baseChatApiUrl}/function_call`,
              functionCallSignal
            );

            let functionCallResponseContent;

            switch (functionCallSignal.name) {
              case "get_restaurant_pages":
                functionCallResponseContent = this.handleGetRestaurant(functionCallResponse);
                break;
              case "open_restaurant_page":
                functionCallResponseContent = this.handleOpenRestaurant(functionCallResponse);
                break;
              case "close_restaurant_page":
                functionCallResponseContent = this.handleCloseRestaurant(functionCallResponse);
                break;
              case "get_user_actions":
                functionCallResponseContent = this.handleGetActions(functionCallResponse);
                break;
              case "get_menu_of_restaurant":
                functionCallResponseContent = this.handleGetCurrentRestaurantMenu(functionCallResponse);
                break;
              case "open_shopping_cart": // to be implemented
                functionCallResponseContent = this.handleOpenShoppingCart(functionCallResponse);
                break;
              case "close_shopping_cart": // to be implemented
                functionCallResponseContent = this.handleCloseShoppingCart(functionCallResponse);
                break;
              case "add_food_to_cart":
                functionCallResponseContent = this.handleAddFoodToCart(functionCallResponse);
                break;
              case "remove_food_from_cart":
                functionCallResponseContent = this.handleRemoveFoodFromCart(functionCallResponse);
                break;
              case "place_order":
                functionCallResponseContent = this.handlePlaceOrder(functionCallResponse);
                break;
              case "activate_handsfree":
                functionCallResponseContent = this.handleActivateHandsFree(functionCallResponse);
                break;
              default:
                functionCallResponseContent = functionCallResponse.data.response.response;
                console.log("Name of function not found - returning response raw");
            }

            console.log(functionCallResponseContent);

            resolve({
              role: "function",
              content: functionCallResponseContent,
              name: functionCallSignal.name,
            });

          } catch (error) {
            reject(error);
          }
        });
      },
      handleGetRestaurant: function(functionCallResponse){
        this.botTypingMsg = "Searching for restaurants..."
        let msg = "@agent-action: You found the restaurant page(s) for " + JSON.stringify(functionCallResponse.data.response) + "!";
        return msg
        
      },
      handleOpenRestaurant: function(functionCallResponse){
        this.botTypingMsg = "Opening restaurant page..."
        // restaurantId in string format to int
        let restaurantId = parseInt(functionCallResponse.data.response.response.restaurant_uuid)
        this.$refs.restaurantsContainer.selectRestaurant(parseInt(restaurantId))
        let msg = "@agent-action: You opened the restaurant page for " + restaurantId + "!";
        console.log(msg)
        return msg
      },
      handleCloseRestaurant: function(functionCallResponse){
        this.botTypingMsg = "Closing restaurant page..."
        this.$refs.restaurantsContainer.deselectRestaurant()
        let msg = "@agent-action: You closed the restaurant page!";
        console.log(msg)
        return msg
      },
      handleAddFoodToCart: function(functionCallResponse){
        this.botTypingMsg = "Adding food to cart..."
        // Parsing ids
        let restaurantId = parseInt(functionCallResponse.data.response.response.restaurant_uuid)
        let foodId = parseInt(functionCallResponse.data.response.response.food_id)
        
        // Making sure the selected restaurant is the one we want
        let restaurantContainer = this.$refs.restaurantsContainer
        let restaurants = restaurantContainer.restaurants
        restaurantContainer.selectRestaurant(restaurantId)

        // Finding the right food, editing it
        let restaurantPage = restaurantContainer.$refs.restaurantFullView
        let foods = restaurantPage.foods
        let food = foods.find(food => food.uuid === foodId)
        food.quantity = functionCallResponse.data.response.response.quantity
        
        // Adding it to the shopping cart
        restaurantPage.addToCart(food)
        
        // Opening the shopping cart
        this.openCart()

        return "@agent-action: You added "+ food.quantity + " of "+ food.name + " to the shopping cart!"
      },

      handleRemoveFoodFromCart: function(functionCallResponse){
        this.botTypingMsg = "Removing food from cart..."
        // Parsing ids
        let restaurantId = parseInt(functionCallResponse.data.response.response.restaurant_uuid)
        let foodId = parseInt(functionCallResponse.data.response.response.food_id)

        // selecting shopping cart
        let shoppingCartContainer = this.$refs.shoppingCart
        let shoppingCartItems = shoppingCartContainer.shoppingCart
        let foodItem = shoppingCartItems.find(item => item.uuid === foodId)
        this.openCart()
        this.removeFromCart(foodItem)
        return "@agent-action: You removed "+ foodItem.quantity + " of "+ foodItem.name + " from the shopping cart!"
        // return 
      },
      handlePlaceOrder: function(functionCallResponse){
        this.botTypingMsg = "Placing order..."
        this.$refs.shoppingCart.submitOrder()
        let msg = "@agent-action: You placed the order!"
        return msg
      },
      handleGetActions: function(functionCallResponse){
        this.botTypingMsg = "Getting your latest actions..."
        let msg = JSON.stringify(this.actions.splice(-10))
        console.log("Compiling latest actions")
        console.log(msg)
        return msg
      },
      handleGetCurrentRestaurantMenu: function(functionCallResponse){
        this.botTypingMsg = "Getting the menu of the restaurant..."
        console.log(functionCallResponse)
        let menu = functionCallResponse.data.response["formatted"]
        console.log(menu)
        return menu
      },
      handleOpenShoppingCart: function(functionCallResponse){
        this.botTypingMsg = "Opening the shopping cart..."
        this.openCart()
        // If the shopping cart is not empty, we show the content
        if (this.shoppingCart.length > 0){
          let msg = "@agent-action: You opened the shopping cart! Here's the content you founded:" + JSON.stringify(this.shoppingCart)
          return msg
        } else {
          let msg = "@agent-action: You opened the shopping cart! It's empty!"
          return msg
        }
        return msg
      },
      handleCloseShoppingCart: function(functionCallResponse){
        this.botTypingMsg = "Closing the shopping cart..."
        this.closeCart()
        let msg = "@agent-action: You closed the shopping cart!"
        return msg
      },
      handleActivateHandsFree: function(functionCallResponse){
        this.botTypingMsg = "Activating handsfree experience..."
        let msg = "@agent-action: You activated the handsfree voice experience"
        this.handsFreeFlag = true
        return msg
      },

      // Utils
      getChatHistory: function(){
        // This removes the logs from the chat history before sending it to the backedn
        let chatHistory = []
        for (let i = 0; i < this.messages.length; i++) {
          let message = this.messages[i]
          let messageObject = {
            role: message.role,
            content: message.content
          }
          if (message.name) {
            messageObject.name = message.name
          }
          chatHistory.push(messageObject)
        }
        return chatHistory
      },

      registerAction: function(msg) {
        this.actions.push("@action:" + msg + " at " + this.getCurrentTime())
        console.log(this.actions)
      },

      // Audio
      sendAudio: function(blob) {
        try {
          this.userTranscribing = true
          this.scrollDown()
          const fileReader = new FileReader();
          fileReader.readAsDataURL(blob);
          return new Promise((resolve, reject) => {
            fileReader.onloadend = async () => {
              const base64String = fileReader.result.replace(/^data:(.*;base64,)?/, '');
              try {
                const response = await axios.post(this.baseChatApiUrl + "/transcribe", { audio: base64String });
                this.userTranscribing = false;
                this.recordedVoiceURL = null;
                resolve(response.data.response);
              } catch (error) {
                reject(error);
                this.userTranscribing = false
              }
            };
          });
        } catch (error) {
          console.error('Error sending audio:', error);
          this.userTranscribing = false
          return Promise.reject(error);
        }
      },

      // Audio Manipulation
      toggleRecording() {
        this.isRecordingFlag = !this.isRecordingFlag;
        if (this.isRecordingFlag) {
          this.chunks = []
          this.recordedVoiceURL = null; // clear previous recording
          navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
            this.recorder = new MediaRecorder(stream);
            this.recorder.addEventListener("dataavailable", (event) => {
              this.chunks.push(event.data);
            });
            this.recorder.addEventListener("stop", () => {
              this.lastestAudioBlob = new Blob(this.chunks, { type: "audio/mp3; codecs=opus" });
              this.recordedVoiceURL = URL.createObjectURL(this.lastestAudioBlob); // set recorded audio URL
            });
            this.recorder.start();
            this.timerInterval = setInterval(() => {
              this.timeRecorded += 10;
            }, 10);
          });
        } else {
          clearInterval(this.timerInterval);
          this.timeRecorded = 0;
          this.recorder.stop();
        }
      },
      cancelAudio(){
        this.isRecordingFlag = false;
        this.recordedVoiceURL = null;
      },

      // Auxiliary functions
      getCurrentTime() {
        const today = new Date();
        let hourTime = today.getHours()
        let minuteTime = today.getMinutes()
        let secondTime =  today.getSeconds()
        let currentTime = hourTime + ':' + minuteTime + ':' + secondTime
        return currentTime
      },
      scrollDown() {
      this.$nextTick(() => {
          this.$refs.chatContainer.$refs.chatMessages.$refs.pageChat.scrollTop = this.$refs.chatContainer.$refs.chatMessages.$refs.pageChat.scrollHeight;
        });
      },
    },
  };
  </script>
