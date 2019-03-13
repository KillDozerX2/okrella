import axios from 'axios'

export const API = {
	data: function() {
		return {
			apiInstance: axios.create({
				baseURL: 'http://127.0.0.1:8000/',
				headers: {'Authorization': 'Token 3752d9d11215a9db484a3ac66b832d471cd369d7'}
			}),
		}
	},
	methods: {
		/*
			This is the GET method that should be used across the app
			every request needs to call this
		*/
		getData(url) {
			this.apiInstance.get(url).then(function(response, request){
				console.log(response);
				console.log(request);
			});
		},
		/*
			This is the POST method that should be used across the app
			every request needs to call this
		*/
		postData(source) {
			console.log("This is a shared method")
		},
	}
}