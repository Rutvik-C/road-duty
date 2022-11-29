import React, { useEffect, useState } from 'react'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Button } from 'react-bootstrap';
import { Form } from "react-bootstrap";

export default function QueryDisplay() {
  const { id } = useParams();

  const [challanId, setChallanId] = useState("")
  const [issue, setIssue] = useState("");
  const [status, setStatus] = useState("");
  const [numberPlate, setNumberPlate] = useState("");
  const [imageLink, setImageLink] = useState("");
  
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/query/' + id).then((res) => {
      const content = res.data;
      setChallanId(content.challan);
      setIssue(content.issue);
      setStatus(content.status);
    })

    axios.get(`http://127.0.0.1:8000/challan_image/?challan=${challanId}&type=whole`).then((res) => {
      setImageLink(res.data[0].image)
    })
  })

  const handleChangeNoIssue = () => {
    axios.get(`http://127.0.0.1:8000/challan/${challanId}`).then((res) => {
      const content = res.data
      content.status = "unpaid"

      axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content)
    })
  }

  const handleClickUpdate = () => {
    axios.get(`http://127.0.0.1:8000/challan/${challanId}`).then((res) => {
      const content = res.data
      content.status = "invalid"

      axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content)

      const data_to_send = {location: content.location, license_number: numberPlate, status: "unpaid"}

      axios.post('http://127.0.0.1:8000/challan/', data_to_send)
    })
  }
  
  return (
    <Card style={{ width: '100%' }}>
      <Card.Body>
        <Card.Img src={imageLink} alt="image data" />
        <Card.Title>{challanId}</Card.Title>
        <Card.Text>
          {issue}
        </Card.Text>
      </Card.Body>
      <ListGroup className="list-group-flush">
        <ListGroup.Item>Status: {status}</ListGroup.Item>
      </ListGroup>
      <Card.Body>
        <Button className='m-2' onClick={handleChangeNoIssue}>No Issues</Button>
          <Form className="register-form">
          <Form.Group controlId="username">
            <Form.Label style={{fontWeight: "bold"}}>License Plate</Form.Label>
            <Form.Control
              type="text"
              placeholder="License Plate"
              name="license_plate"
              onChange={(event) => setNumberPlate(event.target.value)}
            />
          </Form.Group>
          <Button onClick={handleClickUpdate}>
            Update
          </Button>
        </Form>
      </Card.Body>
    </Card>
  )
}
