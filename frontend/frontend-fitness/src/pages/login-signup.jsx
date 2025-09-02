import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'
import { useState } from "react";

function Login() {



  return (
    <div className="container">
      <div className="header">
        <div className="text">Sign up</div>
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
        <div className="forgot-password">Forgot Password</div>
        <div className="submit-container">
          <div className="submit">Sign Up</div>
          <div className="submit">Login</div>
        </div>
      </div>
    </div>
  )
}

export default Login