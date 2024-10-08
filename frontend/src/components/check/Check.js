import React, { useEffect, useState } from 'react'
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';
import Image from '../image/Image';
import { useParams, useHistory } from 'react-router-dom';
import { Button, Form } from 'react-bootstrap';
import axios from 'axios';

export default function Check() {
  const { challanId } = useParams();    // this challanId will be used when we will be making the api calls, as of now no use, as we are showing constant carousal
  const [numberPlate, setNumberPlate] = useState("");
  const [images, setImages] = useState([]);
  const history = useHistory();

  const handleClickSubmit = () => {
    axios.get(`http://127.0.0.1:8000/challan/${challanId}/`).then((res) => {
      const content = res.data;
      content.license_number = numberPlate
      content.status = "unpaid"

      console.log("numberPlate: " + numberPlate);

      axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content)

      alert("Challan Submitted.")
      history.push('/check')
      history.go(0)
    })
  }

  const handleClickInvalid = () => {
    axios.get(`http://127.0.0.1:8000/challan/${challanId}/`).then((res) => {
      const content = res.data;
      content.status = "invalid"

      axios.put(`http://127.0.0.1:8000/challan/${challanId}/`, content)
      
      alert("Marked as Invalid case.")
      history.push('/check')
      history.go(0)
    })
  }

  useEffect(() => {
    axios.get(`http://localhost:8000/challan_image/?challan=${challanId}`).then((res) => {
      const content = res.data;
      setImages(content)
      console.log(content);
    })
  }, [])

  return (
    <div>
        <Form>
            <Form.Group className="mb-3">
                <Form.Control type="text" placeholder="License Plate Number" name="licensePlateNumber" onChange={(event) => setNumberPlate(event.target.value)} />
            </Form.Group>

            <Button className='mr-2' onClick={handleClickSubmit}>
                Submit
            </Button>

            <Button variant="danger" className='m-2' onClick={handleClickInvalid}>
                Invalid
            </Button>
      </Form>
      <Carousel>
          {images.map((image) =>
            <Image key={image.id} link={image.image} />
          )}
        </Carousel>
    </div>
  )
}
