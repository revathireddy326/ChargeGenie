import React from "react";

export default function Login() {
  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white shadow-md rounded-lg border border-gray-200">
      <h2 className="text-2xl font-semibold text-center mb-6 text-blue-700">🔐 Login</h2>
      <form className="space-y-4">
        <input className="w-full border p-3 rounded focus:outline-blue-500" placeholder="Email" />
        <input type="password" className="w-full border p-3 rounded focus:outline-blue-500" placeholder="Password" />
        <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 font-medium">
          Login
        </button>
      </form>
    </div>
  );
}
