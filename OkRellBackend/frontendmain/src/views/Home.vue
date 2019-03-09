<template>
	<div id="home">		
		<div class="paraImg1">
			<div class="caption">
				<h1>
					Lorem ipsum dolor sit amet, consectetur.
				</h1>
				<p>
					Get amazing razors and world-class grooming products delivered for just a few bucks
				</p>
				<LinkButton size="lg" text="GET STARTED" action="getstarted"></LinkButton>
			</div>
		</div>
		<div class="paraImg2">
			<div class="caption">
				<h1>
					Lorem ipsum dolor sit amet, consectetur.
				</h1>
				<p>
					Get amazing razors and world-class grooming products delivered for just a few bucks
				</p>
				<LinkButton size="lg" text="VIEW PRODUCTS" action="products"></LinkButton>
			</div>
		</div>
		<div class="section section-light paraImg3">
		 	<div class="row">
		 		<h2>Three reasons to try okrell</h2>
				<div class="col-md">
					<img src="../assets/heart-box.svg" class="icon form-group">
					<h4 class="form-group">Lorem ipsum dolor sit.</h4>
					<span class="form-group">
						Our boxes don't just come with the best gromming items but they are packed with love.
					</span>
				</div>
				<div class="col-md">
					<img src="../assets/prison.svg" class="icon form-group">
					<h4 class="form-group">Lorem ipsum dolor sit.</h4>
					<span class="form-group">
						We don't believe in trapping customers an never letting them go. 
						With Okrell you are free to leave whenever you'd like. 
					</span>
				</div>
				<div class="col-md">
					<img src="../assets/calendar.svg" class="icon form-group">
					<h4 class="form-group">Lorem ipsum dolor sit.</h4>
					<span class="form-group">
						When we say that your box will be there on the 19th, it will be there on the 19th.
					</span>
				</div>
			</div class="row">
		</div>
	</div>
</template>

<style scoped>
/*Begin home container settings*/
/*End home container settings*/
/*Begin parallax effect styles*/
.paraImg1, .paraImg2, .paraImg3{
	position: relative;
	opacity: 0.75;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	background-attachment: fixed;
}
.paraImg1{
	background-image: url('../assets/backimgone.jpeg');
	min-height: 100vh;
}

.paraImg2{
	background-image: url('../assets/backimgtwo.jpg');
	min-height: 100vh;
}
.paraImg3{
	min-height: 80vh;
}
/*End parallax effect styles*/

/*Begin Caption styles */
.caption {
	position: absolute;
	top: 40%;
	left: 50%;
	transform: translate(-50%, -50%);
	color: white;
	font-family: 'Arial';
	text-align: center;
}
/*End Caption styles */

/*Begin button styles */
.button {
	background-color: #42b983;
}
/*End button styles */

/*Begin section container settings*/
.section{
	text-align: center;
	padding: 3%;
}
.section h2{
	margin-bottom: 30px;
}
.icon{
	max-height: 12vw;
}
.section span{
	padding: 
}
/*End section container settings*/
/*Begin row col-md styles*/
.row {
	width: 80%;
	padding: 3% 10%;
}
.col-md {
	padding:0 3.15%; 
	width: 27%;
	float: left;
}
/*End  row col-md styles*/
/* Being media querries */
@media only screen and (max-width: 768px) {
	.col-md {
		width: 100%;
	}
}
/* End media querries */
</style>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'
import LinkButton from '@/components/Inputs/LinkButton.vue'

export default {
  name: 'home',
  components: {
  	LinkButton,
  }
}
</script>
