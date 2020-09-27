import React from "react";
import "./App.css";

const Footer = ({ url }) => {
  return (
    <div>
      <a href={url} className="gitHub-link">
        <p>
          <em>GitHub</em>
        </p>
      </a>
    </div>
  );
};

export default Footer;
