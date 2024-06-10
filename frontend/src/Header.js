import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import logo from "./logoweb.svg";
const Header = () => {
  return (
    <AppBar
      position="static"
      style={{
        backgroundColor: "rgba(var(--bs-white-rgb),var(--bs-bg-opacity))",
        boxShadow: "none",
      }}
    >
      <Toolbar style={{ paddingLeft: "0px" }}>
        <img
          src={logo}
          alt="logo"
          style={{ width: "150px", marginRight: "20px" }}
        />
      </Toolbar>
    </AppBar>
  );
};

export default Header;
