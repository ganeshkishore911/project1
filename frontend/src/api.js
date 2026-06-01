import axios from "axios"

const api = axios.create({
    baseURL: "http://localhost:8000",  
    withCredentials: true,
})

export default api

export const checkUserLoggedIn = async () => {
  try {
    await api.get("/api/profile/");
    return true;
  } catch (err) {
    return false;
  }
};