import React, { useEffect, useState } from "react";
import api from "../../api";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

const OrderItemsChart = () => {

  const [data, setData] = useState([]);

  useEffect(() => {

    api.get("api/order-stats/")
      .then((res) => {
        setData(res.data);
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

  }, []);

  return (
    <div style={{ width: "100%", height: 400 }}>

      <h1>Your Orders Chart</h1>

      <ResponsiveContainer width="100%" height={400}>

        <BarChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />

          <YAxis />
          <Tooltip />
          <Bar dataKey="quantity" />
        </BarChart>

      </ResponsiveContainer>

    </div>
  );
};

export default OrderItemsChart;