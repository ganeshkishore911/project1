import React, { useEffect, useState } from "react";
import api from "../../api";
import ProductCard from "../../Components/ProductCard/ProductCard";

const Cart = () => {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    getCart();
  }, []);

  const getCart = async () => {
    try {
      const res = await api.get("/api/cart/");
      setCart(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  const removeItem = async (id) => {
    try {
      await api.delete(`/api/cart/${id}/`);
      setCart((prev) => prev.filter((item) => item.id !== id));
    } catch (err) {
      console.log(err);
    }
  };

  const updateQuantity = async (id, quantity) => {
    if (quantity < 1) return;

    try {
      await api.put(`/api/cart/${id}/`, { quantity });

      setCart((prev) =>
        prev.map((item) =>
          item.id === id ? { ...item, quantity } : item
        )
      );
    } catch (err) {
      console.log(err);
    }
  };

  const total = cart.reduce(
    (acc, item) => acc + item.product_price * item.quantity,
    0
  );
  const placeOrder = async () => {
  try {
    await api.post("/api/create-order/");

    alert("Order placed");
    
    getCart(); 
  } catch (err) {
    console.log(err);
    alert("need to add any products in Cart")
  }
};

  return (
    <div>
      <h1>Cart</h1>

      <div className="product-grid" style={{ width: "100%" }}>
        {cart.map((item) => (
          <div key={item.id}>
            <ProductCard
              showCartBtn={false}
              product={{
                id: item.product,
                name: item.product_name,
                price: item.product_price,
                images: item.product_image ? [{ images: item.product_image }] : [],
              }}
            />

            <div style={{ display: "flex", gap: "10px", alignItems: "center", marginTop: "10px" }}>
              <button onClick={() => updateQuantity(item.id, item.quantity - 1)}>-</button>

              <span>{item.quantity}</span>

              <button onClick={() => updateQuantity(item.id, item.quantity + 1)}>+</button>

              <button onClick={() => removeItem(item.id)}>Remove</button>
            </div>
          </div>
        ))}
      </div>

      <h2>Total: ₹{total}</h2>
      <button onClick={placeOrder}>Place Order</button>
    </div>
  );
};

export default Cart;