<template>
	<div id="navbar">
		<b-navbar toggleable="md" type="light" variant="light">

			<b-navbar-toggle target="nav_collapse" />
			<div class="ml-5"></div><div class="ml-5"></div>
			<b-collapse is-nav id="nav_collapse">
				<b-navbar-nav class="">
					<b-nav-item to="getstarted">GET STARTED</b-nav-item>
					<b-nav-item to="products">PRODUCTS</b-nav-item>
					<!-- Will probably replace this with the brand logo -->
					<b-nav-item to="/">OKRELL</b-nav-item>
				</b-navbar-nav>

				<!-- Right aligned nav items -->
				<b-navbar-nav class="ml-auto">
					<b-nav-item to="/login">LOGIN</b-nav-item>
					<b-nav-item to="/box">BOX</b-nav-item>
					<b-nav-item to="/join">JOIN</b-nav-item>					
				</b-navbar-nav>
			</b-collapse>
			<div class="ml-5"></div><div class="ml-5"></div>
			<!-- <b-collapse is-nav></b-collapse> -->
		</b-navbar>
	</div>
</template>

<style scoped>
#navbar{
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 56px;
	z-index: 999;
}

#nav_collapse a {
  font-weight: bold;
}

#nav_collapse a.router-link-exact-active {
  color: #42b983;
}
</style scoped>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
	name: 'navbar',
	components: {
		
	}
}
</script>
