//This is the basic layout of a Vue app or component.
<template>
  <div id="app">
    <Navbar />
    <!-- This is the router vie that router loads up. -->
    <router-view/>
  </div>
</template>

<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<script>

import Navbar from '@/components/Navbar.vue'
export default {
  name: 'app',
  components: {
    Navbar    
  }
}

</script>