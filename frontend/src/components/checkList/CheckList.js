import React from 'react'
import {
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
} from 'mdb-react-ui-kit';
import { Link } from 'react-router-dom';

const LINKS = [
  {image: 'https://avatars.githubusercontent.com/u/2', id: 2}, 
  {image: 'https://avatars.githubusercontent.com/u/69', id: 69},
  {image: 'https://avatars.githubusercontent.com/u/100', id: 100},
  {image: 'https://avatars.githubusercontent.com/u/6969', id: 6969},
  {image: 'https://avatars.githubusercontent.com/u/1', id: 1}, 
  {image: 'https://avatars.githubusercontent.com/u/3', id: 3}, 
  {image: 'https://avatars.githubusercontent.com/u/4', id: 4}, 
  {image: 'https://avatars.githubusercontent.com/u/5', id: 5},
  {image: 'https://avatars.githubusercontent.com/u/6', id: 6},
  {image: 'https://avatars.githubusercontent.com/u/7', id: 7},
  {image: 'https://avatars.githubusercontent.com/u/111', id: 111},
  {image: 'https://avatars.githubusercontent.com/u/123', id: 123},
  {image: 'https://avatars.githubusercontent.com/u/1234', id: 1234},
]

export default function CheckList() {
  return (
    <div>
        <MDBCard className='m-3 p-3'>
            <MDBCardBody>
                <MDBCardTitle>Check List</MDBCardTitle>
                    {LINKS.map((link) =>
                      <MDBCard style={{ maxWidth: '100%' }} >
                        <MDBCard className='m-3'>
                          <MDBCardBody className="d-flex justify-content-between">
                              <MDBCardTitle>{link.id}</MDBCardTitle>
                              <Link
                                className="btn btn-primary"
                                to={{
                                    pathname: `/check/${link.id}`,
                                }}
                                activeClassName="current"
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
