import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import axios from 'axios';
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBBtn,
  MDBCardImage,
  MDBRow,
  MDBCol
} from 'mdb-react-ui-kit';

import "react-responsive-carousel/lib/styles/carousel.min.css";

import Cards from "../cards/Cards";

const Challan = props => {
  const { challanId } = (props.location && props.location.state) || {};
  const [licenseNumber, setLicenseNumber] = useState("")
  const [status, setStatus] = useState("")
  const [amount, setAmount] = useState(0)
  const [dateTime, setDateTime] = useState("")
  const [locations, setLocations] = useState("")
  const [rider, setRider] = useState("")
  const [image, setImage] = useState("")
  const [name, setName] = useState("")

  console.log(props.location && props.location.state)

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/challan/' + challanId).then((res) => {
      const content = res.data;
      console.log("data");
      console.log(content);
      setLicenseNumber(content.license_number);
      setStatus(content.status)
      setAmount(content.amount)
      setDateTime(content.date_time)
      setLocations(content.locations)
      setRider(content.rider)
    })

    axios.get('http://127.0.0.1:8000/rider/' + rider).then((res) => {
      const content = res.data;
      console.log("rider");
      console.log(content);
      setName(content.name);
    })

    axios.get('http://127.0.0.1:8000/challan_image/?challan=' + challanId).then((res) => {
      console.log(res.data[0].image);
      setImage(res.data[0].image);
    })
    console.log("amount:" + amount);
  });

  return (
    <div>
      <NavLink to="/">
        Go Back
      </NavLink>
      <hr />

      <MDBCard className='m-3 p-3'>
        <MDBCardBody>
          <MDBCardTitle>Card title</MDBCardTitle>
          <MDBCard style={{ maxWidth: '100%' }}>
          <MDBRow className='g-0'>
            <MDBCol md='4'>
              <MDBCardImage src={image} alt='...' fluid className="p-3" />
            </MDBCol>
            <MDBCol md='8'>
              <MDBCardBody>
                <MDBCard className="p-3">
                  <Cards title="Challan ID" value={challanId} />
                  <Cards title="License Number" value={licenseNumber} />
                  <Cards title="Status" value={status} />
                  <Cards title="Amount" value={amount} />
                  <Cards title="Date Time" value={dateTime} />
                  <Cards title="Location" value={locations} />
                  <Cards title="Name" value={name} />
                </MDBCard>
              </MDBCardBody>
            </MDBCol>
          </MDBRow>
        </MDBCard>

        <MDBRow>
          <MDBCol sm='6'>
            <MDBCard alignment='center' className="m-3">
              <MDBCardBody>
                 <MDBBtn>Raise Query</MDBBtn>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
          <MDBCol sm='6'>
            <MDBCard alignment='center' className="m-3">
              <MDBCardBody>
                <MDBBtn>Pay Now</MDBBtn>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
        </MDBRow>

        </MDBCardBody>
      </MDBCard>
    </div>
  );
};

export default Challan;
