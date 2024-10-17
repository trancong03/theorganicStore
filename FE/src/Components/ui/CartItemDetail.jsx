import React from "react";

export default function CartItemDetail({ item, onQuantityChange }) {
    return (
        <li className="flex items-center justify-between py-4">
            <div className="flex items-center space-x-4">
                {/* Product Image with Fallback */}
                <img
                    src={item.images && item.images[0] ? item.images[0] : "/path/to/placeholder.jpg"}
                    alt={item.name}
                    className="w-16 h-16 object-cover rounded-md"
                />
                {/* Product Info */}
                <div className="flex flex-col">
                    <h3 className="text-lg font-semibold text-gray-800">{item.name}</h3>
                    <p className="text-gray-500">{parseFloat(item.price).toLocaleString()} VND</p>
                </div>
            </div>
            
            {/* Quantity Adjustment */}
            <div className="flex items-center space-x-2">
                <button
                    className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-2 py-1 rounded"
                    onClick={() => onQuantityChange(item.id, -1)}
                >
                    -
                </button>
                <span className="w-8 text-center">{item.quantity}</span>
                <button
                    className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-2 py-1 rounded"
                    onClick={() => onQuantityChange(item.id, 1)}
                >
                    +
                </button>
            </div>
        </li>
    );
}
