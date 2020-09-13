import React from "react";
import Sidebar from "./components/Sidebar";
import Navigation from "./components/Navigation";
//import Tweet from "./components/CreateTweet";
import FollowSidebar from "./components/FollowSidebar";
import { TweetContainer } from "./tweets";

function App() {
  return (
    <section className="feeds-page">
      <Navigation />
      <TweetContainer />
      <Sidebar />
    </section>
  );
}

export default App;
