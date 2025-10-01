//login / sign up page

import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'
import { useState } from "react";
import { login, apiPost, apiGet } from "../api";
import { useNavigate } from "react-router-dom";

function Login() {
  //maintenance site
  const maintenance = import.meta.env.VITE_MAINTENANCE_MODE === "true";
  const msg = import.meta.env.VITE_MAINTENANCE_MSG || "Under maintenance";

  if (maintenance) {
    return (
      <div style={{margin: "3rem auto", maxWidth: "28rem", borderRadius: "1rem", border: "1px solid #ccc", padding: "1.5rem", textAlign: "center"}}>
      <h2 style={{fontSize: "1.25rem", fontWeight: 600, marginBottom: "0.5rem"}}>Under Maintenance</h2>
      <p style={{opacity: 0.8}}>{msg}</p>
      </div>
        );
  }

  const [toggle, setToggle] = useState("Sign up"); //to switch between sign up and login states
  const [email, setEmail] = useState(""); //user input
  const [password, setPassword] = useState(""); //user input
  const [error, setError] = useState(null); //status of the request
  const [loading, setLoading] = useState(false); //error message if something is amiss
  
  const navigate = useNavigate();
  const isSignup = toggle === "Sign up";
  async function handleLogin() {
    setError(null);
    setLoading(true);
    try {
      await login(email, password); // server sets cookies; no local token       
      await apiGet("/me")    
      navigate("/homepage", { replace: true });   
    } catch (e) {
      console.error("Signup error:", e)
      //optional chaining for cleaner code
      const msg = e?.response?.data?.detail || "Login failed";
      setError(msg); // 
    } finally {
      setLoading(false);
    }
  }

  async function handleSignup() {
    setError(null); setLoading(true);
    try {
      await apiPost("/signup", { Email: email, Password: password });   
      navigate("/homepage", { replace: true }); 
    } catch (e) {
      console.error("Signup error:", e)
      const msg = e?.response?.data?.detail || "Signup failed";
      setError(msg);
    } finally {
      setLoading(false);
    }
  }
  
  //confirms whether user to should sign up or login
  async function onSubmit(e) {
    e.preventDefault();
    if (isSignup) await handleSignup();
    else await handleLogin();
  }

  //code for the login/sign up page
  return (
    <>
    <div className="login-page">
      <div className="login-wrapper">      
        <div className="title-container">
          <div className="title">FitRequest</div>
          </div>
      <div className="container">
        <div className="header">
          <div className="text">{toggle}</div>
        </div>
        <form className="inputs" onSubmit={onSubmit}>
          <div className="input">
            <img src={emailIcon} alt="message icon representing email"/>
            <input type="email" placeholder="Email Address" value={email} onChange={e => {setEmail(e.target.value);
              setError(null)}}required/>
          </div>
          <div className="input"> 
            <img src={passwordIcon} alt="lock to represent password"/>
            <input type="password" placeholder="Password" value={password} onChange={e => {setPassword(e.target.value);
              setError(null)}}required/>
          </div>
          {toggle === "Sign up"?(<div></div>):(<div className="forgot-password"></div>)}
          {error && <p className="errorMsg">{error}</p>}
          <button 
          type="submit" className="submit2" disabled={loading}>{loading ? (toggle === "Sign up" ? "Creating…" : "Logging in…") : (toggle === "Sign up" ? "Create account" : "Log in")}
          </button>
          <div className="submit-container">
            <button type="button" className={toggle === "Login"?"submit gray":"submit"}onClick={() => { setToggle("Sign up");}}>Sign Up Section</button>
            <button type="button" className={toggle === "Sign up"?"submit gray":"submit"}onClick={() => { setToggle("Login");}}>Login Section</button>
          </div>
        </form>
        </div>
      </div>
    </div>
    </>
  );
}

export default Login;
