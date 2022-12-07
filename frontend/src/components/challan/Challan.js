import React, { useEffect, useState } from "react";
import { NavLink, useParams, Link } from "react-router-dom";
import axios from 'axios';
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardImage,
  MDBRow,
  MDBCol
} from 'mdb-react-ui-kit';

import "react-responsive-carousel/lib/styles/carousel.min.css";

import Cards from "../cards/Cards";
import { Button } from "react-bootstrap";

const Challan = props => {
  const [licenseNumber, setLicenseNumber] = useState("")
  const [status, setStatus] = useState("")
  const [amount, setAmount] = useState(0)
  const [dateTime, setDateTime] = useState("")
  const [locations, setLocations] = useState("")
  const [rider, setRider] = useState("")
  const [image, setImage] = useState("")
  const [imageWhole, setImageWhole] = useState("")
  const [name, setName] = useState("")
  const [isPaid, setIsPaid] = useState("Pay Now")

  const { challanId } = useParams();

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/challan/' + challanId).then((res) => {
      const content = res.data;
      console.log("data");
      console.log(content);
      setLicenseNumber(content.license_number);
      setStatus(content.status)
      setAmount(content.amount)
      setDateTime(content.date_time)
      setLocations(content.location)
      setRider(content.rider)

      if (content.status === "paid") {
        setIsPaid("Paid")
      }
    })

    axios.get('http://127.0.0.1:8000/rider/' + rider).then((res) => {
      const content = res.data;
      console.log("rider");
      console.log(content);
      setName(content.name);
    })

    axios.get(`http://127.0.0.1:8000/challan_image/?challan=${challanId}&type=whole`).then((res) => {
      console.log(res.data[0].image);
      setImageWhole(res.data[0].image);
    })
    axios.get(`http://127.0.0.1:8000/challan_image/?challan=${challanId}&type=cutout`).then((res) => {
      console.log(res.data[0].image);
      setImage(res.data[0].image);
    })
    console.log("amount:" + amount);
  });

  const handleClick = (event) => {
    axios.get('http://127.0.0.1:8000/challan/' + challanId).then((res) => {
        const content = res.data;
        content.status = "paid";

        // sending put request to the server to change the status to paid
        axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content);
        setIsPaid("Paid")
    })
  }

  return (
    <div>
      {/* <NavLink to="/" style={{color:"whitesmoke"}}>
        Go Back
      </NavLink> */}
      <hr />

      <MDBCard className='m-3 p-3'>
        <MDBCardImage src={imageWhole} alt='...' fluid />

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
                <Link
                  className="btn btn-dark"
                  to={{
                    pathname: `/raise_query/${challanId}`,
                  }}
                  // activeClassName="current"
                >
                  Raise Query
                </Link>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
          <MDBCol sm='6'>
            <MDBCard alignment='center' className="m-3">
              <MDBCardBody>
                <Button variant="btn btn-dark" onClick={handleClick}>{isPaid}</Button>
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
