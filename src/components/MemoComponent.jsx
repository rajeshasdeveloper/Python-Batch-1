import React, { useState, useMemo } from "react";

const MemoComponent = () => {
  const [num, setnum] = useState(1);
  const [name, setname] = useState("");
  const getFactorial = useMemo(() => factorial(num), [num]);
  //   const getFactorial = () => {
  //     return factorial(num);
  //   };
  return (
    <>
      <h1>
        The factorial of {num} is {getFactorial}
      </h1>
      <div>
        <label>number: </label>
        <input type="text" onChange={(e) => setnum(e.target.value)} />
      </div>
      <div style={{ marginTop: "5%" }}>
        <label>name: </label>
        <input type="text" onChange={(e) => setname(e.target.value)} />
      </div>
      Your name is {name}
    </>
  );
};

const factorial = (num) => {
  console.log("I am from factorial function");
  let value = 1;
  for (let i = 1; i <= num; i++) {
    let j = 0;
    while (j <= 100000000) {
      j += 1;
    }
    value += i;
  }
  return value;
};

export default MemoComponent;
