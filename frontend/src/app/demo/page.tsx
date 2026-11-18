import type { Metadata } from "next";

import { DashboardDemo } from "@/components/dashboard-demo";

export const metadata: Metadata = { title: "Demonstração" };

export default function DemoPage() {
  return <DashboardDemo basePath="/demo" />;
}
