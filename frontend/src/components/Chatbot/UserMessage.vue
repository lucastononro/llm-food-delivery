<template>
  <div class="d-flex justify-content-end mb-4">
    <div class="container-user-msg">
      {{ message.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: "UserMessage",
  props: {
    message: {
      type: Object,
      required: true,
    },
  },
};
</script>