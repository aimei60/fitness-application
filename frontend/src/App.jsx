import Login from "./pages/login-signup.jsx";
import Homepage from './pages/homepage.jsx';
import WorkoutDetail from "./pages/WorkoutDetail.jsx";
import Profile from "./pages/profile.jsx";
import Settings from "./pages/settings.jsx";
import { Route, Routes, Navigate } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} /> {/* root url*/}
      <Route path="/login" element={<Login />} />
      <Route path="/homepage" element={<Homepage />} />
      <Route path="/workouts/:name" element={<WorkoutDetail />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/settings" element={<Settings />} />
    </Routes>
  )
}

export default App
