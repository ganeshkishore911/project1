import React, { useEffect, useState } from "react";
import api from "../../api";
import Order from "../Order/Order";
import { useNavigate } from "react-router-dom";
import OrderItemsChart from "../../Components/Charts/OrderItems";

const Profile = () => {
  const [user, setUser] = useState(null);
   const navigate=useNavigate()
  useEffect(() => {
    getProfile();
  }, []);

  const getProfile = async () => {
    try {
      const res = await api.get("/api/profile/");
      setUser(res.data);
    } catch (err) {
      console.log(err);
    }
  };
  const handleLogout = async () => {
    try {
      await api.post("/api/logout/");

      navigate("/login"); 
    } catch (err) {
      console.log(err);
    }
  };

  if (!user) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>My Profile</h1>

      <div
        style={{
          border: "1px solid #ddd",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        <p>
          <strong>Username:</strong> {user.username}
        </p>

        <p>
          <strong>Email:</strong> {user.email}
        </p>
        <button onClick={handleLogout}>
          Logout
        </button>
      </div>
      <OrderItemsChart/>
<Order />
    </div>
  );
};

export default Profile;