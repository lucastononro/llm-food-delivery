<template>
  <div class="shopping-cart-container">
    <div class="shopping-cart-header sticky-top">
      <button class="close-btn" @click="closeFrame">
        <span>&times;</span>
      </button>
      <h3>Shopping Cart</h3>
      <hr/>
    </div>
    <div class="shopping-cart-body">
      <food-item
      v-for="(item, index) in shoppingCart"
      :key="index"
      :food="item"
      :view="'shoppingcart'"
      @remove-from-cart="removeFromCart"
      :class="{ 'fade-away': item.fadeAway }"
      @register-action="registerAction"
    ></food-item>
    </div>
    <div v-if="shoppingCart.length">
      <hr/>
      <div class="shopping-cart-footer sticky-bottom" v-if="!isLoading && !orderStatus">
        <p class="total-price-container">Total Price: {{ totalPrice.toFixed(2) }} $</p>
        <button @click="submitOrder" class="order-btn">Order</button>
      </div>
    </div>

    
    <div class="shopping-cart-footer sticky-bottom" v-if="isLoading || orderStatus" style="animation: fadeInSlideUp 0.5s ease forwards">
      <p>{{ this.placeholderMsg }}</p>
      <loading-spinner v-if="isLoading" ></loading-spinner>
    </div>
    
  </div>
</template>

  <script>
  import "../styles/shoppingcart.css"
  import FoodItem from "../Common/FoodItem.vue"
  import LoadingSpinner from "../Common/LoadingSpinner.vue"

  export default {
    components: {
      FoodItem,
      LoadingSpinner
    },    
    props: {
      shoppingCart: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {
        isLoading: false,
        orderStatus: false,
        placeholderMsg: "Placing your order..."
      }
    },
    computed: {
      totalPrice() {
        return this.shoppingCart.reduce(
          (total, item) => total + item.price * item.quantity,
          0
        );
      },
    },
    methods: {
      registerAction(msg) {
        this.$emit("register-action", msg)
      },
      closeFrame() {
        this.$emit('close-cart')
        this.placeholderMsg = "Placing your order..."
        this.isLoading = false
        this.orderStatus = false
        
      },
      clearCart() {
        this.$emit('clear-shopping-cart')
      },
      removeFromCart(item) {
        this.$emit('remove-from-cart', item)
      },
      submitOrder() {
        this.isLoading = true;
        this.placeholderMsg = "Placing your order..."
        setTimeout(() => {
          this.isLoading = false;
          this.placeholderMsg = "Your order has been sent..."
          this.orderStatus = true // Sent order
          this.clearCart()
        }, 3000); // Simulate an API call with a 5-second delay
        this.placeholderMsg = "Place your order..."
        this.registerAction("placed the order as is")
      },
    // ...
    },
  };
  </script>