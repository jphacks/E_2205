import React from 'react';
import { useState} from "react";

import './App.css';
import './TwitterTL.jsx'
import './TextBox.tsx'

import TwitterTL from './TwitterTL';
import TextBox from './TextBox';

const App: React.FC = () => {

  const [count, setCount] = useState(0);
  const countUp = () => {
    setCount(count + 1);
  }

  return(

    <div className="App">

      <div className="left_element">

        <div className="title"><p>TwiCordGram</p></div>

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

          </div>
      </div>

      <div className="right_element">
        設定アイコンとかを置く(余裕があれば)
      </div>

    </div>

  )
}

export default App;