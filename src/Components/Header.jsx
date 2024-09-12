import { Heart, Search, ShoppingCart, UserCircle } from "lucide-react";
import React from "react";

export default function Header() {
  return (
    <div className=" h-[12vh] flex items-center bg-white p-3">
      <div className="ml-[15vw] mr-5">
        <img
          className="h-12 sm:h-8 md:h-10 lg:h-16 w-auto"
          src="/image/logo.png"
          alt="The CIU Logo"
        />
      </div>
      <div className="hidden lg:flex items-center  py-2 rounded-2xl h-[7vh] w-[40vw] bg-[#f3f3f3]">
        <input
          className="ml-2 w-[37vw] bg-transparent focus:outline-none placeholder-gray-500 text-gray-700"
          type="text"
          placeholder="Tìm sản phẩm..."
        />
        <button>
          <Search />
        </button>
      </div>
      <div className=" ml-3 flex gap-4 justify-center items-center ">
        <Heart />
        <ShoppingCart />
        <div className="w-[10vw] h-[8vh] bg-[#434343] rounded-3xl flex items-center justify-center text-white font-bold gap-4">
          <UserCircle />
          <h4>Đăng Nhập</h4>
        </div>
        
      </div>
      
    </div>
  );
}
