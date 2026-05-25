import React, {
  useEffect,
  useState,
} from "react";

import api from "../src/api";
import { useParams } from "react-router-dom";

const Main = () => {
  const [banners, setBanners] =
    useState([]);

  const { category } =
    useParams();


  const currentCategory =
    category || "men";

  useEffect(() => {
    getBanners();
  }, [currentCategory]);

  const getBanners = async () => {
    try {
      const res = await api.get(
        `/api/homebanner/${currentCategory}/`
      );

      setBanners(res.data);

      console.log(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="banner-grid">
      {banners.map((banner) => (
        <div
          key={banner.id}
          className="banner-card"
        >
          <img
            src={`http://localhost:8000${banner.image}`}
            alt={banner.title}
          />

          <h2>{banner.title}</h2>

          <p>
            ₹{banner.price}
          </p>
        </div>
      ))}
    </div>
  );
};

export default Main;