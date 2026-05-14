import React, { useEffect, useState } from 'react'
import api from './api'

const Home = () => {
    const [products, setProducts] = useState([])
    useEffect(() => {
        fetchProducts()
    }, [])
    const fetchProducts = async () => {
        try {
            const res = await api.get(
                "/api/products/",
                {
                    withCredentials: true
                }
            )
            console.log(res.data)
            setProducts(res.data)
        } catch (err) {
            console.log(err)
            alert("Unauthorized")
        }
    }
    return (
        <div>
            <h2>Products</h2>
            {
                products.length === 0 ? (<p>No Products Found</p>
                ) : ( products.map((item) => (
                        <div key={item.id}>

                            <h3>{item.name}</h3>
                            <p>{item.image}</p><p>{item.price}</p>

                        </div>
                    ))
                )
            }

        </div>
    )
}

export default Home