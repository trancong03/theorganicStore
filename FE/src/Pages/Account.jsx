import React from "react";
import { Routes, Route } from "react-router-dom"; // Import Routes và Route
import InfomationAccount from './../Components/ui_user_account/InfomationAccount';
import ResetPassWord from './../Components/ui_user_account/ResetPassWord';
import NavigationAccount from './../Components/ui_user_account/navigationAccount';
import Cart from './Cart';

export default function Account({ user, setUserInfo }) {
  return (
    <div className="mx-auto w-full bg-transparent shadow-lg rounded-md flex justify-between items-start gap-4 ml-5 mt-3 h-auto">
      {/* Khối NavigationAccount ở bên phải */}
      <NavigationAccount user={user} setUserInfo={setUserInfo} />

      {/* Khối hiển thị nội dung */}
      <div className="flex-1">
        <Routes>
          <Route path="/" element={<InfomationAccount user={user} setUserInfo={setUserInfo} />} />
          <Route path="reset-password" element={<ResetPassWord user={user} />} />
          <Route path="cart" element={<Cart />} />
        </Routes>
      </div>
    </div>  
  );
}
