import React, { useState } from "react"
import api from "../../api"
import "./Login.scss"
import { useNavigate ,Link} from "react-router-dom"

const Login = () => {
    const [form, setForm] = useState({
        username: "",
        password: ""
    })
    const navigate=useNavigate()

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        })
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const res = await api.post("/api/login/",form,
                {
                    withCredentials: true
                })
            console.log(res.data)
            alert("Login Successful")
            localStorage.setItem("isLoggedIn", "true")
            setForm({username: "",password: ""
                })
                navigate("/")
        } catch (err) {
            console.log(err)
            alert("Invalid Credentials")
        }
    }

    return (

        <div className="login-container">
            <div className="login-card">
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
            <p>Create new account <Link to="/signup">Signup</Link></p>
            </div>
        </div>
    )
}

export default Login