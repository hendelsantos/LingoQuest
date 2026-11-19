import type { Metadata } from "next";

import { StudentDashboard } from "@/components/student-dashboard";

export const metadata: Metadata = { title: "Seu espaço" };

export default function StudentDashboardPage() {
  return <StudentDashboard />;
}
