import type { Metadata } from "next";

import { LearningPath } from "@/components/learning-path";

export const metadata: Metadata = { title: "Trilhas de inglês" };

export default function LearnPage() {
  return <LearningPath />;
}
