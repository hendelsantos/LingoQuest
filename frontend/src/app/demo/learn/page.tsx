import type { Metadata } from "next";

import { LearningPath } from "@/components/learning-path";

export const metadata: Metadata = { title: "Trilhas de inglês — demonstração" };

export default function DemoLearnPage() {
  return <LearningPath basePath="/demo" />;
}
