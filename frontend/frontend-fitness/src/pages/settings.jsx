import "../css/settings.css";
import NavBar from "../components/Navbar";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

const BASE = (import.meta.env.VITE_API_URL || "").replace(/\/+$/, "");

export default function Settings() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [isActive, setIsActive] = useState(false);

  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [message, setMessage] = useState("");

  // Load user email and active status. if no acess token, take them back to login page
  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login", { replace: true });
      return;
    }

    fetch(`${BASE}/me`, {
      headers: {
        "Content-Type": "application/json", Authorization: `Bearer ${token}`,},})
      .then((res) => {
        if (res.status === 401) {
          localStorage.removeItem("access_token");
          navigate("/login", { replace: true });
          return;
        }
        return res.json();
      })
      .then((data) => {
        if (data) {
          setEmail(data.Email || data.email || "");
          setIsActive(data.IsActive ?? data.is_active ?? false);
        }
      })
      .catch(() => setMessage("Failed to load user info."));
  }, [navigate]);

  //password change
  async function handleChangePassword(e) {
    e.preventDefault();
    const token = localStorage.getItem("access_token");
    if (!token) return navigate("/login", { replace: true });

    if (!currentPassword || !newPassword) {
        setMessage("Please fill in both password fields.");
        return;
    }
    if (newPassword.length < 8) {
        setMessage("New password must be at least 8 characters.");
        return;
    }

    try {
        const res = await fetch(`${BASE}/user/change-password`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
            current_password: currentPassword,
            new_password: newPassword,
        }),
        });

        if (res.status === 401) {
        localStorage.removeItem("access_token");
        navigate("/login", { replace: true });
        return;
        }
        if (!res.ok) {
        // make FastAPI errors readable
        let msg = `Failed to change password (${res.status})`;

        try {
        const data = await res.json();

        // FastAPI usually sends error info in "detail"
        if (data.detail) {
            if (Array.isArray(data.detail)) {
            // e.g. [{"loc": ["body","new_password"], "msg": "Field required"}]
            msg = data.detail
                .map(err => `${err.loc[1]}: ${err.msg}`) // "new_password: Field required"
                .join("; ");
            } else if (typeof data.detail === "string") {
            // e.g. "Invalid token"
            msg = data.detail;
            }
        }
        } catch (error) {
        //default msg
        }

        throw new Error(msg);
    }

        setMessage("Password changed successfully!");
        setCurrentPassword("");
        setNewPassword("");
    } catch (err) {
        setMessage(err.message || "Something went wrong.");
    }
    }


  return (
    <>
      <NavBar />
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
