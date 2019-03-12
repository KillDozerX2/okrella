//This is the basic layout of a Vue app or component.
<template>
  <div id="app">
    <Navbar />
    <!-- This is the view that router loads up. -->
    <router-view id="mainView" />
    <Faqs />
    <Sitefooter />
  </div>
</template>

<style>
body, html{
  height:100%;
  margin:0;
  padding: 0;
  font-size:16px;
  font-family:"Lato", sans-serif;
  font-weight:400;
  line-height:1.8em;
  color:#666;
}
::selection {
  background: #42b983;
  color: white;
  }
::-moz-selection {
  background: #42b983;
  color: white;
}
#app {
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
  font-weight: 400;
  line-height: 1.8em;
  /*text-align: center;*/
  color: #666;
}
.router-link-exact-active {
  color: #42b983;
}
#mainView {
  padding-top: 56px;
}
</style>

<script>

import Navbar from '@/components/Navbar.vue'
import Sitefooter from '@/components/Sitefooter.vue'
import Faqs from '@/components/Faqs.vue'
export default {
  name: 'app',
  components: {
    Navbar,
    Sitefooter,
    Faqs,
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  methods: {
    
  },
}

</script>