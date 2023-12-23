<template>
    <div :class="messageClass">
      <div v-if="isBot" class="img_cont_msg">
        <img :src="profilePic" class="user_img_msg">
      </div>
      <div :class="containerClass">
        <div class="typing-load-msg" :class="{ 'fadeInSlideRight': animate }" style="text-align:left">
          <span style="font-weight:normal" v-html="message"></span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "TypingMessage",
    props: {
      profilePic: {
        type: String,
        required: true,
      },
      message: {
        type: String,
        required: true,
      },
      isBot: {
        type: Boolean,
        required: true,
      },
    },
    data() {
      return {
        animate: true,
      }
    },
    watch: {
      message() {
        this.animate = false;
        this.$nextTick(() => { // Wait for the DOM update
          void this.$el.offsetWidth; // Force a reflow
          this.animate = true;
        });
      },
    },
    computed: {
      messageClass() {
        return this.isBot ? "d-flex justify-content-start mb-4" : "d-flex justify-content-end mb-4";
      },
      containerClass() {
        return this.isBot ? "container-assistant-msg" : "container-user-msg"
      }
    },
  };
  </script>