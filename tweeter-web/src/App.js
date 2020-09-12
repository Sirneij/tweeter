import React, { useEffect, useState } from "react";
import logo from "./logo.svg";
import "./App.css";

function loadTweets(callback) {
  const xhr = new XMLHttpRequest();
  const method = "GET";
  const response = "json";
  const url = "http://localhost:8000/api/tweets/";

  xhr.responseType = response;
  xhr.open(method, url);
  xhr.onload = () => {
    callback(xhr.response, xhr.status);
  };
  xhr.onerror = (e) => {
    console.log(e);
    callback({ message: "There was an error fetching the data..." }, 400);
  };
  xhr.send();
}

function Tweet(props) {
  const { tweet } = props;
  const className = props.className
    ? props.className
    : "feeds-content dark-mode-2";
  return (
    <div className={className}>
      <p>
        {tweet.id} -{tweet.content}
      </p>
    </div>
  );
}

function App() {
  const [tweets, setTweets] = useState([]);
  useEffect(() => {
    //do lookups
    const myCallback = (response, status) => {
      console.log(response, status);
      if (status === 201) {
        setTweets(response);
      } else {
        //alert("There was an error");
      }
    };
    loadTweets(myCallback);
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        {tweets.map((tweet, index) => {
          return <Tweet tweet={tweet} key={`${index}-{tweet.id}`} />;
        })}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
