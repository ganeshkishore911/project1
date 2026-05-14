import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000",  // ← localhost, NOT 127.0.0.1
    withCredentials: true,
})

export default api