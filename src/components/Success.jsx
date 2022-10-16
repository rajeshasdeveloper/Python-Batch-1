import React from "react";

const Success = (props) => {
  console.log(props);
  const { message, token } = props;
  console.log(message);
  localStorage.setItem(token, token);
  return (
    <div style={{ marginTop: "5%" }}>
      <h1 style={{ color: props.color }}>{message.toUpperCase()}</h1>
    </div>
  );
};

export default Success;
