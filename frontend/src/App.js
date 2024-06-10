import React from "react";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Header from "./Header"; // Ensure paths are correct
import Tablee from "./Table"; // Ensure paths are correct

function App() {
  return (
    <div className="App">
      <Container maxWidth="lg">
        <Grid container direction="column" spacing={2}>
          <Grid item xs={12}>
            <Header />
          </Grid>
          <Grid item xs={12}>
            <Tablee />
          </Grid>
        </Grid>
      </Container>
    </div>
  );
}

export default App;
