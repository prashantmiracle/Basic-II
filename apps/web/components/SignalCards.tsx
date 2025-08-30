import React from 'react';

export const SignalCards: React.FC = () => (
  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div className="p-4 border rounded">
      <h3 className="font-semibold">Google Trends</h3>
      <p className="text-sm">Placeholder signal value</p>
    </div>
    <div className="p-4 border rounded">
      <h3 className="font-semibold">Social Metrics</h3>
      <p className="text-sm">Placeholder signal value</p>
    </div>
  </div>
);
