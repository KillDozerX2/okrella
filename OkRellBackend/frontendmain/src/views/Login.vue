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
/*import axios*/

export default {
	name: 'login',
	components: {
		
	},
	methods: {
		getHello : function() {
			console.log("Getting Data");
			axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      			 	.then(response => {
      			 	console.log(response.data.bpi);
	      })
		}
	}
}
</script>