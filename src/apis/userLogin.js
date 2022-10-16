import axios from "axios";

export const loginUser = async (userData) => {
  let res = {};
  const url = "http://localhost:4444/user/login";
  try {
    const response = await axios.post(url, userData);
    res.message = response.data.message;
    return res;
  } catch (err) {
    console.log(err);
    console.log(err.response);
    res.error = err.response.data;
    return res;
  }
};
