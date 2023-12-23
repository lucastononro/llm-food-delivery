<template>
  <div class="button-container">
    <div class="btn-group">
      <div v-if="recordedVoiceURL" class="input-btn" @click="cancelAudio">
        <vue-feather type="trash-2" size="16"></vue-feather>
      </div>
      <div class="input-btn" @click="toggleRecording" v-if="!isRecordingFlag">
        <vue-feather type="mic" size="16"></vue-feather>
      </div>
      <div class="input-btn" @click="toggleRecording" v-if="isRecordingFlag">
        <vue-feather type="pause" size="16"></vue-feather>
      </div>
      <div class="input-btn" @click="sendMessage(value)" v-if="recordedVoiceURL">
        <vue-feather type="navigation" size="16"></vue-feather>
      </div>
    </div>
    
  </div>
</template>

<script>
import VueFeather from "vue-feather";

export default {
  name: "InputButtons",
  model: {
    prop: "newMessage",
    event: "update:newMessage",
  },
  components: {
    VueFeather,
  },
  props: {
    isRecordingFlag: {
      type: Boolean,
      required: true,
    },
    recordedVoiceURL: {
      type: String,
      default: null,
    },
  },
  methods: {
    cancelAudio() {
      this.$emit("cancel-audio");
    },
    toggleRecording() {
      this.$emit("toggle-recording");
    },
    sendMessage(message) {
    this.$emit("update:newMessage", message);
    this.$emit("send-message", message);
    },
  },
};
</script>