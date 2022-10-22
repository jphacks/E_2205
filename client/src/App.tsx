import React from 'react';
import { useState} from "react";

import './App.css';
import './TwitterTL.jsx'
import './TextBox.tsx'

import TwitterTL from './TwitterTL';
import InstagramTL from './InstagramTL';
import TextBox from './TextBox';

const App: React.FC = () => {

  const [count, setCount] = useState(0);
  const countUp = () => {
    setCount(count + 1);
  }

  return(

    <div className="App">

      <div className="left_element">

        <div className="title"><p>Twi<span style={{
          textDecorationLine: "line-through",
          textDecorationStyle: "double",
          textDecorationColor: "red"
        }}>Cord</span>Gram</p></div>

        <div className='create_post'>
          <TextBox/>
        </div>

        <div className='create_post'>
          <TextBox/>
        </div>

      </div>

      <div className="center_element">
        <div className="subtitle"><p>Twitter<button onClick={countUp}>更新</button></p></div>

        <div className="timeline">
          <TwitterTL/>
        </div>
      </div>

<div className="center_element">
  <div className="subtitle"><p>Instagram</p></div>
    <div className="timeline">
        <InstagramTL/>
    </div>
</div>

      <div className="right_element">
        <div className="iconlike">
          <p>👤</p>
          <p>🔔</p>
          <p>📬</p>
          <p>⚙️</p>
        </div>
      </div>

    </div>

  )
}

export default App;