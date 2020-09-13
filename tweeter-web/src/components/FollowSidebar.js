import React from "react";
import User3 from "../images/user3.jpg";
import User4 from "../images/user4.jpg";
import User5 from "../images/user5.jpg";

function FollowSidebar(props) {
  return (
    <div className="follow dark-mode-1">
      <h3 className="follow-heading light-text border">Who to follow</h3>
      <div className="follow-user border">
        <div className="follow-user-img">
          <img src={User3} alt="User 3" />
        </div>
        <div className="follow-user-info light-text">
          <h4>Ann Smith</h4>
          <p>@annsmith</p>
        </div>
        <button type="button" className="follow-btn dark-mode-2">
          Follow
        </button>
      </div>
      <div className="follow-user border">
        <div className="follow-user-img">
          <img src={User4} alt="User 4" />
        </div>
        <div className="follow-user-info light-text">
          <h4>Nick Doe</h4>
          <p>@nickdoe</p>
        </div>
        <button type="button" className="follow-btn dark-mode-2">
          Follow
        </button>
      </div>
      <div className="follow-user border">
        <div className="follow-user-img">
          <img src={User5} alt="User 5" />
        </div>
        <div className="follow-user-info light-text">
          <h4>James Black</h4>
          <p>@jamesblack</p>
        </div>
        <button type="button" className="follow-btn dark-mode-2">
          Follow
        </button>
      </div>
      <div className="follow-link">
        <a href="#">Show more</a>
      </div>
      <footer className="follow-footer dark-mode-2">
        <ul>
          <li>
            <a href="#">Terms</a>
          </li>
          <li>
            <a href="#">Privacy policy</a>
          </li>
          <li>
            <a href="#">Cookies</a>
          </li>
          <li>
            <a href="#">About</a>
          </li>
          <li>
            <a href="#">More</a>
          </li>
        </ul>
      </footer>
    </div>
  );
}

export default FollowSidebar;
