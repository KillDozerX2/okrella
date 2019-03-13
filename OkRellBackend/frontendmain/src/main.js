//This is the main.js file
// DO NOT TOUCH THIS
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { site_store } from './store.js'

Vue.config.productionTip = false

new Vue({
  el: "#app",
  router,
  store: site_store,
  render: h => h(App)
}).$mount('#app')
