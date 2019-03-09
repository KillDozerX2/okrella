<template>
	<div class="linkbutton">
		<router-link tag="div" v-bind:to="action">{{ text }}</router-link>
	</div>
</template>

<style scoped>
.linkbutton {
	position: relative;
	height: 50px;
	width: auto;
}
.linkbutton div{
	position: absolute;
	top: 50%;
	left:50%;
	transform: translate(-50%, -50%);
	cursor: pointer;
	background-color: #42b983;
	border-radius: 5px;
	padding: 4px 6px;
}
.linkbutton:hover {
	/* Write hover animation for link button */
}
</style scoped>

<script>
export default {
	name: 'linkbutton',
	props: [
		'text',
		'action',
		'size',
	],
	methods: {
		debug: function () {
			console.log("Testing");
		},
	}
}
</script>
