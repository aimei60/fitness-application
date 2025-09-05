import { Link } from "react-router-dom"
import "../css/navbar.css"
import { useNavigate } from "react-router-dom";

function NavBar() {

    const navigate = useNavigate();
    // removes access token and navigates back to the login page. replace true means user cannot go back to homepage
    function logout() {
        localStorage.removeItem("access_token");
        navigate("/login", { replace: true });
    }
    
    return <nav className="navbar">
        <div className="navbar_brand">
            <div className="logo">FitRequest</div>
        </div>
        <div className="navbar-right">
            <div className="navbar-links">
                <Link to="/profile" className="nav-link-profile">Profile</Link>
                <Link to="/homepage" className="nav-link-settings">Homepage</Link>
                <Link to="/settings" className="nav-link-settings">Settings</Link>
            </div>
            <button className="logout" onClick={logout}>Logout</button>
        </div>
    </nav>
}

export default NavBar;