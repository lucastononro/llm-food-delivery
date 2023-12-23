<template>
  <textarea
    v-if="(!isRecordingFlag) && (recordedVoiceURL==null)"
    name=""
    v-model="messageToBeSent"
    class="form-control type_msg"
    :placeholder="msgPlaceholder"
    :disabled="isRecordingFlag"
    @keyup.enter="sendMessage(messageToBeSent)"
    style="resize:none;"
  ></textarea>
  <span class="form-control type_msg recording-input" v-if="isRecordingFlag"
    > {{ formatTime(timeRecorded) }}
  </span>
  <audio 
    class="form-control type_msg recording-input"
    v-if="recordedVoiceURL" :src="recordedVoiceURL" controls>
  </audio>
</template>

              
<script>

export default {
  name: "MessageInput",
  model: {
    prop: "newMessage",
    event: "update:newMessage",
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
    msgPlaceholder: {
      type: String,
      required: true,
    },
    timeRecorded: {
      type: Number,
      required: true,
    },
  },
  emits: ["send-message", "update:newMessage",],
  data() {
    return {
      messageToBeSent: "",
    } 
  },
  methods: {
    sendMessage(message) {
      this.$emit("update:newMessage", message);
      this.$emit("send-message", message);
      this.messageToBeSent = "";
    },
    formatTime(milliseconds) {
      let totalSeconds = Math.floor(milliseconds / 1000);
      let minutes = Math.floor(totalSeconds / 60);
      let seconds = totalSeconds % 60;
      let formattedTime = `${minutes.toString().padStart(2, "0")}:${seconds
        .toString()
        .padStart(2, "0")}`;
      console.log(formattedTime)
      return formattedTime;
    },
  },
};
</script>