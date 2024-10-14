import React, { useEffect, useState } from "react";
import "./App.css";

import "swiper/css";
import "swiper/css/free-mode";
import "swiper/css/pagination";
import { BrowserRouter, Route, Router, Routes } from "react-router-dom";
import Footer from "./Components/Footer";
import ErrorPage from "./Components/ErrorPage";
import Navbar from "./Components/Navbar";
import Header from "./Components/Header";
import DN from './Components/DN';
import Home from "./Pages/Home";
function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [userInfo, setUserInfo] = useState({}); // Lưu trữ thông tin người dùng

  const handleLoginClick = () => {
    setShowLogin(true); // Khi click nút "Login", hiển thị DN
  };

  const closeLogin = () => {
    setShowLogin(false); // Đóng form đăng nhập
  };

  const handleLoginSuccess = (data) => {
    setUserInfo(data.user); // Cập nhật thông tin người dùng
    localStorage.setItem('userInfo', JSON.stringify(data.user));
    setShowLogin(false); // Đóng form đăng nhập
  };

  useEffect(() => {
    const storedUserInfo = localStorage.getItem('userInfo');
    if (storedUserInfo) {
      setUserInfo(JSON.parse(storedUserInfo)); // Tải thông tin từ localStorage
    }
  }, []);
  const [cartItems, setCartItems] = useState([]);

  const handleAddToCart = (item) => {
    setCartItems((prevItems) => [...prevItems, item]);
  };
  return (
    <>
      <Header userInfo={userInfo} setUserInfo={setUserInfo} onLoginClick={handleLoginClick} cartItems={cartItems} className="fixed top-0 left-0 w-full bg-white shadow-md z-50" />
      {showLogin && <DN closeLogin={closeLogin} onLoginSuccess={handleLoginSuccess} />}
      
      <BrowserRouter>
        <Routes>
          <Route path="/account" element={<DN />} />
          <Route path="/" element={<Home onAddToCart={handleAddToCart}/>}/>
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}

export default App;
