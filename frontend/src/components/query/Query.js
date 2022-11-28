import React from 'react'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export default function Query() {
  return (
   <Form>
      <Form.Group className="mb-3">
        <Form.Label>Query</Form.Label>
        <Form.Control type="email" placeholder="Enter your query" />
      </Form.Group>

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  )
}
