import React from 'react'
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBCardSubTitle
} from 'mdb-react-ui-kit';

export default function Cards({title, value}) {
  return (
    <MDBCard className='m-1'>
        <MDBCardBody>
            <MDBCardTitle>{title}</MDBCardTitle>
            <MDBCardSubTitle>{value}</MDBCardSubTitle>
        </MDBCardBody>
    </MDBCard>
  )
}
