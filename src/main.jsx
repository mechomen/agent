import React from "react";
import ReactDOM from "react-dom/client";
import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";

import App from "./App";

import "./styles/app.css";
import "leaflet/dist/leaflet.css";

const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#4F8CFF",
    },
    secondary: {
      main: "#7C4DFF",
    },
  },
});

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>
  </React.StrictMode>
);