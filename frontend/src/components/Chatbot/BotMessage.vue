<template>
  <div class="d-flex justify-content-start mb-4">
    <div class="img_cont_msg">
      <img :src="ImageMessageBot" class="user_img_msg">
    </div>
    <div class="container-assistant-msg">
      <span style="font-weight:normal" v-html="message.content"></span>
    </div>
    <div class="audio-player">
        <vue-feather
          v-if="isLoading"
          type="loader"
          class="audio-control loading"
        ></vue-feather>
        <vue-feather
          v-else-if="!isPlaying"
          type="play-circle"
          class="audio-control"
          @click="playAudio()"
        ></vue-feather>
        <vue-feather
          v-else
          type="pause-circle"
          class="audio-control playing"
          @click="stopAudio"
        ></vue-feather>
      </div>
  </div>
</template>

<script>
import axios from 'axios';
import VueFeather from 'vue-feather';

export default {
  name: "BotMessage",
  components: {
    VueFeather,
  },
  props: {
    ImageMessageBot: {
      type: String,
      required: true,
    },
    message: {
      type: Object,
      required: true,
    },
    baseApiUrl: {
      type: String,
      required: true,
    },
    autoPlayAudio: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      baseChatApiUrl: import.meta.env.VITE_APP_API_URL + "/api/chat",
      isLoading: false,
      isPlaying: false,
      audio: null,

    };
  },
  mounted() {
    if (this.autoPlayAudio) {
      this.playAudio();
    }
  },
  methods: {
    playAudio() {
      // If audioSrc already exists, play it directly
      if (this.message.audioSrc) {
        this.playExistingAudio();
      } else {
        // Otherwise, make the POST request to get the audioSrc
        this.isLoading = true;
        axios.post(this.baseChatApiUrl + '/tts', { text: this.message.content })
          .then(response => {
            // Handle response
            this.message.audioSrc = 'data:audio/wav;base64,' + response.data.response;
            this.playExistingAudio();
          })
          .catch(error => {
            // Handle error
            console.error('Error playing audio:', error);
          })
          .finally(() => {
            this.isLoading = false;
          });
      }
    },
    playExistingAudio() {
      // Create a new Audio object if it doesn't exist
      if (!this.audio) {
        this.audio = new Audio(this.message.audioSrc);
      }
      // Play the audio
      this.audio.play();
      this.isPlaying = true;
      // When the audio ends, update the isPlaying state
      this.audio.onended = () => {
        this.isPlaying = false;
      };
    },
    stopAudio() {
      if (this.audio) {
        this.audio.pause();
        this.audio.currentTime = 0;
      }
      this.isPlaying = false;
    },
  },
};
</script>