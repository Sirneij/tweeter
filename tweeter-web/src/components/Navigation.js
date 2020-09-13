import React from "react";
import User1 from "../images/user1.jpg";

function Navigation() {
  return (
    <nav className="feeds-nav dark-mode-1">
      <div className="icons">
        <a href="#" className="active">
          <i className="fas fa-home"></i>
        </a>
        <a href="#">
          <i className="fas fa-hashtag"></i>
        </a>
        <a href="#">
          <i className="far fa-bell"></i>
        </a>
        <a href="#">
          <i className="far fa-envelope"></i>
        </a>
      </div>
      <div className="search-bar">
        <i className="fas fa-search"></i>
        <input
          type="text"
          placeholder="Search Twirrer"
          className="search-bar-input dark-mode-2 light-text border"
        />
      </div>
      <div className="user">
        <div className="user-img-wrapper">
          <img src={User1} alt="User picture" />
        </div>
        <a href="#" className="user-link light-text">
          Jane Smith
        </a>
        <i className="fas fa-chevron-down"></i>
      </div>
    </nav>
  );
}

export default Navigation;
