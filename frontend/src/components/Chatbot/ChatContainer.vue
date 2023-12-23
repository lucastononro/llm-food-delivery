<template>
  <div class="chat-container" :class="{ 'minimized': !isChatOpen }">
    <div class="card card-chat">
      <chat-header 
        :ImageHeader="config.images.header_image"
        :config="config"
        :isMinimized="!isChatOpen"
        :handsFreeFlag="handsFreeFlag"
        @toggle-chatbot="toggleChatBot"
        @toggle-handsfree="$emit('toggle-handsfree')"
      >
      </chat-header>

      <chat-body
        v-show="isChatOpen"
        ref="chatMessages" 
        :messages="messages"
        :config="config"
        :userTranscribing="userTranscribing"
        :botTyping="botTyping"
        :botTypingMsg="botTypingMsg"
        :baseApiUrl="baseApiUrl"
        :handsFreeFlag="handsFreeFlag"
      >
      </chat-body>

      <chat-footer 
        v-show="isChatOpen"
        ref="chatFooter"
        :config="config"
        :isRecordingFlag="isRecordingFlag"
        :recordedVoiceURL="recordedVoiceURL"
        :timeRecorded="timeRecorded"
        @toggle-recording="toggleRecording"
        @cancel-audio="cancelAudio"
        @send-message="sendMessage"
        @select-suggested-question="selectSuggestedQuestion"
      >
    </chat-footer>
    </div>
  </div>
</template>

<script>
import ChatHeader from "./ChatHeader.vue";
import ChatFooter from "./ChatFooter.vue";
import ChatBody from "./ChatBody.vue";

import '../styles/chatbot.css'


export default {
  name: "ChatContainer",
  props: {
    config: {
      type: Object,
      required: true,
    },
    messages: {
      type: Array,
      required: true,
    },
    isRecordingFlag: {
      type: Boolean,
      required: true,
    },
    recordedVoiceURL: {
      type: String,
      required: true,
    },
    timeRecorded: {
      type: Number,
      required: true,
    },
    botTyping: {
      type: Boolean,
      required: true,
    },
    botTypingMsg: {
      type: String,
      required: false,
      default: null
    },
    userTranscribing: {
      type: Boolean,
      required: true,
    },
    isChatOpen: {
      type: Boolean,
      required: true,
    },
    handsFreeFlag: {
      type: Boolean,
      required: true,
    },
  },
  components: {
    ChatHeader,
    ChatFooter,
    ChatBody,
  },
  data() {
    return {
    };
  },
  watch: {
    isChatOpen(newValue) {
      if (newValue) {
        // Chat is opening
        this.animateChatOpening();
      } else {
        // Chat is closing
        this.animateChatClosing();
      }
    },
  },

  methods: {
    // Messages handling
    sendMessage(message) {
      this.$emit("send-message", message);
    },
    toggleRecording() {
      this.$emit("toggle-recording");
    },
    cancelAudio() {
      this.$emit("cancel-audio");
    },
    toggleChatBot() {
      this.$emit("toggle-chatbot");
    },
    animateChatOpening() {
      this.$nextTick(() => {
        // Assuming .chat-body and .chat-footer are the elements to animate
        const chatBody = this.$refs.chatBody;
        const chatFooter = this.$refs.chatFooter;

        // Set initial styles for animation start state
        chatBody.style.display = 'none';
        chatFooter.style.display = 'none';

        // Start the animation for the chat container height
        this.$el.style.height = '70vh';

        // After a delay (to sync with the container height animation), show chat body and footer
        setTimeout(() => {
          chatBody.style.display = '';
          chatFooter.style.display = '';
          chatBody.style.opacity = '0';
          chatFooter.style.opacity = '0';

          // Fade in the chat body and footer
          chatBody.style.transition = 'opacity 0.5s ease';
          chatFooter.style.transition = 'opacity 0.5s ease';
          chatBody.style.opacity = '1';
          chatFooter.style.opacity = '1';
        }, 500); 
      });
    },
    animateChatClosing() {
      // Assuming .chat-body and .chat-footer are the elements to animate
      const chatBody = this.$refs.chatBody.$el; 
      const chatFooter = this.$refs.chatFooter.$el;

      // Fade out the chat body and footer with a transition
      chatBody.style.transition = 'opacity 0.5s ease';
      chatFooter.style.transition = 'opacity 0.5s ease';
      chatBody.style.opacity = '0';
      chatFooter.style.opacity = '0';

      // Wait for the fade-out transition to finish before minimizing the container
      setTimeout(() => {
        this.$el.classList.add('minimized');
      }, 500); 
    },
  }
};
</script>