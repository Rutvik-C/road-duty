import React from 'react'
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';
import Image from '../image/Image';
import { useParams } from 'react-router-dom';

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

export default function Carousal() {
  // eslint-disable-next-line
  const { challanId } = useParams();    // this challanId will be used when we will be making the api calls, as of now no use, as we are showing constant carousal
  return (
    <div>
        <Carousel>
          {LINKS.map((link) =>
            <Image key={link.id} link={link.image} />
          )}
        </Carousel>
        {/* carousal */}
    </div>
  )
}
