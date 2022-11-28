import React, { useState } from "react";
import { Form } from "react-bootstrap";
import { Link } from "react-router-dom";

const Home = props => {
  const [state, setState] = useState({
    challanId: "",
  });

  const handleInputChange = event => {
    const { name, value } = event.target;
    setState(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  return (
    <div>
      <h1>Road Duty</h1>
      <Form className="register-form">
        <Form.Group controlId="username">
          <Form.Label style={{fontWeight: "bold"}}>Challan ID</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Challan ID"
            name="challanId"
            onChange={handleInputChange}
          />
        </Form.Group>

        <Link
          className="btn btn-primary"
          to={{
            pathname: `/challan/${state.challanId}`,
            state
          }}
          // activeClassName="current"
        >
          Search
        </Link>
      </Form>

      {console.log(state)}
    </div>
  );
};

export default Home;
