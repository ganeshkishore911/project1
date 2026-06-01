import React, { useEffect, useState } from "react";
import api from "../../api";
import ProductCard from "../../Components/ProductCard/ProductCard";
import "./Order.scss";

const Order = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    getOrders();
  }, []);

  const getOrders = async () => {
    try {
      const res = await api.get("/api/orders/");
      setOrders(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="orders">
      <h1>My Orders</h1>

      {!orders.length ? (
        <h3>No orders found</h3>
      ) : (
        orders.map((order) => {
          const totalPrice =
            order.items?.reduce(
              (a, i) =>
                a +
                i.product_price *
                  i.quantity,
              0
            ) || 0;

          return (
            <div
              key={order.id}
              className="order-card"
            >
              <h3>
                Order #{order.id}
              </h3>

              <div className="product-grid">
                {order.items?.map(
                  (item) => (
                    <div key={item.id}>
                      <ProductCard
                        showCartBtn={false}
                        product={{
                          id: item.product,
                          name:
                            item.product_name,
                          price:
                            item.product_price,
                          images:
                            item.product_image
                              ? [
                                  {
                                    images:
                                      item.product_image,
                                  },
                                ]
                              : [],
                        }}
                      />

                      <p>
                        Quantity:
                        {item.quantity}
                      </p>
                    </div>
                  )
                )}
              </div>

              <h3>
                Total: ₹
                {totalPrice}
              </h3>
            </div>
          );
        })
      )}
    </div>
  );
};

export default Order;