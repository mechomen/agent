from 
import { useState } from "react";
import {
  Paper,
  Typography,
  TextField,
  Button,
  CircularProgress,
  Alert,
} from "@mui/material";
import api from "../services/api";

function AddressForm({ setResult }) {
  const [address, setAddress] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const verifyAddress = async () => {
    if (!address.trim()) {
      setError("Please enter an address.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      // Call FastAPI Backend
      const res = await api.post("/verify", {
        address: address,
      });

      setResult(res.data);
    } catch (err) {
      console.error(err);

      // Demo Data (Used when backend isn't available)
      const demoData = {
        parsed_address: {
          landmark: "Ganesh Temple",
          locality: "Sai Nagar",
          city: "Vijayawada",
          district: "NTR",
          state: "Andhra Pradesh",
        },
        best_match: {
          name: "Ganesh Temple, LIC Colony",
          latitude: 16.5054215,
          longitude: 80.6513258,
        },
        confidence: 0.92,
        evidence: [
          "OpenStreetMap Verified",
          "India Post Verified",
          "Landmark Matched",
        ],
      };

      setResult(demoData);

      setError(
        "Backend not reachable. Showing demo response."
      );
    }

    setLoading(false);
  };

  return (
    <Paper
      elevation={10}
      sx={{
        p: 4,
        borderRadius: 5,
        background: "rgba(255,255,255,.08)",
        backdropFilter: "blur(18px)",
      }}
    >
      <Typography
        variant="h5"
        color="white"
        fontWeight="bold"
        mb={3}
      >
        📍 Address Verification
      </Typography>

      {error && (
        <Alert severity="warning" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}

      <TextField
        fullWidth
        multiline
        rows={7}
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        placeholder="Enter complete address..."
        variant="outlined"
        sx={{
          mb: 3,

          "& .MuiOutlinedInput-root": {
            color: "white",
            borderRadius: 3,
          },

          "& .MuiInputBase-input::placeholder": {
            color: "#d1d5db",
            opacity: 1,
          },

          "& fieldset": {
            borderColor: "#64748b",
          },
        }}
      />

      <Button
        fullWidth
        size="large"
        variant="contained"
        onClick={verifyAddress}
        disabled={loading}
        sx={{
          height: 55,
          borderRadius: 3,
          fontSize: 18,
          background:
            "linear-gradient(90deg,#2563eb,#7c3aed)",

          "&:hover": {
            background:
              "linear-gradient(90deg,#1d4ed8,#6d28d9)",
          },
        }}
      >
        {loading ? (
          <CircularProgress
            size={24}
            sx={{ color: "white" }}
          />
        ) : (
          "✨ Verify Address"
        )}
      </Button>
    </Paper>
  );
}

export default AddressForm;