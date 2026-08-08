import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";

import markerIcon2x from "leaflet/dist/images/marker-icon-2x.png";
import markerIcon from "leaflet/dist/images/marker-icon.png";
import markerShadow from "leaflet/dist/images/marker-shadow.png";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

function MapView({ latitude, longitude }) {
  const lat = Number(latitude);
  const lng = Number(longitude);

  return (
    <div
      style={{
        height: "350px",
        width: "100%",
        borderRadius: "16px",
        overflow: "hidden",
        marginTop: "20px",
      }}
    >
      <MapContainer
        center={[lat, lng]}
        zoom={15}
        scrollWheelZoom={true}
        style={{
          height: "100%",
          width: "100%",
        }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap Contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={[lat, lng]}>
          <Popup>
            <b>Verified Location</b>
            <br />
            Latitude: {lat}
            <br />
            Longitude: {lng}
          </Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default MapView;