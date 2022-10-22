import "./App.css";
import React, { createContext } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Register from "./components/Register";
import Login from "./components/Login";
import HeaderComponent from "./components/HeaderComponent";
import UserDetails from "./components/UserDetails";
import RefComponent from "./components/RefComponent";
import MemoComponent from "./components/MemoComponent";
import CallBackComponent from "./components/CallBackComponent";
import Child from "./components/Child";
import ReducerComponent from "./components/ReducerComponent";

export const TitleContext = createContext();

function App() {
  return (
    <div className="App">
      <Router>
        <HeaderComponent />
        <Routes>
          <Route
            path="/"
            element={
              <TitleContext.Provider value={"Payment App"}>
                <Home />
              </TitleContext.Provider>
            }
          />

          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/users" element={<UserDetails />} />
          <Route path="/ref" element={<RefComponent />} />
          <Route path="/memo" element={<MemoComponent />} />
          <Route path="/callback" element={<CallBackComponent />} />
          <Route path="/reducer" element={<ReducerComponent />} />
          <Route
            path="/child"
            element={
              <TitleContext.Provider value={"Payment App"}>
                <Child />
              </TitleContext.Provider>
            }
          />
          <Route>404 Not found!</Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
