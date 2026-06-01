import { Link } from "react-router-dom";
import "./ProductCard.scss";

function ProductCard({product,showCartBtn = true,children,}) {
  return (
    <div className="product-card">
      <Link
        to={`/product/${product.id}/`}
      >
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
        </div>
      </Link>

      <div className="card-actions">
        {showCartBtn && (
          <button className="cart-btn">
            Add to Cart
          </button>
        )}

        {children}
      </div>
    </div>
  );
}

export default ProductCard;