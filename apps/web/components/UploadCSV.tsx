"use client";
import React from 'react';

export const UploadCSV: React.FC = () => {
  return (
    <form className="border p-4 rounded">
      <input type="file" accept=".csv" className="mb-2" />
      <button type="submit" className="px-4 py-2 bg-green-600 text-white rounded">Upload Sales</button>
    </form>
  );
};
