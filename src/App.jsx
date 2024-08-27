import React from "react";
import "./App.css";

import "swiper/css";
import "swiper/css/free-mode";
import "swiper/css/pagination";
import { BrowserRouter, Route, Router, Routes } from "react-router-dom";
import Home from "./Pages/Home";
import Login from "./Pages/Login";
import Footer from "./Components/Footer";
import ErrorPage from "./Components/ErrorPage";
import Navbar from "./Components/Navbar";
import Header from "./Components/Header";
function App() {
  return (
    <>
      <Header />
      <Navbar />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;
