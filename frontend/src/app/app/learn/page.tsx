import type { Metadata } from "next";

import { LearningPath } from "@/components/learning-path";

export const metadata: Metadata = { title: "Trilha A1" };

export default function LearnPage() {
  return <LearningPath />;
}
