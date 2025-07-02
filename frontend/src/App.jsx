import React, { useState } from "react";
import Navbar from "./components/Navbar";
import Login from "./components/Login";
import Register from "./components/Register";
import Preferences from "./components/Preferences";
import Recommendation from "./components/Recommendation";

// In a real app, useContext or Redux would manage auth state
export default function App() {
  const [showLogin, setShowLogin] = useState(true);
  const [recommendation, setRecommendation] = useState(null);

  // Mock handler to simulate recommendation fetch
  const getRecommendation = () => {
    // Simulate API response
    const fakeResponse = {
      station: {
        name: "EV Point - Sector 12",
        distance: 2.5,
        availability: "🟢 Available",
        price: 12
      },
      explanation: "This station is close, affordable, and available based on your preferences."
    };
    setRecommendation(fakeResponse);
  };

  return (
    <div>
      <Navbar />
      <div className="container mx-auto px-4 py-6">
        <div className="flex justify-center gap-4 mb-6">
          <button onClick={() => setShowLogin(true)} className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
            Login
          </button>
          <button onClick={() => setShowLogin(false)} className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700">
            Register
          </button>
        </div>

        {showLogin ? <Login /> : <Register />}
        <Preferences />
        <div className="text-center mt-6">
          <button onClick={getRecommendation} className="bg-purple-700 text-white px-6 py-2 rounded hover:bg-purple-800">
            Get Recommendation
          </button>
        </div>
        <Recommendation result={recommendation} />
      </div>
    </div>
  );
}