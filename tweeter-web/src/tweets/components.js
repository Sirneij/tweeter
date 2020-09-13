import React, { useEffect, useState } from "react";
import User2 from "../images/user2.jpg";
import PostImg1 from "../images/post-img-1.jpg";
import User1 from "../images/user1.jpg";
import { loadTweets } from "../lookup";

import FollowSidebar from "../components/FollowSidebar";

export function TweetContainer(props) {
  const inputTextRef = React.createRef();
  const [newTweets, setNewTweets] = useState([]);
  const handSubmit = (e) => {
    e.preventDefault();
    const newTweetValue = inputTextRef.current.value;
    let tempNewTweets = [...newTweets];
    tempNewTweets.unshift({
      content: newTweetValue,
      likes: 0,
      id: 123,
    });
    setNewTweets(tempNewTweets);
    inputTextRef.current.value = "";
  };
  return (
    <div className="feeds-content dark-mode-2">
      <form
        method="POST"
        className="feeds-header dark-mode-1"
        onSubmit={handSubmit}
      >
        <div className="header-top border">
          <h4 className="light-text">Home</h4>
          <i className="far fa-star"></i>
        </div>
        <div className="header-post dark-mode-1 border">
          <div className="header-img-wrapper">
            <img src={User1} alt="Author" />
          </div>

          <input type="hidden" name="next" value="/" />
          <input
            type="text"
            ref={inputTextRef}
            placeholder="What's happening?"
            className="dark-mode-2 light-text border"
            name="tweet"
            required={true}
          />
        </div>
        <div className="additionals">
          <i className="far fa-image"></i>
          <i className="fas fa-camera"></i>
          <i className="fas fa-chart-bar"></i>
          <button type="submit" className="follow-btn" title="tweet">
            Tweet
          </button>
        </div>
        <hr />
        <div className="d-none alert alert-danger" id="error"></div>
      </form>
      <div className="posts dark-mode-1">
        <TweetsList newTweets={newTweets} />
      </div>
      <FollowSidebar />
    </div>
  );
}

export const ActionButton = (props) => {
  const { tweet, action } = props;
  const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0);
  const [userLiked, setUserLiked] = useState(
    tweet.userLiked === true ? true : false
  );
  const actionDisplay = action.display ? action.display : "action";
  const className = props.className ? props.className : "far fa-heart";
  const handleClick = (e) => {
    e.preventDefault();
    if (action.type === "like") {
      if (userLiked === true) {
        setLikes(likes - 1);
        setUserLiked(false);
      } else {
        setLikes(likes + 1);
        setUserLiked(true);
      }
    }
  };
  const display =
    action.type === "like" ? `${likes} ${actionDisplay}` : actionDisplay;
  return (
    <i className={className} onClick={handleClick}>
      {display}
    </i>
  );
};

export function Feeds(props) {
  const { tweet } = props;
  return (
    <div className="post border">
      <div className="user-avatar">
        <img src={User2} alt="Author" />
      </div>
      <div className="post-content">
        <div className="post-user-info light-text">
          <h4>Helen Brown</h4>
          <i className="fas fa-check-circle"></i>
          <span>@helenbrown 15m</span>
        </div>
        <p className="post-text light-text">{tweet.content}</p>
        <div className="post-img">
          <img src={PostImg1} alt="Post" />
        </div>
        <div className="post-icons">
          {/* <ActionButton className="far fa-comment" tweet={tweet} /> */}
          <ActionButton
            tweet={tweet}
            action={{ type: "retweet", display: "retweet" }}
            className="fas fa-retweet"
          />
          <ActionButton
            tweet={tweet}
            action={{ type: "like", display: "likes" }}
            className="far fa-heart"
          />
        </div>
      </div>
    </div>
  );
}

export function TweetsList(props) {
  const [tweetInit, setTweetInit] = useState([]);
  console.log(props.newTweets);
  useEffect(() => {
    //do lookups
    const myCallback = (response, status) => {
      if (status === 201) {
        setTweetInit(response);
      } else {
        //alert("There was an error");
      }
    };
    loadTweets(myCallback);
  }, []);

  return tweetInit.map((tweet, index) => {
    return <Feeds tweet={tweet} key={index - tweet.id} />;
  });
}
