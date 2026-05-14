import React, { useState } from "react"
import api from "../api"
import '../styles/signup.scss'

const Signup = () => {

  const [form, setForm] = useState({
    username: "",
    password: "",
    email: ""
  })
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    })
  }
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await api.post(
        "/api/signup/",form,
        {
          withCredentials: true  // browser allows the cookies to receive and send token automatically
        }
      )
      console.log(res.data)
      alert("Signup Successful")
    
      setForm({})
    } catch (err) {
      console.log(err)
    }
  }

  return (

    <div>
      <h2>Signup</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text" name="username"placeholder="Username" onChange={handleChange}/>

        <input type="email" name="email" placeholder="Email" onChange={handleChange}/>
        <input type="password"name="password" placeholder="Password" onChange={handleChange} />
        <button type="submit">Signup</button>
      </form>

    </div>
  )
}

export default Signup