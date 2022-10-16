import { Button } from "antd";
import React, { useRef, useState } from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <div style={{ marginTop: "10%" }}>
        <h1>Welcome to Payment App</h1>
      </div>
      <div>
        <span>
          <Link to="/login">
            <Button type="primary" style={{ marginRight: 5 }}>
              Login
            </Button>
          </Link>
          <Link to="/register">
            <Button type="primary" style={{ marginLeft: 5 }}>
              Signup
            </Button>
          </Link>
          <Link to="/users">
            <Button type="primary" style={{ marginLeft: 10 }}>
              Users
            </Button>
          </Link>
        </span>
      </div>
    </>
  );
};

export default Home;
