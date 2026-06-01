import { Link } from "react-router-dom";
import "./Footer.scss";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-top">

        <div>
          <h3>Shop</h3>

          <Link to="/men">Men</Link>
          <Link to="/ladies">Women</Link>
          <Link to="/kids">Kids</Link>
        </div>

        <div>
          <h3>Quick Links</h3>

          <Link to="/">Home</Link>
          <Link to="/wishlist">
            Wishlist
          </Link>
          <Link to="/cart">
            Cart
          </Link>
          <Link to="/profile">
            Profile
          </Link>
        </div>

        <div>
          <h3>Contact</h3>

          <p>
            Email:
            ganeshkishore51@gmail.com.com
          </p>

          <p>
            Phone:
            +91 9043508432
          </p>
        </div>

      </div>

      <div className="footer-bottom">
        <p>
          © 2026 Fluxo.
          All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;