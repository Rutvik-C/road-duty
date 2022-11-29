import React from 'react'

export default function Image({link}) {
    console.log("link: " + link);
  return (
    <div>
        <img src={link} style={{ maxHeight: '50%' }} alt="" />
    </div>
  )
}
