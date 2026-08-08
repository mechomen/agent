import { useState } from "react";
import {
  Box,
  Typography,
  Grid,
  Card,
  CardContent,
} from "@mui/material";

import AddressForm from "../components/AddressForm";
import ResultCard from "../components/ResultCard";

function Home() {
  const [result, setResult] = useState(null);

  return (
    <Box
      sx={{
        minHeight: "100vh",
        background:
          "linear-gradient(135deg,#0f172a,#1e293b,#312e81)",
        p: 4,
      }}
    >
      {/* Header */}

      <Typography
        variant="h3"
        align="center"
        fontWeight="bold"
        color="white"
      >
        🚀 Address Intelligence AI
      </Typography>

      <Typography
        align="center"
        sx={{
          color: "#cbd5e1",
          mt: 1,
          mb: 5,
        }}
      >
        AI Powered Address Parsing & Verification System
      </Typography>

      {/* Dashboard Cards */}

      <Grid container spacing={3} mb={5}>
        <Grid item xs={12} md={4}>
          <Card
            sx={{
              bgcolor: "rgba(255,255,255,0.08)",
              backdropFilter: "blur(12px)",
              color: "white",
            }}
          >
            <CardContent>
              <Typography variant="h5">
                📍 Address Parser
              </Typography>

              <Typography mt={1}>
                Extracts landmark, city,
                district and state.
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card
            sx={{
              bgcolor: "rgba(255,255,255,0.08)",
              backdropFilter: "blur(12px)",
              color: "white",
            }}
          >
            <CardContent>
              <Typography variant="h5">
                🧠 AI Verification
              </Typography>

              <Typography mt={1}>
                Uses AI to verify addresses
                with confidence score.
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card
            sx={{
              bgcolor: "rgba(255,255,255,0.08)",
              backdropFilter: "blur(12px)",
              color: "white",
            }}
          >
            <CardContent>
              <Typography variant="h5">
                🌍 Geo Mapping
              </Typography>

              <Typography mt={1}>
                Shows verified location
                on an interactive map.
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Main Section */}

      <Grid container spacing={4}>
        <Grid item xs={12} md={5}>
          <AddressForm setResult={setResult} />
        </Grid>

        <Grid item xs={12} md={7}>
          <ResultCard result={result} />
        </Grid>
      </Grid>
    </Box>
  );
}

export default Home;