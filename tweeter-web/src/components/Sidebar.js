import React, { Component } from "react";
import User1 from "../images/user1.jpg";

class Sidebar extends Component {
  render() {
    return (
      <div className="sidebar-wrapper">
        <div className="sidebar dark-mode-1">
          <div className="sidebar-header border">
            <h2 className="light-text">Account info</h2>
            <i className="fas fa-times"></i>
          </div>
          <div className="sidebar-user">
            <div className="sidebar-user-img">
              <img src={User1} alt="User" />
            </div>
            <span>+</span>
          </div>
          <div className="sidebar-user-info light-text">
            <h4>Jane Smith</h4>
            <p>@janesmith</p>
          </div>
          <div className="following light-text">
            <p className="following-paragraph">
              <span>711</span> Following
            </p>
            <p className="following-paragraph">
              <span>7.5K</span> Followers
            </p>
          </div>
          <div className="sidebar-list-1 border">
            <ul>
              <li>
                <a href="#">
                  {" "}
                  <i className="fas fa-user"></i> Profile{" "}
                </a>
              </li>
              <li>
                <a href="#">
                  {" "}
                  <i className="far fa-list-alt"></i> Lists{" "}
                </a>
              </li>
              <li>
                <a href="#">
                  {" "}
                  <i className="far fa-bookmark"></i> Bookmarks{" "}
                </a>
              </li>
              <li>
                <a href="#">
                  {" "}
                  <i className="fab fa-adversal"></i> Ads{" "}
                </a>
              </li>
              <li>
                <a href="#">
                  {" "}
                  <i className="fas fa-chart-line"></i> Analytics{" "}
                </a>
              </li>
            </ul>
          </div>
          <div className="sidebar-list-2">
            <div className="dark-mode">
              <p>Dark Mode</p>
              <div className="toggle">
                <div className="circle"></div>
              </div>
            </div>
            <ul>
              <li>
                <a href="#">Settings and Privacy</a>
              </li>
              <li>
                <a href="#">Help Center</a>
              </li>
              <li>
                <a href="#">Log Out</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default Sidebar;
