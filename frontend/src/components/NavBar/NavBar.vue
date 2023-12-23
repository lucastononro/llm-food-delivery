<template>
    <header class="navbar navbar-dark sticky-top">
        <div class="nav navbar pt-2">
            <div class="navbar-brand shadow-none d-flex align-items-center">
                <img class="navbar-logo" src="favicon.png" />
                <h2 class="navbar-title mb-0">
                  Discover restaurants and order food online using a virtual assistant 
                </h2>
            </div>
        </div>
        <div class="shopping-cart" @click="$emit('open-cart')">
            <span v-if="cartItemCount" class="cart-item-count">{{ cartItemCount }}</span>
            <img class="shopping-cart-logo" src="shopping-cart-icon.png" alt="Shopping Cart" />
        </div>
    </header>
</template>

<script>
import "../styles/navbar.css"
import "../styles/shoppingcart.css"

export default {
  name: "NavBar",
  props: {
    shoppingCart: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    cartItemCount() {
      return this.shoppingCart.length;
    },
  },
};
</script>
