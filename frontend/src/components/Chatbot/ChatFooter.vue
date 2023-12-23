<template>
  <div class="card-footer card-chat-footer">
    <!-- <suggested-questions
      :questions="questions"
      @select-suggested-question="selectSuggestedQuestion"
    ></suggested-questions> -->

    <div class="input-group">
      <message-input
        v-model="newMessage"
        :isRecordingFlag="isRecordingFlag"
        :recordedVoiceURL="recordedVoiceURL"
        :msgPlaceholder="config.msgPlaceholder"
        :timeRecorded="timeRecorded"
        @send-message="sendMessage"
      >
      </message-input>
      <div class="input-group-append">
        <input-buttons
          v-model="newMessage"
          :isRecordingFlag="isRecordingFlag"
          :recordedVoiceURL="recordedVoiceURL"
          @cancel-audio="cancelAudio"
          @toggle-recording="toggleRecording"
          @send-message="sendMessage"
        ></input-buttons>
      </div>
    </div>
  </div>
</template>

<script>
import InputButtons from "./InputButtons.vue";
import MessageInput from "./MessageInput.vue";

export default {
  name: "ChatFooter",
  props: {
    isRecordingFlag: {
      type: Boolean,
      required: true,
    },
    recordedVoiceURL: {
      type: String,
      default: null,
    },
    timeRecorded: {
      type: Number,
      required: true,
    },
    config: {
      type: Object,
      required: true,
    },
  },
  components: {
    InputButtons,
    MessageInput,
  },
  data() {
    return {
      newMessage: "",
    };
  },
  methods: {
    sendMessage(message) {
      this.$emit("send-message", message);
    },
    cancelAudio() {
      this.$emit("cancel-audio");
    },
    toggleRecording() {
      this.$emit("toggle-recording");
    },
  },
};
</script>