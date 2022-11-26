import React from 'react'

export default function Image({link}) {
    console.log("link: " + link);
  return (
    <div>
        <img src={link} style={{ maxWidth: '100%', maxHeight: '400px' }} alt="" />
    </div>
  )
}
