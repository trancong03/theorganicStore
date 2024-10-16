import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Nhập Link từ react-router-dom
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEnvelope, faLocationDot, faShare, faPlus } from '@fortawesome/free-solid-svg-icons';
import { BellRing, Heart, Info, ListOrdered, LogOut, TimerReset, Wallet } from 'lucide-react';

export default function NavigationAccount({ user, setUserInfo }) {
    const [avatarImage, setAvatarImage] = useState(`image/${user.avatar || 'default-avatar.jpg'}`); // Thay 'default-avatar.jpg' bằng đường dẫn tới hình ảnh mặc định

    useEffect(() => {
        setAvatarImage(`/image/${user.avatar || 'cong.jpg'}`);
    }, [user]);

    const handleAvatarChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setAvatarImage(reader.result);
            };
            setAvatarFile(file); // Lưu file để gửi lên máy chủ
            reader.readAsDataURL(file);
        }
    };

    const handleSubmit = async () => {
    
};

    return (
       <>
            {/* <div className='w-[30vw]'>
                <div className="max-w-md mx-auto bg-white rounded-lg overflow-hidden shadow-md p-4 text-md">
                    <div className="relative">
                        <div className="absolute top-2 right-2">
                            <label htmlFor="cover-upload" className="border rounded p-1 bg-white cursor-pointer opacity-70">
                                <FontAwesomeIcon icon={faPlus} className="text-gray-600" />
                            </label>
                        </div>
                        <div className="absolute -bottom-8 left-4">
                            <img
                                src={avatarImage}
                                alt="User"
                                className="w-16 h-16 rounded-full border-4 border-white"
                            />
                            <div className="absolute bottom-0 right-0">
                                <input
                                    type="file"
                                    accept="image/*"
                                    onChange={handleAvatarChange}
                                    id="avatar-upload"
                                    className="hidden"
                                />
                                <label htmlFor="avatar-upload" className="border rounded p-1 bg-white cursor-pointer opacity-70">
                                    <FontAwesomeIcon icon={faPlus} className="text-gray-600" />
                                </label>
                            </div>
                        </div>
                    </div>
                    <br />
                    <div className="mt-3 pl-4">
                        <h2 className="text-xl font-semibold">{user.fullname}</h2>
                        <div className="flex items-center">
                            <span className="text-yellow-500 text-sm">★★★★☆</span>
                            <span className="ml-2 text-sm">(1 nhận xét)</span>
                            <span className="ml-2 text-blue-500">Đã xác thực</span>
                        </div>
                        <div className='pt-3 pb-3 text-slate-500 text-lg'>
                            <h1>Người theo dõi : <b>0</b> |  Đang theo dõi:  <b>0</b></h1>
                        </div>
                        <p className="text-gray-600 mt-2 text-md">
                            <FontAwesomeIcon icon={faLocationDot} /> {user.address}
                        </p>
                        <p className="text-sm text-gray-600 mt-2 text-md">
                            <FontAwesomeIcon icon={faEnvelope} />  {user.email}
                        </p>
                    </div>
                    <button onClick={handleSubmit} className='border p-2 w-[80%] border-solid rounded-xl font-bold bg-orange-400 text-white text-lg mt-3 flex items-center justify-center gap-2'>
                        <FontAwesomeIcon icon={faShare} />
                        <h1>Cập Nhật Hình Ảnh</h1>
                    </button>
                    <Link to="/account">
                        <button className='border p-2 w-[80%] hover:bg-slate-300 border-solid rounded-xl font-bold text-lg mt-3'>
                            Chỉnh Sửa Trang Cá Nhân
                        </button>
                    </Link>
                    <Link to="/account/reset-password"> {/* Sử dụng Link để điều hướng */}
            {/* <button className='border p-2 w-[80%] hover:bg-slate-300 border-solid rounded-xl font-bold text-lg mt-3'>
                            Thay đổi mật khẩu
                        </button>
                    </Link>
                </div>

            </div>  */}
            <div className="w-1/4 p-4 bg-white shadow-md h-[100vh]">
                <div className="flex items-center mb-4">
                    <img
                        src={avatarImage}
                        alt="Avatar"
                        className="w-16 h-16 rounded-full border-4 border-white"
                    />
                    <span className="font-bold text-lg">{user.name}</span>
                </div>
                <ul className='space-y-4'>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200 ' >
                        <ListOrdered/>
                        <a href="/orders" className="block p-2 rounded">Quản lý đơn hàng</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <BellRing/>
                        <a href="/notifications" className="block p-2 rounded">Thông báo</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <Heart/>
                        <a href="/favorites" className="block p-2 rounded">Sản phẩm yêu thích</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <Info/>
                        <a href="/account" className="block p-2 rounded">Thông tin tài khoản</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <FontAwesomeIcon icon={faLocationDot} />
                        <a href="/address" className="block p-2 rounded">Số địa chỉ</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <Wallet/>
                        <a href="/vouchers" className="block p-2 rounded">Ví voucher</a></li>
                    <li className='flex justify-start ml-3 items-center  hover:bg-gray-200'>
                        <LogOut/>
                        <a href="/logout" className="block p-2 rounded">Đăng xuất</a></li>
                    <li className='flex justify-start ml-3 h-full items-center  hover:bg-gray-200'>
                        <TimerReset />
                        <a href="/account/reset-password" className="block p-2 rounded">
                            Thay đổi mật khẩu</a></li>
                </ul>
            </div>
       </>
    );
}
