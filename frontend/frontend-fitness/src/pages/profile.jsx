//profile page
import "../css/profile.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

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

  useEffect(() => {
    async function load(e) {
      e.preventDefault();
      setLoading(true);
      setMsg(null);

      try {
        const res = await fetch("/api/profile", {
          method: "GET",
          credentials: "include"
        });

        if (res.status === 401) {
          navigate("/login", { replace: true });
          return;
        }

        if (res.status === 404) {
          setMode("create")
          return
        }

        if (!res.ok) {
          throw new Error("Failed to load profile");
        }

        const data = await res.json();

        setForm({
          FullName: data.FullName || "",
          Age: data.Age || "",
          Height: data.HeightCM || "",
          Weight: data.WeightKG || "",
          FitnessLevel: data.FitnessLevel || "",
          Goal: data.Goal || "",
          InjuriesOrLimitations: data.InjuriesOrLimitations || "",
        });
        setMode("update");

      } catch {
        setMsg("Failed to load profile");
      } finally {
        setLoading(false);
      }
    }
    load();
  }, [navigate]);

  function onChange(e) {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function onSubmit(e) {
    e.preventDefault();
    setSaving(true);
    setMsg(null);

    try {
      const csrfRes = await fetch("/api/csrf-token", {
        credentials: "include"
      });

      const csrfData = await csrfRes.json();
      const csrfToken = csrfData.csrfToken;

      let ageValue = undefined;
      if (form.Age !== "") {
        ageValue = Number(form.Age);
      }

      let heightValue = undefined;
      if (form.Height !== "") {
        heightValue = Number(form.Height);
      }

      let weightValue = undefined;
      if (form.Weight !== "") {
        weightValue = Number(form.Weight);
      }

      const payload = {
        FullName: form.FullName,
        Age: ageValue,
        Height: heightValue,
        Weight: weightValue,
        FitnessLevel: form.FitnessLevel,
        Goal: form.Goal,
        InjuriesOrLimitations: form.InjuriesOrLimitations,
      };

      let method = "POST";
      if (mode === "update") {
        method = "PATCH";
      }

      const res = await fetch("/api/profile", {
        method: method,
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrfToken
        },
        body: JSON.stringify(payload)
      });

      if (res.status === 401) {
        navigate("/login", { replace: true });
        return;
      }

      if (!res.ok) {
        throw new Error("Failed to save profile");
      }

      const data = await res.json();

      setForm({
        FullName: data.FullName || "",
        Age: data.Age || "",
        Height: data.HeightCM || "",
        Weight: data.WeightKG || "",
        FitnessLevel: data.FitnessLevel || "",
        Goal: data.Goal || "",
        InjuriesOrLimitations: data.InjuriesOrLimitations || "",
      });

      setMode("update");
      setMsg("Profile saved!");
    } catch {
      setMsg("Failed to save profile");
    } finally {
      setSaving(false);
    }
  }

  let msgClass = "msg-error";
  if (msg === "Profile saved!") {
    msgClass = "msg-success";
  }

  let buttonText = "Update profile";
  if (mode === "create") {
    buttonText = "Create profile";
  }

  if (saving) {
    buttonText = "Saving…";
  }

  if (loading) {
    return <p>Loading profile...</p>;
  }

  return (
    <>
      <header className="nav-bar">
      <NavBar />
      </header>
      <div className="main-profile-container">
        <div className="profile-container">
          <h1 className="profile-title">Your Profile</h1>
          {msg && (<p className={"msg " + msgClass}>{msg}</p>)}
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
              {buttonText}
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

