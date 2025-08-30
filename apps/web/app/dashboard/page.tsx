import { UploadCSV } from '../../components/UploadCSV';
import { SignalCards } from '../../components/SignalCards';

export default function Dashboard() {
  return (
    <div className="p-4 space-y-4">
      <h2 className="text-2xl font-semibold">Dashboard</h2>
      <SignalCards />
      <UploadCSV />
    </div>
  );
}
