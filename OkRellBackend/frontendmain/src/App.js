// This is boiler plate react code
// These imports are just needed for eract to work
import React, { Component } from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom'
// Import your components here
import Navbar from './Components/Navbar'

class App extends Component {
  render() {
    return (

		<div className="App">
			<Navbar/>
		</div>
    );
  }
}

export default App;
