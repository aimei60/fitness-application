import { useNavigate } from "react-router-dom";

function Homepage() {
    const navigate = useNavigate();
    // removes access token and navigates back to the login page. replace true means user cannot go back to homepage
    function logout() {
        localStorage.removeItem("access_token");
        navigate("/login", { replace: true });
    }
    
    return (
    
    <button onClick={logout}>Log out</button>
       

    )
}

export default Homepage