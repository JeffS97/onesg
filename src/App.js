import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Footer, Home, Propose } from "./components";
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <Router>
        <Navigation />
        <Switch>
          <Route path="/" exact component={() => <Home />} />
          <Route path="/propose" exact component={() => <Propose />} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;


//<Route path="/about" exact component={() => <About />} />
//<Route path="/contact" exact component={() => <Contact />} />
