import React from 'react';
import './App.css';

import {useState} from "react";

type TodoType = {
  id: number;
  todo: string;
  isDone: boolean;
};

const TextBox: React.FC = () => {
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
    <div className="TextBox">
        <input
            onChange={(e: React.ChangeEvent<HTMLInputElement>) => handleChange(e)}
            type="text"
        />
        <input
            type="file"
            id="avatar" name="avatar"
            accept="image/png, image/jpeg">
        </input>
        <br></br>
        <button onClick={(): void => handleClick()}>New Post</button>
        {
            todos.map((number) => (
            <p key={number.id}>
                {number.todo}
            </p>
        ))}
    </div>
  );
};

export default TextBox;


