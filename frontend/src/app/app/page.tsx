import type { Metadata } from "next";

import { DashboardDemo } from "@/components/dashboard-demo";

export const metadata: Metadata = { title: "Seu espaço" };

export default function StudentDashboardPage() {
  return <DashboardDemo />;
}
