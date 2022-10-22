import { Layout, Menu } from "antd";
import React from "react";
import { Link } from "react-router-dom";
import "../styles/antd_header.css";

const { Header } = Layout;
const HeaderComponent = () => {
  const navigationArray = [
    { label: "Payment App", route: "/" },
    {
      label: "login",
      route: "/login",
    },
    {
      label: "register",
      route: "/register",
    },
  ];

  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu
          theme="light"
          mode="horizontal"
          defaultSelectedKeys={["2"]}
          items={navigationArray.map((object, index) => {
            const key = index + 1;
            return {
              key,
              label: <Link to={object.route}>{object.label}</Link>,
            };
          })}
        />
      </Header>
    </Layout>
  );
};
export default HeaderComponent;
