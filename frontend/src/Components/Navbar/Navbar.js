import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../../api";
import "./Navbar.scss";

const Navbar = () => {
    const [categories, setCategories] = useState([]);
    const [subCategories, setSubCategories] = useState([]);
    const [hoveredCategory, setHoveredCategory] =
        useState(null);

    const isLoggedIn =
        localStorage.getItem("isLoggedIn");

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
                {isLoggedIn ? (
                    <Link to="/profile">
                        👤
                    </Link>
                ) : (
                    <>
                        <Link to="/signup">
                            <button>Signup</button>
                        </Link>

                        <Link to="/login">
                            <button>Login</button>
                        </Link>
                    </>
                )}
            </div>
        </nav>
    );
};

export default Navbar;