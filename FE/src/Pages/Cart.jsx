import React, { useEffect, useState } from "react";
import CartItemDetail from "../Components/ui/CartItemDetail";

export default function Cart({ cartItems, onAddToCart }) {
    const [cart, setCart] = useState(cartItems);
    const [totalAmount, setTotalAmount] = useState(0);

    useEffect(() => {
        const updatedCartItems = cartItems.map(item => ({
            ...item,
            quantity: item.quantity || 1,
        }));
        setCart(updatedCartItems);

        const total = updatedCartItems.reduce((sum, item) => {
            const price = parseFloat(item.price);
            const quantity = item.quantity || 1;
            return sum + price * quantity;
        }, 0);
        setTotalAmount(total);
    }, [cartItems]);

    const handleQuantityChange = (itemId, change) => {
        setCart((prevCart) => {
            const updatedCart = prevCart.map((item) => {
                if (item.id === itemId) {
                    const newQuantity = (item.quantity || 1) + change;
                    return { ...item, quantity: Math.max(newQuantity, 1) };
                }
                return item;
            });

            const newTotal = updatedCart.reduce((sum, item) => {
                const price = parseFloat(item.price);
                return sum + price * (item.quantity || 1);
            }, 0);
            setTotalAmount(newTotal);

            return updatedCart;
        });
    };

    return (
        <div className="flex flex-col lg:flex-row p-6 lg:p-12 gap-6 bg-gray-100 min-h-screen mx-60">
            <div className="flex-1 bg-white shadow-md rounded-lg p-6 h-fit ">
                <h2 className="text-2xl font-bold mb-4 text-gray-700">Giỏ hàng</h2>
                <ul className="divide-y divide-gray-200">
                    {cart.map((item) => (
                        <CartItemDetail
                            key={item.id}
                            item={item}
                            onQuantityChange={handleQuantityChange}
                        />
                    ))}
                </ul>
            </div>
            <div className="w-full lg:w-1/3 max-w-sm bg-white shadow-md rounded-lg p-6 h-fit">
                <h3 className="text-xl font-semibold text-gray-700">Tổng tiền</h3>
                <p className="text-2xl font-bold text-gray-800 mt-2 mb-4">{totalAmount.toLocaleString()} VND</p>
                <button className="w-full bg-blue-500 hover:bg-blue-600 text-white py-3 px-4 rounded-lg transition duration-300 ease-in-out">
                    Thanh toán
                </button>
            </div>
        </div>
    );
}
