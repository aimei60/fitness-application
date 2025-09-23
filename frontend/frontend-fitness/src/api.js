//handles authentication tokens: stores them, loads them when the application starts and makes sure all axios requests are authenticated automatically
import axios from "axios";

// create axios instance with correct base URL
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  withCredentials: false,
});

// load saved token from localStorage and attach to axios if found
let token = localStorage.getItem("access_token");
if (token) {
  api.defaults.headers.common.Authorization = `Bearer ${token}`;
}

// helper function to set or clear token
export function setToken(t) {
  token = t;
  if (t) {
    localStorage.setItem("access_token", t);
    api.defaults.headers.common.Authorization = `Bearer ${t}`;
  } else {
    localStorage.removeItem("access_token");
    delete api.defaults.headers.common.Authorization;
  }
}

