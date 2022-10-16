import { Button, Checkbox, Form, Input } from "antd";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { loginUser } from "../apis/userLogin";
import Success from "./Success";

const Login = () => {
  const [color, setColor] = useState("green");
  const [loginData, setloginData] = useState("");
  const onFinish = async (values) => {
    const userData = {
      email: values.email,
      password: values.password,
    };
    const response = await loginUser(userData);
    setloginData(response.message || response.error);
    if ("error" in response) {
      setColor("red");
    }
  };
  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };
  return (
    <>
      <Form
        name="basic"
        labelCol={{
          span: 8,
        }}
        wrapperCol={{
          span: 16,
        }}
        initialValues={{
          remember: true,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
        style={{
          maxWidth: "20%",
          marginTop: "10%",
          marginLeft: "37%",
        }}
      >
        <Form.Item
          label="email"
          name="email"
          rules={[
            {
              required: true,
              type: "email",
              message: "Please input your email!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[
            {
              required: true,
              message: "Please input your password!",
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item
          name="remember"
          valuePropName="checked"
          wrapperCol={{
            offset: 8,
            span: 16,
          }}
        >
          <Checkbox>Remember me</Checkbox>
        </Form.Item>

        <Form.Item
          wrapperCol={{
            offset: 8,
            span: 16,
          }}
        >
          <Button type="primary" htmlType="submit">
            Login
          </Button>
        </Form.Item>
      </Form>
      <div>
        Not a user?
        <Link to="/register"> Register here</Link>
      </div>

      {loginData ? <Success message={loginData} color={color} /> : ""}
    </>
  );
};
export default Login;
