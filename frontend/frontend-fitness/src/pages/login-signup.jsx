import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'
import { useState } from "react";
import { api, setToken } from "../api";

function Login() {

  const [toggle, setToggle] = useState("Sign up"); //to switch between sign up and login states
  const [email, setEmail] = useState(""); //user input
  const [password, setPassword] = useState(""); //user input
  const [error, setError] = useState(null); //status of the request
  const [loading, setLoading] = useState(false); //error message if something is amiss
  
  const isSignup = toggle === "Sign up";
  //sends login request to backend. if successful saves the jwt token with setToken and sends the user to the homepage else if failed shows error
  async function handleLogin() {
    setError(null);
    setLoading(true);
    try {
      const { data } = await api.post("/login", { Email: email, Password: password });
      setToken(data.access_token);           
      window.location.href = "/homepage";    
    } catch (e) {
      //optional chaining for cleaner code
      const msg = e?.response?.data?.detail || "Login failed";
      setError(msg); // 
    } finally {
      setLoading(false);
    }
  }

  //sign up function
  async function handleSignup() {
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
          {toggle === "Sign up"?(<div></div>):(<div className="forgot-password">Forgot Password</div>)}
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
    </>
  );
}

export default Login;
