<template>
    <div class="loading-spinner-container">
        <div class="loading-spinner" :style="{ height: spinnerHeight, width: spinnerWidth }"></div>
    </div>
</template>

  <script>
  export default {
    name: 'LoadingSpinner',
    props: {
      height: {
        type: String,
        default: '36px',
      },
      width: {
        type: String,
        default: '36px',
      },
    },
    computed: {
      spinnerHeight() {
        return this.height;
      },
      spinnerWidth() {
        return this.width;
      },
    },
  };
  </script>
