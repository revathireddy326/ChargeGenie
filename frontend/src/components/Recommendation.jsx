import React from "react";

export default function Recommendation({ result }) {
  if (!result) return null;

  return (
    <div id="reco" className="bg-white max-w-lg mx-auto p-6 rounded-lg shadow-md border border-gray-200 mt-12">
      <h3 className="text-xl font-semibold text-blue-700 mb-3">🔌 Recommended Station</h3>
      <div className="space-y-2 text-gray-800">
        <p><strong>Name:</strong> {result.station.name}</p>
        <p><strong>Distance:</strong> {result.station.distance} km</p>
        <p><strong>Availability:</strong> {result.station.availability}</p>
        <p><strong>Price:</strong> ₹{result.station.price}</p>
        <p className="mt-3 italic text-gray-600 border-t pt-2">{result.explanation}</p>
      </div>
    </div>
  );
}
