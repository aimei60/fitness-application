//login / sign up page
import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function Login() {

  const [toggle, setToggle] = useState("Sign up"); //to switch between sign up and login states
  const [email, setEmail] = useState(""); //user input
  const [password, setPassword] = useState(""); //user input
  const [error, setError] = useState(null); //status of the request
  const [loading, setLoading] = useState(false); //error message if something is amiss
  const [captchaToken, setCaptchaToken] = useState(""); //captchs

  const navigate = useNavigate();

  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

  let isSignup = false;
  if (toggle === "Sign up") {
    isSignup = true;
  }

  useEffect(() => {
    if (!window.turnstile) return;

    //stops 2 cloudflare turnstiles showing up
    const container = document.getElementById("turnstile-widget");
    if (!container) return;
    container.innerHTML = "";

    window.turnstile.render("#turnstile-widget", {
      sitekey: import.meta.env.VITE_TURNSTILE_SITE_KEY,
      callback: function (token) {
        setCaptchaToken(token);
      },
    });
  }, []);

  async function handleLogin() {
    setError(null);
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE_URL}/api/login`, {
        method: "POST",
        credentials: "include",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({Email: email, Password: password})
      });

    
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Login failed");
    }     
 
      navigate("/homepage", { replace: true });   
    } catch (e) {
      console.error(e)
      setError("Login failed");
    } finally {
      setLoading(false);
    }
  }

  async function handleSignup() {
    setError(null); 
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/signup`, {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({Email: email, Password: password, CaptchaToken: captchaToken
        })
    })

    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Login failed");
    }  

      navigate("/homepage", { replace: true }); 
    } catch (e) {
      console.error("Signup error:", e)
      setError(e.message || "Signup failed")
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

  //signup/login logic
  let forgotPasswordSection = null;
  if (toggle !== "Sign up") {
    forgotPasswordSection = <div className="forgot-password"></div>;
  }

  let errorSection = null;
  if (error) {
    errorSection = <p className="errorMsg">{error}</p>;
  }

  let buttonText = "Log in";
  if (toggle === "Sign up") {
    buttonText = "Create account";
  }

  if (loading) {
    buttonText = "Logging in...";
    if (toggle === "Sign up") {
      buttonText = "Creating…";
    }
  }

  let signUpButtonClass = "submit";
  if (toggle === "Login") {
    signUpButtonClass = "submit gray";
  }

  let loginButtonClass = "submit";
  if (toggle === "Sign up") {
    loginButtonClass = "submit gray";
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
          {/*forgotPasswordSection*/}
          {errorSection}
          <button type="submit" className="submit2" disabled={loading}>{buttonText}</button>
           <div className="turnstile" id="turnstile-widget"></div>
          <div className="submit-container">
            <button type="button" className={signUpButtonClass}onClick={() => {setToggle("Sign up");}}>Sign Up Section</button>
            <button type="button" className={loginButtonClass}onClick={() => {setToggle("Login");}}>Login Section</button>
          </div>
        </form>
        </div>
      </div>
    </div>
    </>
  );
}

export default Login;
