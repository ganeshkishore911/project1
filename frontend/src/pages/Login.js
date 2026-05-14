import React, { useState } from "react"
import api from "../api"

const Login = () => {
    const [form, setForm] = useState({
        username: "",
        password: ""
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
                "/api/login/",form,
                {
                    withCredentials: true
                })
            console.log(res.data)
            alert("Login Successful")
            setForm({})
        } catch (err) {
            console.log(err)
            alert("Invalid Credentials")
        }
    }

    return (

        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    value={form.username}
                    onChange={handleChange}/>
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={form.password}
                    onChange={handleChange}/>
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default Login