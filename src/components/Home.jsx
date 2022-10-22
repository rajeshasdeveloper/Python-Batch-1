import { Button } from "antd";
import React, { useContext } from "react";
import { Link } from "react-router-dom";
import "../styles/homePage.css";
import Child from "./Child";
import { TitleContext } from "../App";

const Home = () => {
  const title = useContext(TitleContext);
  console.log("I am home component");
  return (
    <>
      <div id="header">
        <h1>Welcome to {title}</h1>
      </div>
      <div>
        <span>
          <Link to="/login">
            <Button size="large" type="default">
              Login
            </Button>
          </Link>
          <Link to="/register">
            <Button size="large" type="default">
              Signup
            </Button>
          </Link>
          <Link to="/users">
            <Button size="large" type="default">
              Users
            </Button>
          </Link>
        </span>
      </div>
      <div>
        <TitleContext.Provider value={"rajesh"}>
          <Child />
        </TitleContext.Provider>
      </div>
    </>
  );
};

export default Home;
