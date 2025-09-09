import "../css/homepage.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom"

//exporting api
const BASE = import.meta.env.VITE_API_URL || "";

function Homepage() {
  const [workouts, setWorkouts] = useState([]); 
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(null);
  const navigate = useNavigate(); 

  //check the user is logged in or send user to login page
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login", { replace: true });
      return;
    }

    //loads, fetches and displays workouts using saved token. 
    //if token is invalid, send to login page
    //else display error message.
    async function load() {
      setLoading(true);
      setErr(null);
      try {
        if (!BASE) throw new Error("API base URL is not set");

        const res = await fetch(`${BASE}/workouts`, {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        if (res.status === 401) {
          localStorage.removeItem("access_token");
          navigate("/login", { replace: true });
          return;
        }

        if (!res.ok) throw new Error(`Error ${res.status}`);
        const data = await res.json();
        setWorkouts(Array.isArray(data) ? data : []);
      } catch (e) {
        setErr(e.message || "Failed to load workouts");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [navigate]);

  //directs user to the workout page with the workout details they picked
  const handleSelect = (name) => {
    navigate(`/workouts/${encodeURIComponent(name)}`);
  };
  
  //displays all 30 workout names
  return (
    <div>
      <NavBar />
      <div className="homepage-container">
        <h2 className="workout-title">Choose your workout!</h2>
        <div className="workout-list-container">
          {workouts.length === 0 ? (
            <p>No workouts found!</p>
          ) : (
            <ul>
                {workouts.map((w) => {
                    const name = w.Name || w.name;
                    const description = w.Description || w.description || "";

                    return (
                    <li key={w.id || name} // chooses id or name 
                        className="workout-item"
                        onClick={() => handleSelect(name)}
                        role="button"
                        tabIndex={0}>
                        <span className="workout-name">{name}</span>
                        <span className="description-name">{description}</span>
                    </li>
                    );
                })}
                </ul>
          )}
        </div>
      </div>
    </div>
  );
}

export default Homepage;
