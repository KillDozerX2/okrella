<template>
	<div id="navbar">
		<div class="mainMenu">
			<div id="menuIcon" @click="showHideMenu" >
	            <div id="menuLine"></div>
	        </div>
	        <ul class="hide-on-md">
	        	<router-link tag="li" to="/getstarted">GET STARTED</router-link>
	        	<router-link tag="li" to="/products">PRODUCTS</router-link>
	        	<router-link tag="li" to="/">HOME</router-link>
	        	<router-link tag="li" to="/login">LOGIN</router-link>
	        	<router-link tag="li" to="/join">JOIN</router-link>
	        	<router-link tag="li" to="/box">BOX</router-link>
	        </ul>
		</div>
        
        <div id="sideMenu" class="showing" v-bind:class="{ hidden: isHidden }">        	
            <ul>
            	<router-link tag="li" to="/">HOME</router-link>
            	<router-link tag="li" class="line" to="/getstarted">GET STARTED</router-link>
	        	<router-link tag="li" class="line" to="/products">PRODUCTS</router-link>
	        	<router-link tag="li" class="line" to="/login">LOGIN</router-link>
	        	<router-link tag="li" class="line" to="/join">JOIN</router-link>
	        	<router-link tag="li" class="line" to="/box">BOX</router-link>
	        	<li id="close" @click="showHideMenu">
	                <img src="../assets/Close.png" height="30px" width="30px"/>
	            </li>
            </ul>
        </div>
	</div>
</template>

<style scoped>
/* Being Main Menu Styles */
.mainMenu ul {
	height: 56px;
	list-style-type: none;
	margin: 0;
	padding: 0;
	overflow: hidden;
}
.mainMenu ul li {
	float: left;
	cursor: pointer;
	height: 100%;
	text-align: center;
	line-height: 36px;
	padding: 10px;
}
li:hover {
	background-color: #42b983;
	color: white;
	-webkit-transition: color 2s;
  	transition: color 2s;
	-webkit-transition: color 2s;
  	transition: color 2s;
}
/* End Main Menu Styles */
#navbar{
	background-color: white;
	border-bottom: 1px solid #42b983;
	z-index: 999;
	position: fixed;
	height: 56px;
	width: 100%;
}
/*Begin MenuIcon Styles*/
#menuIcon{
	display: none;
	position: absolute;
	top: 0;
	right: 5px;
	height: 49px;
	width: 49px;
	/*margin: 0;*/
	margin: 3.5px;
	cursor: pointer;
}
#menuLine{
    height: 4px;
    width: 50px;
    background-color: #42b983;
    position: absolute;
    top:50%;
    left: 50%;
    transform: translate(-50%,-50%);
    transition: all .3s;
    border-radius: 5%;
}
#menuIcon:hover #menuLine{
    width: 30px;
}
#menuLine::before{
    content: '';
    height: 4px;
    width: 40px;
    background-color: #42b983;
    position: absolute;
    margin-top: 10px;
    transition: all .3s;
}
#menuLine:hover #menuLine::before{
    width: 50px;
}
#menuLine::after{
    content: '';
    height: 4px;
    width: 40px;
    background-color:#42b983;
    position: absolute;
    margin-top: -10px;
    transition: all .3s;
}
#menuLine:hover #menuLine::after{
    width: 50px;
}
/*End MenuIcon Styles*/

/*Begin Side Menu Styles*/
.showing {
    height: 100%;
    width: 300px;
    background-color: #42b983;
    opacity: 0.98;
    -webkit-clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
	clip-path: polygon(0 0, 100% 0, 100% 100%, 0% 100%);
    position: fixed;

	-webkit-transition: -webkit-clip-path 1s ease-in-out;
  	transition: -webkit-clip-path 1s ease-in-out;
	-webkit-transition: clip-path 1s ease-in-out;
  	transition: clip-path 1s ease-in-out;
  	left: 0;
}
.hidden {
    height: 100%;
    width: 300px;
    background-color: #42b983;
    opacity: 0.98;
    -webkit-clip-path: polygon(0 0, 0 50%, 0 50%, 0% 100%);
	clip-path: polygon(0 0, 0 50%, 0 50%, 0% 100%);
    position: fixed;

	-webkit-transition: -webkit-clip-path 1s ease-in-out;
  	transition: -webkit-clip-path 1s ease-in-out;
	-webkit-transition: clip-path 1s ease-in-out;
  	transition: clip-path 1s ease-in-out;
  	/*left: -300px;*/
}
#sideMenu ul{
	height: 80%;
	width: 80%;
	margin: 10% 10% 10% 10%;
    list-style: none;
    padding: 0px;
    color: #ddd;
    text-align: center;
}
#sideMenu ul li{
    margin: 20px;
}
#sideMenu ul li{
    cursor: pointer;
}
.line{
    
}
#sideMenu ul li:hover .line{
    width: 180px;
}
/*End Side Menu Styles*/

/* Being media querries */
@media only screen and (max-width: 768px) {
	.hide-on-md{
		display: none;
	}
	#menuIcon {
	display: block;
	}
}
/* End media querries */
</style scoped>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
	name: 'navbar',
	components: {
		
	},
	data: function () {
		return {isHidden: true}
	},
	methods: {
		showHideMenu: function (event){
			this.isHidden = !this.isHidden
		}
	},
}
</script>
