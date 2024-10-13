import React from 'react';

export default function MyShoppingCart({ cartItems }) {
  return (
    <div className="absolute right-0 mt-2 w-[20rem] bg-white border rounded-lg shadow-lg p-4 z-50">
      <h3 className="text-lg font-semibold mb-2">Sản phẩm trong giỏ hàng</h3>
      {cartItems.length > 0 ? (
        <ul>
          {cartItems.map((item, index) => (
            <li key={index} className="flex justify-between items-center mb-2">
              <div>
                <p>{item.name}</p>
                <p className="text-gray-500">{item.price}đ</p>
              </div>
              <img src={`image/${item.images[0]}`} alt={item.name} className="w-12 h-12 rounded" />
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-gray-500">Giỏ hàng của bạn trống.</p>
      )}
    </div>
  );
}
