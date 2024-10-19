// src/App.js
import React, { useState, useEffect } from "react";
import "./App.css";
import "swiper/css";
import "swiper/css/free-mode";
import "swiper/css/pagination";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Footer from "./Components/Footer";
import ErrorPage from "./Components/ErrorPage";
import Header from "./Components/Header";
import DN from './Components/DN';
import Home from "./Pages/Home";
import Cart from "./Pages/Cart";
import Account from './Pages/Account';
import InfomationAccount from "./Components/ui_user_account/InfomationAccount";
import ResetPassWord from "./Components/ui_user_account/ResetPassWord";
import { CartProvider } from './Components/context/CardContext'; 
function App() {
  const [showLogin, setShowLogin] = useState(false);
  const [userInfo, setUserInfo] = useState({});

  const handleLoginClick = () => {
    setShowLogin(true);
  };

  const closeLogin = () => {
    setShowLogin(false);
  };

  const handleLoginSuccess = (data) => {
    setUserInfo(data.person);
    localStorage.setItem('userInfo', JSON.stringify(data.person));
    setShowLogin(false);
  };

  const handleAddToCart = async (item, personID) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/add_product_to_Cart/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          product_id: item.ProductID,
          person_id: personID,
        }),
      });
      const result = await response.json();
      if (result.success) {
        console.log('Product added to cart successfully');
      } else {
        console.log('Failed to add product to cart');
      }
    } catch (error) {
      console.error('Error adding product to cart:', error);
    }
  };

  useEffect(() => {
    const storedUserInfo = localStorage.getItem('userInfo');
    if (storedUserInfo) {
      setUserInfo(JSON.parse(storedUserInfo));
    }
  }, []);

  return (
    <CartProvider personID={userInfo.iduser}>
      <BrowserRouter>
        <Header userInfo={userInfo} setUserInfo={setUserInfo} onLoginClick={handleLoginClick} />
        {showLogin && <DN closeLogin={closeLogin} onLoginSuccess={handleLoginSuccess} />}

        <Routes>
          <Route path="/" element={<Home onAddToCart={(item) => handleAddToCart(item, userInfo.iduser)} />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/account/*" element={<Account user={userInfo} setUserInfo={setUserInfo} />}>
            <Route path="info" element={<InfomationAccount user={userInfo} setUserInfo={setUserInfo} />} />
            <Route path="reset-password" element={<ResetPassWord user={userInfo} />} />
          </Route>
          <Route path="*" element={<ErrorPage />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </CartProvider>
  );
}

export default App;
