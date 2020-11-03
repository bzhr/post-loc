import * as React from "react";
import GetApiData from "../components/GetApiData";

const Home = () => {
  return (
    <div className="App">
      <header className="App-header">
        Hey, enter a search term in the box, to search stores by city name or
        postcode.
      </header>
      <GetApiData></GetApiData>
    </div>
  );
};

export default Home;
