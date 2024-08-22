
import React from 'react';
import './App.css';

import 'swiper/css';
import 'swiper/css/free-mode';
import 'swiper/css/pagination';
import { BrowserRouter, Route, Router, Routes } from 'react-router-dom';
import Home from './UI/Home';
function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element ={<Home/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
