//centralizes and automates authentication, CSRF protection, and cookie-based sessions and automatically makes sure all axios requests are authenticated
import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL ?? "/api";

//Axios instance that sends/receives cookies
export const api = axios.create({
  baseURL: API_BASE,
  withCredentials: true,
  headers: { "Content-Type": "application/json" },
});

//read a cookie for CSRF
export function getCookie(name) {
  const m = document.cookie.match(new RegExp("(^| )" + name + "=([^;]+)"));
  return m ? decodeURIComponent(m[2]) : null;
}

//handles safe GET requests
export function apiGet(path, config = {}) {
  return api.get(path, config);
}

//attach CSRF token for write/actionable requests
function withCsrf(config = {}) {
  const csrf = getCookie("csrf_token") || "";
  return { ...config, headers: { ...(config.headers || {}), "X-CSRF-Token": csrf } };
}
export function apiPost(path, data, config = {}) {
  return api.post(path, data, withCsrf(config));
}
export function apiPut(path, data, config = {}) {
  return api.put(path, data, withCsrf(config));
}
export function apiPatch(path, data, config = {}) {
  return api.patch(path, data, withCsrf(config));
}
export function apiDelete(path, config = {}) {
  return api.delete(path, withCsrf(config));
}

// Login: server sets cookies; no localStorage tokens anymore
export async function login(email, password) {
  await api.post("/login", { Email: email, Password: password });
}

