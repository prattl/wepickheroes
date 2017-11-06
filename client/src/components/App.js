import React, { Component } from 'react';
import {
    Redirect,
    Route,
} from 'react-router-dom'

import Index from './Index'
import { Footer, Navigation } from './layout'

class App extends Component {
    render() {
        return (
            <div>
                <Navigation/>
                <Route exact path="/" render={() => <Redirect to="/wepickheroes" />} />
                <Route path="/wepickheroes" component={Index} />
                <Footer />
            </div>
        );
    }
}


export default App;
