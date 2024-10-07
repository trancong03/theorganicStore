import { Heart, LogOut, Search, SettingsIcon, ShoppingCart, UserCircle } from "lucide-react";
import React, { useState, useEffect, useRef } from "react";
import Navbar from "./Navbar";

export default function Header({ onLoginClick, userInfo, setUserInfo, }) {
  const [isSticky, setIsSticky] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(userInfo ? true : false);
  const menuRef = useRef(null);
  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 100) { // Adjust this value based on your header height
        setIsSticky(true);
      } else {
        setIsSticky(false);
      }
    };

    window.addEventListener('scroll', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const handleSettingsClick = () => {
    if (!userInfo) {
      onLoginClick();
    }
    else {
      navigate('/account');
    }
  };
  // Đóng menu khi nhấp ra ngoài
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setIsMenuOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [menuRef]);

  const handleAuthClick = () => {
    if (isLoggedIn) {
      setUserInfo(null); // Đặt lại thông tin người dùng
      setIsLoggedIn(false); // Cập nhật trạng thái đăng nhập
    } else {
      onLoginClick();
    }
    setIsLoggedIn(!isLoggedIn);
    setIsMenuOpen(false);
  };
  return (
    <div className={`transition-all duration-300 ${isSticky ? 'fixed top-0 left-0 w-full shadow-md z-50' : ''}`}>
      <div className="h-[10vh] flex items-center bg-white p-3 ">
        <div className="ml-[15vw] mr-5">
          <img
            className="h-12 sm:h-8 md:h-10 lg:h-16 w-auto"
            src="/image/logo.png"
            alt="The CIU Logo"
          />
        </div>
        <div className="hidden lg:flex items-center py-2 rounded-2xl h-[7vh] w-[40vw] bg-[#f3f3f3]">
          <input
            className="ml-2 w-[37vw] bg-transparent focus:outline-none placeholder-gray-500 text-gray-700"
            type="text"
            placeholder="Tìm sản phẩm..."
          />
          <button>
            <Search />
          </button>
        </div>
        <div className="ml-3 flex gap-4 justify-center items-center">
          <Heart />
          <ShoppingCart />
          <div className="px-3 py-2 h-10 w-[20vw] bg-transparent rounded-3xl flex items-center justify-start relative ">
            <nav className="relative">
              <a
                onClick={() => {
                  setIsMenuOpen(!isMenuOpen); 
                }}
                className={`text-[#5b5858cc] flex gap-2 items-center font-arial px-3 py-2`}
              >

                <img
                  src={userInfo ? `image/${userInfo.avatar}` : "/image/icon.png"}
                  alt=""
                  className="w-12 h-12 rounded-full"
                />
                {userInfo?.fullname || "Tài khoản"}

              </a>

              {/* Menu con bên dưới */}
              {isMenuOpen && (
                <div
                  ref={menuRef}
                  className="absolute top-[8.5vh] mt-2 bg-white border rounded shadow-md  w-48 z-50">
                  <ul>
                    <li className="py-2 px-3 hover:bg-gray-100">
                      <button className="w-full text-left flex items-center gap-2" onClick={handleSettingsClick}>
                        <SettingsIcon />
                        Cài đặt
                      </button>
                    </li>
                    <li className="py-2 px-3 hover:bg-gray-100">
                      <button className="w-full text-left flex items-center gap-2" onClick={handleAuthClick}>
                        <LogOut />
                        {userInfo ? "Logout" : "Login"}
                      </button>
                    </li>
                  </ul>
                </div>
              )}
            </nav>
          </div>
        </div>
     </div>
      <Navbar />
    </div>
  );
}
