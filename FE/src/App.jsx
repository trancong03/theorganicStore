import React, { useEffect, useState } from "react";
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
    setUserInfo(data.person); 
    localStorage.setItem('userInfo', JSON.stringify(data.person));
    setShowLogin(false); 
  };

  useEffect(() => {
    const storedUserInfo = localStorage.getItem('userInfo');
    if (storedUserInfo) {
      setUserInfo(JSON.parse(storedUserInfo)); 
    }
    console.log(userInfo);
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
        <Header userInfo={userInfo} setUserInfo={setUserInfo} onLoginClick={handleLoginClick} cartItems={cartItems} className="fixed top-0 left-0 w-full bg-white shadow-md z-50" />
        {showLogin && <DN closeLogin={closeLogin} onLoginSuccess={handleLoginSuccess} />}

        <Routes>
          <Route path="/" element={<Home onAddToCart={handleAddToCart}/>}/>
          <Route path="/account/*" element={<Account user={userInfo} setUserInfo={setUserInfo} />}>
            <Route path="info" element={<InfomationAccount user={userInfo} setUserInfo={setUserInfo} />} />
            <Route path="reset-password" element={<ResetPassWord user={userInfo} />} />
          </Route>
          <Route path="*" element={<ErrorPage />} />
        </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
