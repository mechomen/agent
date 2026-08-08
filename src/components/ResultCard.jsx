import {
  Paper,
  Typography,
  Grid,
  Chip,
  LinearProgress,
  Divider,
  Box,
} from "@mui/material";
import RoomIcon from "@mui/icons-material/Room";
import VerifiedIcon from "@mui/icons-material/Verified";
import PublicIcon from "@mui/icons-material/Public";
import MapView from "./MapView";

function ResultCard({ result }) {
  if (!result) {
    return (
      <Paper
        elevation={10}
        sx={{
          p: 4,
          borderRadius: 5,
          background: "rgba(255,255,255,.08)",
          backdropFilter: "blur(18px)",
          minHeight: 600,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Typography
          color="#cbd5e1"
          fontSize={20}
          align="center"
        >
          🚀 Enter an address and click
          <br />
          <b>Verify Address</b>
          <br />
          to see AI analysis.
        </Typography>
      </Paper>
    );
  }

  return (
    <Paper
      elevation={10}
      sx={{
        p: 4,
        borderRadius: 5,
        background: "rgba(255,255,255,.08)",
        backdropFilter: "blur(18px)",
        color: "white",
      }}
    >
      <Typography
        variant="h5"
        fontWeight="bold"
        mb={3}
      >
        🤖 AI Verification Result
      </Typography>

      <Typography fontWeight="bold">
        Confidence Score
      </Typography>

      <LinearProgress
        variant="determinate"
        value={result.confidence * 100}
        sx={{
          height: 10,
          borderRadius: 5,
          mt: 1,
          mb: 2,
        }}
      />

      <Typography mb={4}>
        {(result.confidence * 100).toFixed(0)}%
      </Typography>

      <Divider sx={{ mb: 3 }} />

      <Typography
        variant="h6"
        gutterBottom
      >
        📍 Parsed Address
      </Typography>

      <Grid container spacing={2}>

        <Grid item xs={6}>
          <Typography>
            <b>Landmark</b>
          </Typography>

          <Typography color="#cbd5e1">
            {result.parsed_address.landmark}
          </Typography>
        </Grid>

        <Grid item xs={6}>
          <Typography>
            <b>Locality</b>
          </Typography>

          <Typography color="#cbd5e1">
            {result.parsed_address.locality}
          </Typography>
        </Grid>

        <Grid item xs={6}>
          <Typography>
            <b>City</b>
          </Typography>

          <Typography color="#cbd5e1">
            {result.parsed_address.city}
          </Typography>
        </Grid>

        <Grid item xs={6}>
          <Typography>
            <b>District</b>
          </Typography>

          <Typography color="#cbd5e1">
            {result.parsed_address.district}
          </Typography>
        </Grid>

        <Grid item xs={12}>
          <Typography>
            <b>State</b>
          </Typography>

          <Typography color="#cbd5e1">
            {result.parsed_address.state}
          </Typography>
        </Grid>

      </Grid>

      <Divider sx={{ my: 4 }} />

      <Typography
        variant="h6"
        gutterBottom
      >
        📌 Best Match
      </Typography>

      <Typography>
        <RoomIcon
          sx={{
            mr: 1,
            color: "#38bdf8",
          }}
        />
        {result.best_match.name}
      </Typography>

      <Typography mt={1}>
        <PublicIcon
          sx={{
            mr: 1,
            color: "#38bdf8",
          }}
        />
        {result.best_match.latitude},
        {" "}
        {result.best_match.longitude}
      </Typography>

      <Divider sx={{ my: 4 }} />

      <Typography
        variant="h6"
        gutterBottom
      >
        ✔ Evidence
      </Typography>

      <Box>
        {result.evidence.map((item, index) => (
          <Chip
            key={index}
            icon={<VerifiedIcon />}
            label={item}
            color="success"
            sx={{
              mr: 1,
              mb: 1,
            }}
          />
        ))}
      </Box>

      <Divider sx={{ my: 4 }} />

      <Typography
        variant="h6"
        gutterBottom
      >
        🗺 Verified Location
      </Typography>

      <MapView
        latitude={result.best_match.latitude}
        longitude={result.best_match.longitude}
      />
    </Paper>
  );
}

export default ResultCard;