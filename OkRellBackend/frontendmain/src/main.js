//This is the main.js file
// DO NOT TOUCH THIS
import Vue from 'vue'
import App from './App.vue'
import router from './router'
// //Bootstrap imports
// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// Vue.use(BootstrapVue)
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
