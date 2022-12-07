import React from 'react'
import {
    MDBCard,
    MDBCardBody,
    MDBCardTitle,
  } from 'mdb-react-ui-kit';

import { Link } from "react-router-dom";

export default function Query() {

  return (
   <>
   
   <MDBCard className='m-3 p-3' alignment='center'>
        {/* <MDBCardBody>
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
        </MDBCardBody> */}
        <Link
          className="btn btn-outline-dark m-3 p-3"
          to={{
            pathname: `/check/`,
          }}
        >
          Manual Check
        </Link>

        <Link
          className="btn btn-outline-dark m-3 p-3"
          to={{
            pathname: `/query/`,
          }}
        >
          Query
        </Link>

    </MDBCard>
    </>
  )
}
