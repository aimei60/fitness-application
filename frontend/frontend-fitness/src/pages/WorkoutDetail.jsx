//workout details page

import "../css/workoutdetail.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

const BASE = import.meta.env.VITE_API_URL || "";

export default function WorkoutDetail() {
  const { name: Name } = useParams();
  const [workout, setWorkout] = useState(null);
  const [err, setErr] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login", { replace: true });
      return;
    }

    async function load() {
      setLoading(true);
      setErr(null);
      try {
        const res = await fetch(`${BASE}/workouts/${Name}`, {
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
        if (res.status === 404) {
          setErr("Workout not found");
          setWorkout(null);
          return;
        }
        if (!res.ok) throw new Error(`Error ${res.status}`);

        const data = await res.json();
        setWorkout(data);
      } catch (e) {
        setErr(e.message || "Failed to load workout");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [Name, navigate]);

  if (loading) return <p>Loading workout…</p>;
  if (err) return <p style={{ color: "red" }}>{err}</p>;
  if (!workout) return null;

  // displays the specific chosen workout details
  const title = workout.Name || workout.name;
  const description = workout.Description || workout.description;
  const sections = workout.Sections || workout.sections || [];

  return (
    <>
      <header className="nav-bar">
      <NavBar />
      </header>
      <div className="back-button-container">
        <button className="back-button" onClick={() => navigate(-1)}>
          Back to Workouts List
        </button>
      </div>
      <div className="workout-container">
        <div className="workout-detail">
          <h2 className="workout-title">{title}</h2>
          <p className="workout-description">{description}</p>

          {sections.length === 0 ? (
            <p>No sections found!</p>
          ) : (
            <div className="sections-container">
              {sections.map((section) => {
                const sectionName = section.SectionName || "Untitled Section";
                const routines = section.Routines || [];

                return (
                  <div key={section.ID} className="section-card">
                    <h3 className="section-title">{sectionName}</h3>

                    {routines.length === 0 ? (
                      <p>No routines found!</p>
                    ) : (
                      <ul className="routine-list">
                        {routines.map((routine) => (
                          <li key={routine.ID} className="routine-item">
                            <div>
                              <div className="routine-row">
                                <span className="routine-name">{routine.Name}</span>
                                {routine.RepsDuration && (
                                  <span className="routine-duration">
                                    {" "}
                                    - {routine.RepsDuration}
                                  </span>
                                )}
                              </div>
                            </div>
                            {routine.RoutineDescription && (
                              <p className="routine-desc">{routine.RoutineDescription}</p>
                            )}
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
