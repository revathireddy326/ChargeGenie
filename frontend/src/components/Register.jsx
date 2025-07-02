import React from "react";

export default function Register() {
  return (
    <div className="max-w-md mx-auto mt-10 p-6 bg-white shadow-md rounded-lg border border-gray-200">
      <h2 className="text-2xl font-semibold text-center mb-6 text-green-700">📝 Register</h2>
      <form className="space-y-4">
        <input className="w-full border p-3 rounded focus:outline-green-500" placeholder="Email" />
        <input type="password" className="w-full border p-3 rounded focus:outline-green-500" placeholder="Password" />
        <button type="submit" className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700 font-medium">
          Register
        </button>
      </form>
    </div>
  );
}
