//handles authentication tokens: stores them, loads them when the application starts and makes sure all axios requests are authenticated automatically
import axios from "axios";

//create axios instance with correct base URL
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://localhost:8000",
  withCredentials: false, //using Bearer tokens, not cookies
});

//load saved token from localStorage and attach to axios if found. axios attaches it to every request and this makes sure the user stays logged in if the page refreshes
let token = localStorage.getItem("access_token");
if (token) {
  api.defaults.headers.common.Authorization = `Bearer ${token}`;
}

//logging in/ out set token function. logging in: saves token to local storage and sets axios authorisation header. logging out: removes token from storage and stops sending it in requests
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

