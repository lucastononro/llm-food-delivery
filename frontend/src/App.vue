<script setup>
	import VueFeather from 'vue-feather'
</script>

<script>
	import AppContainer from "./components/AppContainer.vue";

	export default {
		name: 'App',
		components: {
			AppContainer
		},
		data() {
			return {
				environment: import.meta.env.VITE_ENVIRONMENT,
			};
		}
	}
</script>

<template>
	<AppContainer />
</template>

<style scoped></style>
