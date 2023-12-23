<template>
  <div class="card-body card-chat-body" ref="pageChat">
    <div class="user-message" v-for="(message, index) in messages" v-bind:key="message.content">
      <div v-if="message.role == 'assistant'">
        <bot-message
          v-if="message.role == 'assistant'"
          :ImageMessageBot="config.images.bot_image"
          :message="message"
          :baseApiUrl="baseApiUrl"
          :autoPlayAudio="shouldAutoPlay(message)"
        >
        </bot-message>
      </div>
      <div v-else-if="message.role == 'user'">
        <user-message
          :userProfilePic="config.images.user_profile_pic"
          :message="message"
        >
        </user-message>
      </div>
    </div>
      <typing-message v-if="userTranscribing" v-slot:user-transcribing
            :profilePic="config.images.user_profile_pic"
            :message="config.transcribingMsg" 
            :isBot="false"
          >
      </typing-message>
      <typing-message v-if="botTyping" v-slot:bot-typing 
        :profilePic="config.images.bot_image" 
        :message="this.getTypingMsg(botTypingMsg)"
        :isBot="true"
        :key="this.getTypingMsg(null)"
      >
      </typing-message>
  </div>
</template>

<script>
import BotMessage from './BotMessage.vue';
import UserMessage from './UserMessage.vue';
import TypingMessage from './TypingMessage.vue';


export default {
  name: "ChatBody",
  props: {
    config: {
      type: Object,
      required: true,
    },
    messages: {
      type: Array,
      required: true,
    },
    userTranscribing: {
      type: Boolean,
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
    baseApiUrl: {
      type: String,
      required: true,
    },
    handsFreeFlag: {
      type: Boolean,
      required: true,
    },
  },
  components: {
    BotMessage,
    UserMessage,
    TypingMessage
  },
  methods: {
    getTypingMsg: function(msg){
      if (msg == null) {
        return this.config.typingMsg
      }
      return msg
    },
    shouldAutoPlay(message) {
      let flag = message.role === 'assistant' && this.handsFreeFlag;
      return flag
    },
    watch: {
      messages(newMessages, oldMessages) {
        // Check if a new message has been added
        if (newMessages.length > oldMessages.length) {
          const newMessage = newMessages[newMessages.length - 1];
          // Check if the new message is from the assistant and if handsFreeFlag is true
          if (newMessage.role === 'assistant' && this.handsFreeFlag) {
            // Find the BotMessage component for the new message and play its audio
            const botMessageComponent = this.$children.find(
              (component) => component.message === newMessage && component instanceof BotMessage
            );
            if (botMessageComponent) {
              botMessageComponent.playAudio();
            }
          }
        }
      },
    },
  }
};
</script>