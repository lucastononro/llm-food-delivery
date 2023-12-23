<template>
  <div class="food-item">
    <img  @error="onImageError" :src="!(food.image==null)? food.image : 'food-placeholder.png'" class="food-img" alt="Food Image" />
    <div class="food-details">
      <h4 class="food-name">{{ food.name }}</h4>
      <p class="restaurant-name" v-if="view=='shoppingcart'">{{ food.restaurant.name}}</p>
      <p class="food-description" v-if="view=='restaurant'">{{ food.description }}</p>
      <p class="food-price"> Item(s) price: {{ parseFloat((food.price * food.quantity).toFixed(2)) }} $</p>
    </div>
    <div class="food-actions">
      <div class="quantity-control">
        <input class="quantity-input" type="number" v-model.number="food.quantity" min="1" readonly />
        <button class="quantity-btn" @click="decrementQuantity">-</button>
        <button class="quantity-btn" @click="incrementQuantity">+</button>
      </div>
      <button v-if="view=='restaurant'" class="add-to-cart-btn" @click="addToCart">Add</button>
      <button v-if="view=='shoppingcart'" class="add-to-cart-btn" @click="removeFromCart">Remove</button>
    </div>
  </div>
</template>
  
  <script>
  export default {
    props: {
      food: {
        type: Object,
        required: true,
      },
      view: {
        type: String,
        default: "restaurant",
      },
    },
    data() {
      return {
        quantity: 1,
      };
    },
    methods: {
      registerAction(msg) {
        this.$emit("register-action", msg)
      },
      addToCart() {
        this.$emit("add-to-cart", this.food);
      },
      removeFromCart() {
        this.$emit("remove-from-cart", { food: this.food });
      },
      incrementQuantity() {
        this.food.quantity++;
        this.registerAction("incremented the amount of food " + this.food.name + " to " + this.food.quantity + " items (in the restaurant page, not in the shopping cart)")
      },
      decrementQuantity() {
        if (this.food.quantity > 1) {
          this.food.quantity--;
          this.registerAction("decremented the amount of food " + this.food.name + " to " + this.food.quantity + " items (in the restaurant page, not in the shopping cart)")
        }
      },
      onImageError(event) {
        event.target.src = 'food-placeholder.png';
      }
    },
  };
  </script>