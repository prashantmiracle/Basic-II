"use client";
import { useState } from 'react';
import { Button } from '@ui/index';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  return (
    <form className="max-w-sm mx-auto p-4 space-y-2">
      <h2 className="text-xl font-semibold">Login</h2>
      <input className="border p-2 w-full" placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} />
      <input className="border p-2 w-full" placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} />
      <Button type="submit">Login</Button>
    </form>
  );
}
