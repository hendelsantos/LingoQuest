import type { Metadata } from "next";

import { LessonPlayer } from "@/components/lesson-player";

export const metadata: Metadata = { title: "Missão de inglês — demonstração" };

export default async function DemoLessonPage({ params, searchParams }: {
  params: Promise<{ lessonId: string }>;
  searchParams: Promise<{ course?: string }>;
}) {
  const { lessonId } = await params;
  const { course } = await searchParams;
  return <LessonPlayer slug={lessonId} courseSlug={course} basePath="/demo" />;
}
