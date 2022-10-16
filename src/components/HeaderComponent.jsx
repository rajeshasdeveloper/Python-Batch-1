import { Layout, Menu } from "antd";
import React from "react";
import { Link } from "react-router-dom";
const { Header } = Layout;
const HeaderComponent = () => (
  <Layout className="layout">
    <Link to="/">
      <Header>
        <div className="logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={["2"]}
          items={new Array(1).fill(null).map((_, index) => {
            const key = index + 1;
            return {
              key,
              label: `Payment App`,
            };
          })}
        />
      </Header>
    </Link>
  </Layout>
);
export default HeaderComponent;
