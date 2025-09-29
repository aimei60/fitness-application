//settings
import "../css/settings.css";
import NavBar from "../components/Navbar";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import { apiGet, apiPost } from "../api"; // axios helpers (cookies + CSRF)

export default function Settings() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [isActive, setIsActive] = useState(false);

  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [message, setMessage] = useState("");

  //Load user email and active status (cookie session)
  useEffect(() => {
    apiGet("/me")
      .then((res) => {
        const d = res.data || {};
        setEmail(d.Email || d.email || "");
        setIsActive(d.IsActive ?? d.is_active ?? false);
      })
      .catch((e) => {
        if (e?.response?.status === 401) {
          navigate("/login", { replace: true });
        } else {
          setMessage("Failed to load user info.");
        }
      });
  }, [navigate]);

  //password change
  async function handleChangePassword(e) {
    e.preventDefault();

    if (!currentPassword || !newPassword) {
      setMessage("Please fill in both password fields.");
      return;
    }
    if (newPassword.length < 8) {
      setMessage("New password must be at least 8 characters.");
      return;
    }

    try {
      await apiPost("/user/change-password", {
        current_password: currentPassword,
        new_password: newPassword,
      }); 

      setMessage("Password changed successfully!");
      setCurrentPassword("");
      setNewPassword("");
    } catch (e) {
      if (e?.response?.status === 401) {
        navigate("/login", { replace: true });
      } else {
        const detail = e?.response?.data?.detail;
        setMessage(detail || e.message || "Something went wrong.");
      }
    }
  }

  return (
    <>
      <header className="nav-bar">
      <NavBar />
      </header>
      <h1 className="settings">Settings</h1>
      <div className="settings-container">
        <h1 className="password-change">Password Change</h1>

        {message && <p>{message}</p>}

        {/* User Info */}
        <div>
          <p className="email">Email: {email}</p>
          <p className="status">Status: {isActive ? "Active" : "Inactive"}</p>
        </div>

        {/* Change Password */}
        <form onSubmit={handleChangePassword}>
          <div>
            <label>Current Password</label>
            <input
              type="password"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
            />
          </div>
          <div>
            <label>New Password</label>
            <input
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>
          <button type="submit">Change Password</button>
        </form>
      </div>
    </>
  );
}
