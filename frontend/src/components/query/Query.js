import axios from 'axios';
import React, { useState } from 'react'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import { useParams,useHistory } from "react-router-dom";

export default function Query() {
  const { challanId } = useParams();
  const [issue, setIssue] = useState("");
  const history = useHistory();

  const handleClick = (e) => {
    // e.preventDefault()
    axios.get('http://127.0.0.1:8000/challan/' + challanId).then((res) => {
      const content = res.data;
      content.status = "query_raised";

      axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content);
    })

    const data = {
      status: "query_raised",
      challan: challanId,
      issue: issue
    }

    axios.post('http://127.0.0.1:8000/query/', data).then(res => {
        setIssue("");
        alert("Query Submitted.")

        history.push(`/challan/${challanId}/`)
        history.go(0)
    }); 
  }

  return (
   <Form>
      <Form.Group className="mb-3">
        <Form.Label>Query</Form.Label>
        <Form.Control type="text" name="issue" onChange={(event) => setIssue(event.target.value)} placeholder="Enter your query" />
      </Form.Group>

      <Button variant="primary" onClick={handleClick}>
        Submit
      </Button>
    </Form>
  )
}
