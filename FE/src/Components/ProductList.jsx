import React, { useState } from 'react';
import CartItemShopping from './CartItemShopping'; // Đường dẫn component CartItem

export default function ProductList() {
    return (
        <div>
            {products.length === 0 ? (
                <p>Không có sản phẩm nào.</p> // Thông báo khi không có sản phẩm
            ) : (
                products.map((product, index) => (
                    <CartItemShopping
                        key={index}
                        name={product.name}
                        price={product.price}
                        images={product.images}
                        onAddToCart={handleAddToCart} // Truyền hàm handleAddToCart
                    />
                ))
            )}
        </div>
    );
}
