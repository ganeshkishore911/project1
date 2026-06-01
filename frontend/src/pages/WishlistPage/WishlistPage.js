import React, {
  useEffect,
  useState,
} from "react";

import axios from "axios";
import ProductCard from "../../Components/ProductCard/ProductCard";

export const WishlistPage =
  () => {
    const [wishlist, setWishlist] =
      useState([]);

    useEffect(() => {
      getWishlist();
    }, []);

    const getWishlist =
      async () => {
        try {
          const response =
            await axios.get(
              "http://localhost:8000/api/wishlist/",
              {
                withCredentials:true,
              }
            );

          setWishlist(
            response.data
          );
        } catch (error) {
          console.log(error);
        }
      };

    return (
      <div>
        <h1>Wishlist</h1>

        <div
          className="product-grid"
          style={{
            width: "100%",
          }}
        >
          {wishlist.length ===0 ? (
            <p>
              No wishlist items</p>
          ) : (
            wishlist.map((item) => (
                <ProductCard
                  key={item.id}
                  product={{
                    id: item.product,
                    name:item.product_name,
                    price:item.product_price,
                    images:item.product_image? [{
                            images:item.product_image,},]
                      : [],
                  }}
                />
              )
            )
          )}
        </div>
      </div>
    );
  };