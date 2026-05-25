import { Link } from "react-router-dom";
import "./ProductCard.scss";

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <Link to={`/product/${product.id}/`}>
        <div className="product-image">
          <img
            src={`http://localhost:8000${product.images?.[0]?.images}`}
            alt={product.name}
          />

          {product.is_new && (
            <span className="badge">
              NEW
            </span>
          )}

        </div>

        <div className="product-info">
          <h3>{product.name}</h3>

          <p className="price">
            ₹{product.price}
          </p>

          <button className="cart-btn">
            Add to Cart
          </button>
        </div>
      </Link>
    </div>
  );
}

export default ProductCard;