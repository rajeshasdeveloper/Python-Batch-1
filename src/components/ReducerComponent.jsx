import React, { useReducer, useState } from "react";

const initialState = [
  {
    name: "python",
  },
  {
    name: "javaScript",
  },
];

const languageReducer = (state, action) => {
  const { type, label } = action;
  switch (type.toLowerCase()) {
    case "python":
      return { ...state, label };
    case "javascript":
      return { ...state, label };
    default:
      return { ...state, label };
  }
};

const ReducerComponent = () => {
  const [name, setname] = useState("");
  const [currentState, dispatch] = useReducer(languageReducer, initialState);
  const languageDispatcher = (e) => {
    e.preventDefault();
    dispatch({ type: name, label: `Welcome ${name} Developer` });
  };
  return (
    <>
      <h1>{currentState.label}</h1>
      <div style={{ margin: "5% 0" }}>
        <label> name: </label>
        <input type="text" onChange={(e) => setname(e.target.value)} />
      </div>
      <div>
        <button onClick={languageDispatcher}>show</button>
      </div>
    </>
  );
};

export default ReducerComponent;
