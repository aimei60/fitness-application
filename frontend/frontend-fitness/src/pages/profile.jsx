//profile page

import "../css/profile.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const BASE = (import.meta.env.VITE_API_URL || "").replace(/\/+$/, "");

export default function Profile() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    FullName: "",
    Age: "",
    Height: "",
    Weight: "",
    FitnessLevel: "",
    Goal: "",
    InjuriesOrLimitations: "",
  });

  const [mode, setMode] = useState("create");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [msg, setMsg] = useState(null);

  // check the user is logged in or send user to login page
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login", { replace: true });
      return;
    }

    //loads, fetches and displays profile page using saved token. 
    //if token is invalid, send to login page
    //else display error message.
    async function load() {
      setLoading(true);
      setMsg(null);
      try {
        const res = await fetch(`${BASE}/profile`, {
          headers: {"Content-Type": "application/json", Authorization: `Bearer ${token}`},
        });

        if (res.status === 401) {
          localStorage.removeItem("access_token");
          navigate("/login", { replace: true });
          return;
        }

        if (res.status === 404) {
          // if no profile yet then create show empty form
          setMode("create");
          setForm({
            FullName: "",
            Age: "",
            Height: "",
            Weight: "",
            FitnessLevel: "",
            Goal: "",
            InjuriesOrLimitations: "",
          });
          return;
        }
        if (!res.ok) throw new Error(`Error ${res.status}`);

        // allows user to enter profile details
        const data = await res.json();
        setForm({
          FullName: data.FullName || "",
          Age: data.Age ?? "",
          Height: data.HeightCM ?? "",
          Weight: data.WeightKG ?? "",
          FitnessLevel: data.FitnessLevel || "",
          Goal: data.Goal || "",
          InjuriesOrLimitations: data.InjuriesOrLimitations || "",
        });
        //allows user to update if needed
        setMode("update");
      } catch (e) {
        setMsg(e.message || "Failed to load profile");
      } finally {
        setLoading(false);
      }
    }

    load();
  }, [navigate]);

   // updates form state as the user types e.g FullName: "" to FullName: "John"
  function onChange(e) {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function onSubmit(e) {
    e.preventDefault();
    const token = localStorage.getItem("access_token");
    if (!token) {navigate("/login", { replace: true });
      return;
    }

    setSaving(true);
    setMsg(null);
    
    // decide create or update
    try {
      const method = mode === "create" ? "POST" : "PATCH";

      // gets the data ready
      const toNum = (v) => (v === "" ? undefined : Number(v));
      const payload = {
        FullName: form.FullName,
        Age: toNum(form.Age),
        Height: toNum(form.Height), 
        Weight: toNum(form.Weight), // 
        FitnessLevel: form.FitnessLevel,
        Goal: form.Goal,
        InjuriesOrLimitations: form.InjuriesOrLimitations,
      };

      // checks again if token expired or not
      const res = await fetch(`${BASE}/profile`, {
        method,
        headers: {"Content-Type": "application/json", Authorization: `Bearer ${token}`},
        body: JSON.stringify(payload),
      });

      if (res.status === 401) {
        localStorage.removeItem("access_token");
        navigate("/login", { replace: true });
        return;
      }
      if (!res.ok) {
        let detail = "";
        try {
          const j = await res.json();
          detail = j?.detail;
        } catch {}
        throw new Error(detail || `Failed to save profile (${res.status})`);
      }

      const data = await res.json();
      setForm({
        FullName: data.FullName || "",
        Age: data.Age ?? "",
        Height: data.HeightCM ?? "",
        Weight: data.WeightKG ?? "",
        FitnessLevel: data.FitnessLevel || "",
        Goal: data.Goal || "",
        InjuriesOrLimitations: data.InjuriesOrLimitations || "",
      });
      setMode("update");
      setMsg("Profile saved!");
    } catch (e) {
      setMsg(e.message || "Failed to save profile");
    } finally {
      setSaving(false);
    }
  }

  return (
    <>
      <header className="nav-bar">
      <NavBar />
      </header>
      <div className="main-profile-container">
        <div className="profile-container">
          <h1 className="profile-title">Your Profile</h1>

          {/* success or error message*/}
          {msg && (
            <p className={`msg ${msg === "Profile saved!" ? "msg-success" : "msg-error"}`}>
              {msg}
            </p>
          )}

          <form onSubmit={onSubmit} className="form">
            {/* Full Name */}
            <div className="field">
              <label className="wording-label">Full name</label>
              <input
                className="input"
                name="FullName"
                value={form.FullName}
                onChange={onChange}
                required
              />
            </div>

            {/* Age */}
            <div className="grid">
              <div className="field">
                <label className="label">Age</label>
                <input
                  type="number"
                  className="input"
                  name="Age"
                  value={form.Age}
                  onChange={onChange}
                  required
                  min="0"
                  max={120}
                />
              </div>
              
              {/* Height */}
              <div className="field">
                <label className="label">Height (cm)</label>
                <input
                  type="number"
                  className="input"
                  name="Height"
                  required
                  min={100}
                  max={250}
                  value={form.Height}
                  onChange={onChange}
                />
              </div>

              {/* Weight */}
              <div className="field">
                <label className="label">Weight (kg)</label>
                <input
                  type="number"
                  className="input"
                  name="Weight"
                  required
                  min={30}
                  max={300}
                  value={form.Weight}
                  onChange={onChange}
                />
              </div>

              {/* Fitness Level */}
              <div className="field">
                <label className="label">Fitness level</label>
                <input
                  className="input"
                  name="FitnessLevel"
                  value={form.FitnessLevel}
                  onChange={onChange}
                  placeholder="Beginner / Intermediate / Advanced"
                />
              </div>
            </div>

            {/* Goal */}
            <div className="field">
              <label className="label">Goal</label>
              <input
                className="input"
                name="Goal"
                value={form.Goal}
                onChange={onChange}
                placeholder="Lose weight, gain muscle, etc."
              />
            </div>

            {/* Injuries / limitations */}
            <div className="field">
              <label className="label">Injuries or limitations</label>
              <textarea
                className="input"
                name="InjuriesOrLimitations"
                rows="3"
                value={form.InjuriesOrLimitations}
                onChange={onChange}
              />
            </div>

            {/* Submit button */}
            <button type="submit" className="btn" disabled={saving}>
              {saving ? "Saving…" : mode === "create" ? "Create profile" : "Update profile"}
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

