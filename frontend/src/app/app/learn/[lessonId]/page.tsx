import type { Metadata } from "next";

import { LessonPlayer } from "@/components/lesson-player";

export const metadata: Metadata = { title: "Missão A1" };

export default async function LessonPage({
  params,
}: {
  params: Promise<{ lessonId: string }>;
}) {
  const { lessonId } = await params;
  return <LessonPlayer slug={lessonId} />;
}
