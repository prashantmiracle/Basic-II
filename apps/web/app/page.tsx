import Link from 'next/link';
import { Button } from '@ui/index';

export default function Page() {
  return (
    <main className="p-8 text-center">
      <h1 className="text-4xl font-bold mb-4">Studio Rama / Aayushmaa Forecasts</h1>
      <p className="mb-6">AI-powered fashion demand and trend forecasting.</p>
      <Link href="/dashboard"><Button>Enter Dashboard</Button></Link>
    </main>
  );
}
