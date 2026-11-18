import type { Metadata } from "next";

import { LiveClassesOverview } from "@/components/live-classes-overview";

export const metadata: Metadata = { title: "Aulas ao vivo — demonstração" };

export default function DemoLivePage() {
  return <LiveClassesOverview basePath="/demo" />;
}
