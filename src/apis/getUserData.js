import axios from "axios";

export const fetchUserDetails = async () => {
  const res = await axios
    .get("http://localhost:4444/user/details")
    .catch((err) => console.log(err.message));
  return res.data;
};
