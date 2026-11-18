import type { Metadata } from "next";

import { LiveClassroomDemo } from "@/components/live-classroom-demo";

export const metadata: Metadata = { title: "Sala ao vivo — demonstração" };

export default function DemoLiveClassroomPage() {
  return <LiveClassroomDemo basePath="/demo" />;
}
