import React from "react";

export default function Preferences() {
  return (
    <div id="prefs" className="max-w-lg mx-auto mt-12 p-6 bg-white shadow-md rounded-lg border border-gray-200">
      <h2 className="text-xl font-semibold text-purple-700 mb-4">⚙️ Charging Preferences</h2>
      <form className="space-y-4">
        <input className="w-full border p-3 rounded" placeholder="💰 Price Threshold (₹)" />
        <input className="w-full border p-3 rounded" placeholder="🕒 Preferred Time (e.g. Evening)" />
        <input className="w-full border p-3 rounded" placeholder="🔋 Current Battery %" />
        <button className="bg-purple-700 text-white px-4 py-2 rounded hover:bg-purple-800 w-full font-medium">
          Save Preferences
        </button>
      </form>
    </div>
  );
}
