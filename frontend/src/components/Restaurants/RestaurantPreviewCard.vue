<template>
  <div
    class="restaurant-card"
    @click="$emit('restaurant-clicked', restaurant.uuid)"
  >
    <div class="restaurant-card-item" :style="{'--delay': idx + 1}">
      <img :src="restaurant.image" @error="onImageError" class="restaurant-card-img-top rounded" alt="Restaurant Image" />
      <div class="restaurant-card-body">
        <h5 class="restaurant-card-title">{{ restaurant.name }}</h5>
        <p class="restaurant-card-text">
          <span v-if="restaurant.description.length > 30">
            {{ restaurant.description.substring(0, 30) }}... 
            <!-- <span class="show-more" @click.stop="showMore = true">Show more</span> -->
          </span>
          <span v-else>{{ restaurant.description }}</span>
          <span v-if="showMore">{{ restaurant.description.substring(100) }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    restaurant: {
      type: Object,
      required: true,
    },
    idx: {
      type: Number,
      required: true,
    }
  },
  methods: {
    onImageError(event) {
      event.target.src = 'restaurant.png';
    }
  }
};
</script>