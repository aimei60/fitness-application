//settings
import "../css/settings.css";
import NavBar from "../components/Navbar";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function Settings() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [isActive, setIsActive] = useState(false);

  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [message, setMessage] = useState("");

  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

  useEffect(() => {
    async function loadUser() {
      setMessage("");

      try {
        const res = await fetch(`${API_BASE_URL}/api/me`, {
          method: "GET",
          credentials: "include"
        });

        if (res.status === 401) {
          navigate("/login", { replace: true });
          return;
        }

        if (!res.ok) {
          throw new Error("Failed to load your information.");
        }

        const d = await res.json();;

        setEmail(d.Email || "");
        setIsActive(d.IsActive);

      } catch {
        setMessage("Failed to load your information.");
      }
    }
    loadUser();
  }, [navigate]);

  //password change
  async function handleChangePassword(e) {
    e.preventDefault();

    if (email === "demo@gmail.com") {
      setMessage("Demo account cannot change password.");
      return;
    }

    if (!currentPassword || !newPassword) {
      setMessage("Please fill in both password fields.");
      return;
    }
    if (newPassword.length < 8) {
      setMessage("New password must be at least 8 characters.");
      return;
    }

    try {
      const csrfRes = await fetch(`${API_BASE_URL}/api/csrf-token`, {
        method: "GET",
        credentials: "include"
      }); 

      if (!csrfRes.ok) {
        throw new Error("Failed to get CSRF token.");
      }

      const csrfData = await csrfRes.json();
      const csrfToken = csrfData.csrfToken;

      const res = await fetch(`${API_BASE_URL}/api/user/change-password`, {
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrfToken
        },
        body: JSON.stringify({
          current_password: currentPassword,
          new_password: newPassword
        })
      });

      if (res.status === 401) {
        navigate("/login", { replace: true });
        return;
      }

      if (!res.ok) {
        let detail = "Something went wrong.";

        try {
          const errorData = await res.json();
          if (errorData.detail) {
            detail = errorData.detail;
          }
        } catch {
        }

        throw new Error(detail);
      }

      setMessage("Password changed successfully!");
      setCurrentPassword("");
      setNewPassword("");
    } catch (e) {
      if (e.message) {
        setMessage(e.message);
      } else {
        setMessage("Something went wrong");
      }
    }
  }

  let statusText = "Inactive";
  if (isActive) {
    statusText = "Active";
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
          <p className="status">Status: {statusText}</p>
        </div>
        {/* Change Password */}
        {email !== "demo@gmail.com" && (
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
          </form>)}
          {email === "demo@gmail.com" && (<p className="demo-account">Demo account cannot update password.</p>)}
      </div>
    </>
  );
}
