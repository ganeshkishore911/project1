import React, {
  useEffect,
  useState,
} from "react";

import { useParams } from "react-router-dom";
import { FaHeart, FaRegHeart } from "react-icons/fa";
import api from "../../api";
import "./Product.scss";

export const Product = () => {
  const { id } = useParams();

  const [product, setProduct] =useState(null);

  const [wishlistItemId, setWishlistItemId] =useState(null);
  const [added,setAdded]=useState(false)

  useEffect(() => {
    getProduct();
    checkWishlist();
  }, [id]);

  const getProduct = async () => {
    try {
      const res = await api.get(
        `/api/product/${id}/`
      );

      setProduct(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  const checkWishlist = async () => {
    try {
      const res = await api.get("/api/wishlist/");

      const likedProduct =
        res.data.find(
          (item) =>
            item.product === Number(id)
        );

      if (likedProduct) {
        setWishlistItemId(
          likedProduct.id
        );
      }
    } catch (err) {
      console.log(err);
      
    }
  };

const toggleWishlist = async () => {
  try {
    if (wishlistItemId) {
      await api.delete(`/api/wishlist/${wishlistItemId}/`);

      setWishlistItemId(null);
    } else {
      const res = await api.post("/api/wishlistcreate/",
        {product: Number(id),}
      );

      setWishlistItemId(res.data.id);
    }
  } catch (err) {
    console.log("wishlist error",err.response?.data);
    alert("login first")
  }
};


const addToCart = async () => {
  try {
    const res = await api.post("/api/cartcreate/",
      {
        product: Number(id),
        quantity: 1,
      }
    );
    setAdded(true)
    console.log("added to cart", res.data);
    console.log()
  } catch (err) {
    console.log("cart error",err.response?.data)
    alert("loggin first")
  }
};
  if (!product) {
    return <h2>Loading...</h2>;
  }

  return (
    <div className="product-page">
      {/* Left Side Image */}
      <div className="product-left">
  {product.images?.map((img) => (
    <img
      key={img.id}
      src={`http://localhost:8000${img.images}`}
      alt={product.name}
      className="product-image"
    />
  ))}
</div>

      {/* Right Side Details */}
      <div className="product-right">
        <div className="title-row">
          <h1>{product.name}</h1>

          <button
            className="wishlist-btn"
            onClick={toggleWishlist}
          >
            {wishlistItemId ? (
              <FaHeart />
            ) : (
              <FaRegHeart />
            )}
          </button>
        </div>

        <p className="description">
          {product.description}
        </p>

        <h2 className="price">
          ₹{product.price}
        </h2>

        <button
      className="cart-btn"
      onClick={addToCart}
    >
      {added ? "Added" : "Add to Cart"}
    </button>
      </div>
    </div>
  );
};