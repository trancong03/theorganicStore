import { createContext, useState, useContext, useEffect } from 'react';

const CartContext = createContext();

export const CartProvider = ({ children,personID }) => {
    const [cartItems, setCartItems] = useState([]);
    useEffect(() => {
        const fetchCartItems = async () => {
            if (!personID) return; 
            try {
                const response = await fetch(`http://localhost:8000/api/get_product_on_cart/`, {
                    method: 'POST', 
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ person_id: personID }), 
                });
                const result = await response.json();
                setCartItems(...cartItems,result);
            } catch (error) {
                console.error('Error fetching cart items:', error);
            }
        };
        fetchCartItems();
    }, [personID]);  

    const addToCart = (item) => {
        setCartItems([...cartItems, item]);
    };

    const removeFromCart = (itemId) => {
        setCartItems(cartItems.filter(item => item.id !== itemId));
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
