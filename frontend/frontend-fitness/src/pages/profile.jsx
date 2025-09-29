//profile page
import "../css/profile.css";
import NavBar from "../components/Navbar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiGet, apiPost, apiPatch } from "../api"; // axios helpers (cookies + CSRF)

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
    let isMounted = true;

    async function load() {
      setLoading(true);
      setMsg(null);
      try {
        const res = await apiGet("/profile"); // sends cookies
        const data = res.data;
        if (!isMounted) return;
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
      } catch (e) {
        const status = e?.response?.status;
        if (status === 401) {
          navigate("/login", { replace: true });
          return;
        }
        if (status === 404) {
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
        } else {
          setMsg(e?.response?.data?.detail || e.message || "Failed to load profile");
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

  function onChange(e) {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function onSubmit(e) {
    e.preventDefault();

    setSaving(true);
    setMsg(null);

    try {
      const toNum = (v) => (v === "" ? undefined : Number(v));
      const payload = {
        FullName: form.FullName,
        Age: toNum(form.Age),
        Height: toNum(form.Height),
        Weight: toNum(form.Weight),
        FitnessLevel: form.FitnessLevel,
        Goal: form.Goal,
        InjuriesOrLimitations: form.InjuriesOrLimitations,
      };

      const res =
        mode === "create"
          ? await apiPost("/profile", payload)
          : await apiPatch("/profile", payload);

      const data = res.data;
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
      const status = e?.response?.status;
      if (status === 401) {
        navigate("/login", { replace: true });
      } else {
        const detail = e?.response?.data?.detail;
        setMsg(detail || e.message || "Failed to save profile");
      }
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

