<template>
	<div id="login">
		<button @click="getHello">Do something</button>
	</div>
</template>

<style scoped>

</style scoped>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
	name: 'login',
	components: {
		
	},
	data : function() {
		return {
			srcUrl : "http://127.0.0.1:8000",
		}	
	},
	methods: {
		getHello : function() {
			console.log("Getting Data");
			/*These addresses need to be changed before pushing to production*/
			axios.get(this.srcUrl + '/api/user/hello/')
      			 	.then(response => {
      			 	console.log(response);
	      })
		}
	}
}
</script>