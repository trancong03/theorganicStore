import React from "react";

export default function CartItemDetail({ item, onQuantityChange }) {
    return (
        <li className="flex items-center justify-between py-4">
            <div className="flex items-center space-x-4">
                <img
                    src={`image/product/${item.ImageID && item.ImageID[0] ? item.ImageID[0] : 'cong.jpg'}`} // Đảm bảo 'cong.jpg' được đặt trong dấu nháy đơn
                    alt={item.name}
                    className="w-16 h-16 object-cover rounded-md"
                />
                <div className="flex flex-col">
                    <h3 className="text-lg font-semibold text-gray-800">{item.Name}</h3>
                    <p className="text-gray-500">{parseFloat(item.Price).toLocaleString()} VND</p>
                </div>
            </div>
            
            <div className="flex items-center space-x-2">
                <button
                    className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-2 py-1 rounded"
                    onClick={() => onQuantityChange(item.ProductID, -1)}
                >
                    -
                </button>
                <span className="w-8 text-center">{item.quantity}</span>
                <button
                    className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-2 py-1 rounded"
                    onClick={() => onQuantityChange(item.ProductID, 1)} 
                >
                    +
                </button>
            </div>
        </li>
    );
}
