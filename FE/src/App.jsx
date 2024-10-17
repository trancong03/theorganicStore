import React, { useEffect, useState } from "react";
import "./App.css";
import "swiper/css";
import "swiper/css/free-mode";
import "swiper/css/pagination";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Footer from "./Components/Footer";
import ErrorPage from "./Components/ErrorPage";
import Navbar from "./Components/Navbar";
import Header from "./Components/Header";
import DN from './Components/DN';
import Home from "./Pages/Home";
import Cart from "./Pages/Cart";

function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [userInfo, setUserInfo] = useState({}); // Lưu trữ thông tin người dùng
  const [cartItems, setCartItems] = useState([]);

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

  const handleAddToCart = (item) => {
    // Check if the item with the same ID already exists in the cart
    const isDuplicate = cartItems.some(cartItem => cartItem.id === item.id);
    
    if (!isDuplicate) {
      setCartItems((prevItems) => [...prevItems, item]);
    } else {
      alert("Sản phẩm đã có trong giỏ hàng!"); // Alert the user about the duplicate item
    }
  };

  return (
    <BrowserRouter>
      <Header userInfo={userInfo} setUserInfo={setUserInfo} onLoginClick={handleLoginClick} cartItems={cartItems} />
      {showLogin && <DN closeLogin={closeLogin} onLoginSuccess={handleLoginSuccess} />}
      
      <Routes>
        <Route path="/account" element={<DN />} />
        <Route path="/cart" element={<Cart cartItems={cartItems}/>} />
        <Route path="/" element={<Home onAddToCart={handleAddToCart} />} />
        <Route path="*" element={<ErrorPage />} />
      </Routes>

      <Footer />
    </BrowserRouter>
  );
}

export default App;
