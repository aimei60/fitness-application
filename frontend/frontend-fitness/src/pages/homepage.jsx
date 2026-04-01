//homepage
import "../css/homepage.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Homepage() {
  const [workouts, setWorkouts] = useState([]); 
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate(); 

  //check the user is logged in or send user to login page
  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);

      try {
        const res = await fetch("/api/workouts", {
          method: "GET",
          credentials: "include"
        });

        if (res.status === 401) {
          navigate("/login", { replace: true });
          return;
        }

        if (!res.ok) {
          throw new Error("Failed to load workouts");
        }

        const data = await res.json();
        setWorkouts(data);
          
      } catch (e) {
        if (e.message) {
          setError(e.message);
        } else {
          setError("Failed to load workouts");
        }
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
      <header className="nav-bar">
      <NavBar />
      </header>
      <div className="homepage-container">
        <h2 className="workout-title">Choose your workout!</h2>
        <div className="workout-list-container">
          {loading && <p>Loading workouts...</p>}
          {!loading && error && <p style={{ color: "crimson" }}>{err}</p>}
          {!loading && !error && workouts.length === 0 && (
            <p>No workouts found!</p>
          )}
          {!loading && !error && workouts.length > 0 && (
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
