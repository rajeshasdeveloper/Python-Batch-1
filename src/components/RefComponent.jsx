import { Radio } from "antd";
import React, { useState, useRef, useEffect } from "react";

const RefComponent = () => {
  const [Name, setName] = useState("");
  const [logout, setlogout] = useState("");
  const currentElm = useRef("");
  useEffect(() => {}, [Name]);
  return (
    <div style={{ margin: "5% 0" }}>
      <h1>Your name is {Name || "empty"}</h1>
      <h1>{logout && currentElm.current.value ? logout : null}</h1>
      <label>name: </label>
      <input
        type="text"
        value={Name}
        ref={currentElm}
        onChange={(e) => {
          e.preventDefault();
          return setName(e.target.value);
        }}
      />
      <div style={{ marginTop: "5%" }}>
        <button
          onClick={() => {
            setName("");
            setlogout(`Logout successful for ${currentElm.current.value}`);
            currentElm.current.focus();
          }}
        >
          Logout
        </button>
      </div>
    </div>
  );
};

export default RefComponent;
