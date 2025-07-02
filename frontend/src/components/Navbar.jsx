import React from "react";

export default function Navbar() {
  return (
    <nav className="bg-gradient-to-r from-blue-700 to-blue-500 text-white p-4 shadow-lg">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold tracking-wide">⚡ ChargeGenie</h1>
        <div className="space-x-6 text-md">
          <a href="#" className="hover:underline">Home</a>
          <a href="#prefs" className="hover:underline">Preferences</a>
          <a href="#reco" className="hover:underline">Recommendations</a>
        </div>
      </div>
    </nav>
  );
}
