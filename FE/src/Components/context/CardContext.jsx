import { createContext, useState, useContext, useEffect } from 'react';

const CartContext = createContext();

export const CartProvider = ({ children, personID }) => {
    const [cartItems, setCartItems] = useState([]);

    useEffect(() => {
        const fetchCartItems = async () => {
            if (!personID) return; // Kiểm tra nếu personID không tồn tại thì không fetch
            try {
                const response = await fetch('http://localhost:8000/api/get_product_on_cart/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ person_id: personID }), // Gửi personID để lấy giỏ hàng của người dùng
                });
                const result = await response.json();
                if (result.product) {
                    setCartItems(result.product);
                } else {
                    console.error('Invalid response format:', result);
                }
            } catch (error) {
                console.error('Error fetching cart items:', error);
            }
        };

        fetchCartItems();
    }, [personID]); 

    const addToCart = async (item) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/add_product_to_Cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_id: item.ProductID,
                    person_id: personID,
                }),
            });
            const result = await response.json();
            if (result.success) {
                setCartItems(prevItems => [...prevItems, item]); // Thêm sản phẩm vào giỏ
                console.log('Product added to cart successfully');
            } else {
                console.log('Failed to add product to cart');
            }
        } catch (error) {
            console.error('Error adding product to cart:', error);
        }
    };
    const removeFromCart = async (itemId) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/remove_product_from_Cart/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    product_id: itemId,
                    person_id: personID,
                }),
            });
            const result = await response.json();
            if (result.success) {
                setCartItems(cartItems.filter(item => item.ProductID !== itemId)); 
                console.log('Product remove from cart successfully');
            } else {
                console.log('Failed to Product remove from cart');
            }
        } catch (error) {
            console.error('Error Product remove from cart:', error);
        }
    };

    return (
        <CartContext.Provider value={{ cartItems, addToCart, removeFromCart }}>
            {children}
        </CartContext.Provider>
    );
};

export const useCart = () => {
    return useContext(CartContext);
};
