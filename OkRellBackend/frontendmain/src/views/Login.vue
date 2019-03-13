<template>
	<div id="login">
		<button @click="getData('api/user/hello')">Do something</button>
		<h4>{{ getHello }}</h4>
	</div>
</template>

<style scoped>

</style scoped>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'
import { API } from '@/api.js'
export default {
	name: 'login',
	components: {
		
	},
	/*This is more of config data, don't get this confused with state*/
	data : function() {
		return {
			
		}	
	},
	computed: {
		getHello: function() {
			return this.$store.getters.getUserToken
		}
	},
	mixins:[API,],
	methods: {
		
	}
}
</script>