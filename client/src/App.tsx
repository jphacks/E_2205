import React from 'react';
import logo from './logo.svg';
import './App.css';
import './TwitterTL.tsx'
import './TextBox.tsx'

import TwitterTL from './TwitterTL';
import TextBox from './TextBox';

function App() {
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
        <div className="subtitle"><p>Twitter</p></div>

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