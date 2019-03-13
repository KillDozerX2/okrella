import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'

Vue.use(Vuex)

export const site_store = new Vuex.Store({
	state: {
		user_token: 'RandomToken',
		user: {},
		selected_products: [],
	},
	getters: {
		/* This is the get method for the user_token state variable*/
		getUserToken: state => {
			return state.user_token
		},
		/* This is the get method for the user state variable*/
		getUser: state => {
			return state.user
		},
		/* This is the get method for the selected_products state variable*/
		getSelectedProducts: state => {
			return state.selected_products
		},
	},
	mutations: {

	}
});