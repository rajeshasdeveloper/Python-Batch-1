import React, { useEffect, useState } from "react";
import { Card, Col, Row } from "antd";
import { fetchUserDetails } from "../apis/getUserData";

const UserDetails = () => {
  const [userData, setUserData] = useState("");
  useEffect(() => {
    (async () => {
      const users = await fetchUserDetails();

      setUserData(users);
    })();
  }, []);

  return (
    <>
      {userData ? (
        <>
          <div className="site-card-wrapper">
            {userData.map((el) => (
              <Row gutter={16} key={el[0]}>
                <Col span={8}>
                  <Card bordered={false}>{el[2]}</Card>
                </Col>
                <Col span={8}>
                  <Card bordered={false}>{el[1]}</Card>
                </Col>
                <Col span={8}>
                  <Card bordered={false}>{el[3]}</Card>
                </Col>
              </Row>
            ))}
          </div>
        </>
      ) : (
        <h1>Loading ...</h1>
      )}
    </>
  );
};

export default UserDetails;
