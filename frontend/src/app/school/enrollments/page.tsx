import type { Metadata } from "next";

import { EnrollmentManager } from "@/components/enrollment-manager";

export const metadata: Metadata = { title: "Matrículas" };

export default function EnrollmentsPage() {
  return <EnrollmentManager />;
}
