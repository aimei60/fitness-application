//handles authentication tokens: stores them, loads them when the application starts and makes sure all axios requests are authenticated automatically
import axios from "axios";

//creates axios to make http requests. all requests go to backend --> vite_api_base or http://localhost:8000
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE || "http://localhost:8000",
  withCredentials: false
});

// checks if token was saved in local storage from a previous login and if found axios attaches it to every request and this makes sure the suer stays logged in if the page refreshes
let token = localStorage.getItem("access_token");
if (token) api.defaults.headers.common.Authorization = `Bearer ${token}`;

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
