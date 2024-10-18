import React, { useEffect, useState } from "react";
import Banner from "../Components/Banner";
import CartItem from "../Components/ui/CartItem";


export default function Home({ onAddToCart }) {
  const [listProduct, setlistProduct] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/product/')
      .then(response => response.json())
      .then(data => setlistProduct(data.product))
      .catch(error => console.error('Error fetching data:', error));
  }, []);
  const productsBanner = [...listProduct];
  return (
    <div className=" bg-[#f2f0f0]">
      <Banner products={productsBanner.sort(() => Math.random() - 0.5).slice(0, 10)} />
      <div className="grid grid-cols-5 m-[5%]">
        {
        listProduct.map((product) => {
          return (
            <CartItem
              key={product.ProductID}
              name={product.Name}  
              price={product.Price}  
              images={product.ImageID || []}  
              origin={product.Origin}  
              expirationDate={product.ExpirationDate}  
              unit={product.Unit}  
              onAddToCart={() => onAddToCart(product)}  
            />
          );
        })}
      </div>

    </div>
  );
}
