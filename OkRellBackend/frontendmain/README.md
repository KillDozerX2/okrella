## Available Actions
### cd to the frontendmain directory first.

## These are the following actions that need to be taken when developing new components or making changes.

```
npm install
```
## Project setup
Installs all the dependencies for the project.

```
npm run serve
```
### Compiles and hot-reloads for development

Runs the app in the development mode.<br>
Open http://localhost:3000 to view it in the browser.

npm development server offers hot reloads, it reloads everytime you save your changes<br>
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br>
See the section about [running tests] for more information.


```
npm run build
```
### Compiles and minifies for production
Builds the app for production to the `build` folder.<br>
The exported index.html will be rendered using Template.as_view() method in django which will give out front-end control completely to React.

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## This is the main scheme for the css followed.
Always include your Css in the correct commented blocks like This
```
/* Begin name of block, semantically understood */
/* End name of block, semantically understood */
```

## New vue instance template
```
<template>
	<div id="Name of your component in lowercase">
		
	</div>
</template>

<style scoped>

</style scoped>

<script>
// @ is an alias to /src
// Import your components here.
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
	name: 'Name of your component in lowercase',
	components: {
		
	}
}
</script>

```

## Getting json data
#### Install axios if not installed by npm install with apckage.json, Seriosly talk to me if this happens

`npm install --save axios`
