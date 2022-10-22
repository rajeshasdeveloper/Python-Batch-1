import React, { useContext } from "react";
import { TitleContext } from "../App";

const Child = () => {
  const title = useContext(TitleContext);
  return <div>Value from props {title}</div>;
};

export default Child;
