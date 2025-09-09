import Login from "./pages/login-signup";
import Homepage from './pages/homepage';
import WorkoutDetail from "./pages/WorkoutDetail";
import { Route, Routes, Navigate } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} /> {/* root url*/}
      <Route path="/login" element={<Login />} />
      <Route path="/homepage" element={<Homepage />} />
      <Route path="/workouts/:name" element={<WorkoutDetail />} />
    </Routes>
  )
}

export default App
