<template>
  <div v-if="restaurant" class="restaurant-full-view">
    <div class="sticky-top">
      <button class="go-back-btn" @click="goBack">Return</button>
      <h2>{{ restaurant.name }}</h2>
      <img  @error="onImageError" :src="!(restaurant.image==null)? restaurant.image : 'restaurant.png'" class="restaurant-card-img-fullview rounded" alt="Restaurant Image" />
      <div class="description-container">
        <p>{{ restaurant.description }}</p>
      </div>
    </div>
    
    <div class="food-list">
      <food-item
        v-for="(food, index) in this.foods"
        :key="index"
        :food="food"
        @add-to-cart="addToCart"
        @register-action="registerAction"
      ></food-item>
    </div>
  </div>
</template>
  

<script>

import FoodItem from "../Common/FoodItem.vue";
import axios from "axios";

export default {
  components: {
    FoodItem,
  },
  props: {
    restaurant: {
      type: Object,
      required: true,
    },
  },
  data(){
    return {
      baseApiUrl: import.meta.env.VITE_APP_API_URL + "/api",
      foods: []
    }
  },
  methods: {
    registerAction(msg) {
      this.$emit("register-action", msg)
    },
    getFoods(restaurant) {
      axios.get(this.baseApiUrl + "/restaurants/" + `${restaurant.uuid}` + "/foods")
        .then(response => {
          this.foods = [];
          const data = response.data;
          for (let i = 0; i < data.length; i++) {
            this.foods.push({
              name: data[i].name,
              description: data[i].description,
              price: data[i].price,
              quantity: 1,
              restaurant: {
                restaurant
              },
              image: data[i].image,
              // image: null,
              uuid: data[i].id,
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    addToCart(item){
      this.$emit("add-to-cart", item)
    },
    goBack() {
      this.$emit("go-back");
    },
    onImageError(event) {
      event.target.src = 'restaurant.png';
    }
  },
  // mounted() {
  //   this.getFoods(this.restaurant)
  // }
};

  
</script>