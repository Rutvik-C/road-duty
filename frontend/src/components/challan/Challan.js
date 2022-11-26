import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import axios from 'axios';
  

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
  const [phone, setPhone] = useState("")
  const [email, setEmail] = useState("")

  const IMAGE = "https://images.unsplash.com/photo-1500964757637-c85e8a162699?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXRpZnVsJTIwbGFuZHNjYXBlc3xlbnwwfHwwfHw%3D&w=1000&q=80"

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
      setPhone(content.phone)
      setEmail(content.email)
    })

    axios.get('http://127.0.0.1:8000/challan_image/?challan=' + challanId).then((res) => {
      console.log(res.data[0].image);
      setImage(res.data[0].image);
    })
  });

  return (
    <div>
      <NavLink to="/" activeClassName="active">
        Go Back
      </NavLink>
      <hr />
      <div>
        <img src={IMAGE} alt="image not found" />
      </div>
      <div className="form-details d-flex justify-content-between">
        <div>
          <div>
            <img src={image} alt="image not found" />
          </div>
        </div>
        <div className="w-100 p-3">
          <div>
            <strong>Challan ID:</strong> {challanId}
          </div>
          <div>
            <strong>License Number:</strong> {licenseNumber}
          </div>
          <div>
            <strong>Status:</strong> {status}
          </div>
          <div>
            <strong>Amount:</strong> {amount}
          </div>
          <div>
            <strong>Date Time:</strong> {dateTime}
          </div>
          <div>
            <strong>Challan ID:</strong> {challanId}
          </div>
          <div>
            <strong>Locations:</strong> {locations}
          </div>
          <div>
            <strong>Name:</strong> {name}
          </div>
          <div>
            <strong>Phone:</strong> {phone}
          </div>
          <div>
            <strong>E-mail:</strong> {email}
          </div>
        </div>        
      </div>
    </div>
  );
};

export default Challan;
