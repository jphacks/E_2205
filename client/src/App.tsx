import React from 'react';
import logo from './logo.svg';
import './App.css';

import { useState} from "react";

type TodoType = {
  id: number;
  todo: string;
  isDone: boolean;
};



const App: React.FC = () => {
  const [text, setText] = useState<string>("");
  const [todos, setTodos] = useState<TodoType[]>([]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>): void => {
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

  <h1>TwiCordGram(仮)</h1>

  <div className='create_post'>
    <input
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleChange(e)}
        type="text"
      />
      <button onClick={(): void => handleClick()}>tweet</button>
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

  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>

  </div>
</div>

<div className="center_element">
  <div className="subtitle"><p>Instagram</p></div>
  <div className="timeline">

  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>
  <div className="post">
    <div className="username"><p>user</p></div>
    <p>text</p>
  </div>

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


