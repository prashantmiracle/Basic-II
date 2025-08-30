import React from 'react';
import { Button } from '@ui/index';

export const Pricing: React.FC = () => (
  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
    {['Free','Pro','Enterprise'].map(tier => (
      <div key={tier} className="border p-4 rounded text-center">
        <h3 className="font-bold text-xl mb-2">{tier}</h3>
        <p className="mb-4">Plan details</p>
        <Button>Choose</Button>
      </div>
    ))}
  </div>
);
