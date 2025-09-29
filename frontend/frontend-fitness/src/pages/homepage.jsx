//homepage
import "../css/homepage.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiGet } from "../api"; // uses baseURL=/api and withCredentials:true

function Homepage() {
  const [workouts, setWorkouts] = useState([]); 
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(null);
  const navigate = useNavigate(); 

  //check the user is logged in or send user to login page
  useEffect(() => {
    let isMounted = true;

    async function load() {
      setLoading(true);
      setErr(null);
      try {
        const res = await apiGet("/workouts"); // cookie-based session
        const data = res.data;
        if (isMounted) setWorkouts(Array.isArray(data) ? data : []);
      } catch (e) {
        const status = e?.response?.status;
        if (status === 401) {
          navigate("/login", { replace: true });
        } else {
          setErr(e?.response?.data?.detail || e.message || "Failed to load workouts");
        }
      } finally {
        if (isMounted) setLoading(false);
      }
    }

    load();
    return () => {
      isMounted = false;
    };
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
          {/* Show loading spinner or message while data is being fetched */}
          {loading && <p>Loading workouts...</p>}

          {/* Show error if something goes wrong */}
          {!loading && err && <p style={{ color: "crimson" }}>{err}</p>}

          {/* Show empty state only when loading has finished and there is no error */}
          {!loading && !err && workouts.length === 0 && (
            <p>No workouts found!</p>
          )}

          {/* Display workouts when successfully fetched */}
          {!loading && !err && workouts.length > 0 && (
            <ul>
              {workouts.map((w) => {
                const name = w.Name || w.name;
                const description = w.Description || w.description || "";

                return (
                  <li
                    key={w.id || name} // chooses id or name 
                    className="workout-item"
                    onClick={() => handleSelect(name)}
                    role="button"
                    tabIndex={0}
                  >
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
