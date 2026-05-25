import React, {
  useEffect,
  useState,
} from "react";

import { useParams } from "react-router-dom";
import api from "../../api";
import "./Product.scss";

export const Product = () => {
  const { id } = useParams();

  const [product, setProduct] =
    useState(null);

  useEffect(() => {
    getProduct();
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

  if (!product) {
    return <h2>Loading...</h2>;
  }

  return (
    <div className="product-page">
      {/* Left Side Image */}
      <div className="product-left">
        <img
          src={`http://localhost:8000${product.images?.[0]?.images}`}
          alt={product.name}
        />
      </div>

      {/* Right Side Details */}
      <div className="product-right">
        <h1>{product.name}</h1>

        <p className="description">
          {product.description}
        </p>

        <h2 className="price">
          ₹{product.price}
        </h2>

        <button className="cart-btn">
          Add to Cart
        </button>
      </div>
    </div>
  );
};