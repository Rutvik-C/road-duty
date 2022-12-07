import React, { useState, useEffect } from 'react'
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
} from 'mdb-react-ui-kit';
import { Link } from 'react-router-dom';

import axios from 'axios';

export default function QueryList() {
  const [queries, setQueries] = useState([]);
  
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/query/').then((res) => {
      const content = res.data;
      console.log(content);
      setQueries(content);
    })
  }, [])

  return (
    <div>
        <MDBCard className='m-3 p-3'>
            <MDBCardBody>
                <MDBCardTitle>Query List</MDBCardTitle>
                    {queries.map((query) =>
                      <MDBCard key={query.id} style={{ maxWidth: '100%' }} >
                        <MDBCard className='m-3'>
                          <MDBCardBody className="d-flex justify-content-between">
                              <MDBCardTitle>Challan {query.challan}</MDBCardTitle>
                              <Link
                                className="btn btn-primary"
                                to={{
                                    pathname: `/query/${query.id}`,
                                }}
                              >
                                Go
                            </Link>
                          </MDBCardBody>
                        </MDBCard>
                      </MDBCard>
                    )}
            </MDBCardBody>
        </MDBCard>
    </div>
  )
}
