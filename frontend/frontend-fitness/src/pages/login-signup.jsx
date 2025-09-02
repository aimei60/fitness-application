import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'
import { useState } from "react";

function Login() {
//to switch between sign up and login states
  const [toggle, setToggle] = useState("Sign up");

  return (
    <div className="container">
      <div className="header">
        <div className="text">{toggle}</div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={emailIcon} alt=""></img>
          <input type="email" placeholder="Email Address"></input>
        </div>
        <div className="input">
          <img src={passwordIcon} alt=""></img>
          <input type="password" placeholder="Password"></input>
        </div>
        {toggle==="Sign up"?<div></div>:<div className="forgot-password">Forgot Password</div>}
        <div className="submit-container">
          <div className={toggle==="Login"?"submit gray":"submit"} onClick={()=> {setToggle("Sign up")}}>Sign Up</div>
          <div className={toggle=="Sign up"?"submit gray":"submit"} onClick={()=> {setToggle("Login")}}>Login</div>
        </div>
      </div>
    </div>
  )
}

export default Login