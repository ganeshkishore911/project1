import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../../api";
import { checkUserLoggedIn } from "../../api";
import "./Navbar.scss";
import { FaCartPlus, FaHeart, FaUser } from "react-icons/fa";

const Navbar = () => {
    const [categories, setCategories] = useState([]);
    const [subCategories, setSubCategories] = useState([]);
    const [hoveredCategory, setHoveredCategory] =useState(null);

    const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    checkLogin();
  }, []);

  const checkLogin = async () => {
    const loggedIn = await checkUserLoggedIn();
    setIsLoggedIn(loggedIn);
  };
       
    useEffect(() => {
        getCategories(); 
    }, []);

    const getCategories = async () => {
        try {
            const res = await api.get("/api/category/");
            setCategories(res.data);
        } catch (err) {
            console.log(err);
        }
    };

    const getSubCategories = async (id) => {
        try {
            const res = await api.get(`/api/category/${id}/`);

            setSubCategories(res.data);

        } catch (err) {
            console.log(err);
        }
    };

    return (
        <nav className="navbar">


            {/* Categories */}
            <ul className="nav-links">
  {categories.map((cat) => (
    <li
      key={cat.id}
      onMouseEnter={() => {
        setHoveredCategory(cat.id);
        getSubCategories(cat.id);
      }}
      onMouseLeave={() =>
        setHoveredCategory(null)
      }
    >
      <Link
        to={`/${cat.name.toLowerCase()}`}
      >
        {cat.name}
      </Link>

      {hoveredCategory === cat.id && (
        <div className="mega-menu">
          {subCategories.map((sub) => (
            <Link
              key={sub.id}
              to={`/productlist/${sub.id}`}
            >
              {sub.name}
            </Link>
          ))}
        </div>
      )}
    </li>
  ))}
</ul>

            {/* Logo */}
            <Link to="/">
                <h2>Fluxo</h2>
            </Link>

            {/* Right */}
            <div>
                <Link to={"/wishlist"}><FaHeart/></Link>
                <Link to={"/cart"}><FaCartPlus/></Link>
                {isLoggedIn ? (
        <Link to="/profile"><FaUser></FaUser></Link>
      ) : (
        <>
          <Link to="/login"><button>Login</button></Link>
          <Link to="/signup"><button>Signup</button></Link>
        </>
      )}
            
            </div>
        </nav>
    );
};

export default Navbar;