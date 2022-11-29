import React, {useState, useEffect} from 'react'
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
} from 'mdb-react-ui-kit';
import { Link } from 'react-router-dom';

import axios from 'axios';

export default function CheckList() {
  const [challans, setChallans] = useState([]);
  useEffect(() => {
    axios.get("http://localhost:8000/challan/?status=to_check_manually").then((res) => {
      const content = res.data;
      setChallans(content)
      console.log(content);
    })
  }, [])
  return (
    <div>
        <MDBCard className='m-3 p-3'>
            <MDBCardBody>
                <MDBCardTitle>Check List</MDBCardTitle>
                    {challans.map((challan) =>
                      <MDBCard key={challan.id} style={{ maxWidth: '100%' }} >
                        <MDBCard className='m-3'>
                          <MDBCardBody className="d-flex justify-content-between">
                              <MDBCardTitle>{challan.id}</MDBCardTitle>
                              <Link
                                className="btn btn-primary"
                                to={{
                                    pathname: `/check/${challan.id}`,
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
