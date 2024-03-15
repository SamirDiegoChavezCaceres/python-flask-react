import logo from './logo.svg';
import React from 'react';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';


import {About} from './components/About';
import {Items} from './components/Items';
import {Navbar} from './components/Navbar';


function App() {
  return (
    <Router>
      <Navbar/>
      <div className='container p-4'>
        <Routes>
          <Route path="/" element={<Items/>} />
          <Route path="/about" element={<About/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
