import "../css/loginsignup.css";
import emailIcon from '../assets/email.png'
import passwordIcon from '../assets/password.png'

function Login() {

  return (
    <div className="container">
      <div className="header">
        <div className="text">Sign up</div>
      </div>
      <div className="inputs">
        <div className="input">
          <img src={emailIcon} alt=""></img>
          <input type="email"></input>
        </div>
        <div className="input">
          <img src={passwordIcon} alt=""></img>
          <input type="password"></input>
        </div>
        <div className="forgotten-password">Forgotten Password</div>
        <div className="submit-container">
          <div className="submit">Sign Up</div>
          <div className="submit">Login</div>
        </div>
      </div>
    </div>
  )
}

export default Login