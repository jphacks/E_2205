import React from 'react';
import logo from './logo.svg';
import './App.css';
import './TwitterTL.tsx'

import { useState} from "react";
import TwitterTL from './TwitterTL';

type TodoType = {
  id: number;
  todo: string;
  isDone: boolean;
};



const App: React.FC = () => {
  const [text, setText] = useState<string>("");
  const [todos, setTodos] = useState<TodoType[]>([]);

  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>): void => {
    setText(e.target.value);
  };
  const handleClick = (): void => {
    setTodos([
      ...todos,
      { id: todos.length++, todo: text, isDone: false }
    ]);
  };

  return (
    <>
      
      <div className="App">

<div className="left_element">

  <div className="title"><p>TwiCordGram</p></div>

  <div className='create_post'>
    <textarea className="text_area"
        onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => handleChange(e)}
      />
      <button className="button" onClick={(): void => handleClick()}>tweet</button>
      {todos.map((number) => (
        <p key={number.id}>
          {number.todo}
        </p>

      ))}
  </div>

  <div className='create_post'>
    Instagram新規投稿作成UI
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

    </>
  );
};
export default App;


