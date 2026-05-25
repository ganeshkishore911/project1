import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../../api";
import ProductCard from "../../Components/ProductCard/ProductCard"
import "./ProductList.scss";

function ProductList() {
  const { id } = useParams();

  const [productlist, setProductlist] =
    useState([]);

  useEffect(() => {
    getProductlist();
  }, [id]);

  const getProductlist = async () => {
    try {
      const res = await api.get(
        `/api/productlist/${id}/`
      );

      setProductlist(res.data);
      console.log(res.data)
    } catch (err) {
      console.log("error", err);
    }
  };

  return (
    <div>
      <h1>Product List</h1>
<div className="product-grid" style={{ width: "100%" }}>
      
  {productlist.map((prod) => (
    <ProductCard key={prod.id} product={prod}/>
  ))}
</div>
    </div>
  );
}

export default ProductList;