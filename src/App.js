import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import HeaderComponent from "./components/HeaderComponent";
import UserDetails from "./components/UserDetails";

function App() {
  return (
    <div className="App">
      <Router>
        <HeaderComponent />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/users" element={<UserDetails />} />
          <Route>404 Not found!</Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
