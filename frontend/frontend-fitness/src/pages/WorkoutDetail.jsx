//workout details page
import "../css/workoutdetail.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

export default function WorkoutDetail() {
  const params = useParams();
  const Name = params.name;
  const [workout, setWorkout] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);

      try {
        const res = await fetch("/api/workouts/" + encodeURIComponent(Name), {
          method: "GET",
          credentials: "include"
        });

        if (res.status === 401) {
          navigate("/login", { replace: true });
          return;
        }

        if (res.status === 404) {
          setError("Workout not found");
          setWorkout(null);
          return;
        }

        if (!res.ok) {
          throw new Error("Failed to load workout");
        }

        const data = await res.json();
        setWorkout(data);

      } catch (e) {
        if (e.message) {
          setError(e.message);
        } else {
          setError("Failed to load workout");
        }
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [Name, navigate]);

  if (loading) {
    return <p>Loading workout…</p>; 
  }

  if (err) {
    return <p style={{ color: "red" }}>{err}</p>;
  }

  // displays the specific chosen workout details
  const title = workout.Name || workout.name;
  const description = workout.Description || workout.description;
  const sections = workout.Sections || workout.sections || [];

  return (
    <>
      <header className="nav-bar"><NavBar /></header>
      <div className="back-button-container">
        <button className="back-button" onClick={() => navigate(-1)}>Back to Workouts List</button>
      </div>
      <div className="workout-container">
        <div className="workout-detail">
          <h2 className="workout-title">{title}</h2>
          <p className="workout-description">{description}</p>
          {sections.length === 0 && <p>No sections found!</p>}
          {/* Sections */}
          {sections.length > 0 && (
            <div className="sections-container">
              {sections.map((section) => {
                const sectionName = section.SectionName || "Untitled Section";
                const routines = section.Routines || [];
                return (
                  <div key={section.ID} className="section-card">
                    <h3 className="section-title">{sectionName}</h3>
                    {/* No routines */}
                    {routines.length === 0 && <p>No routines found!</p>}
                    {/* Routines */}
                    {routines.length > 0 && (<ul className="routine-list">{routines.map((routine) => (
                          <li key={routine.ID} className="routine-item">
                            <div className="routine-row">
                              <span className="routine-name">{routine.Name}</span>
                              {routine.RepsDuration && (<span className="routine-duration">{" - "}{routine.RepsDuration}</span>)}
                            </div>
                            {routine.RoutineDescription && (<p className="routine-desc">{routine.RoutineDescription}</p>)}
                          </li>
                        ))}
                      </ul>
                    )}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>
    </>
  );
}
