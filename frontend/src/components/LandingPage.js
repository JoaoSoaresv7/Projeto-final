import React from "react";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";
import Footer from "./Footer";

const LandingPage = () => {
  return (
    <div className="App">
      <div id="home"> {/*Ancoragem*/}
        <Home />
      </div>
      <div id="sobre"> {/*Ancoragem*/}
        <About />
      </div>
      <div id="contato"> {/*Ancoragem*/}
        <Contact />
      </div>
      <Footer />
    </div>
  );
};

export default LandingPage;
