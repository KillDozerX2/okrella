import React from 'react';
import ReactDOM from 'react-dom';
// main css file import for the index page 
import './index.css';
// importing the App component. which will serve as the main component
import App from './App';
// this service worker is something cool.
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
serviceWorker.unregister();
