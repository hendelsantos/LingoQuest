import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { Suspense } from "react";

import { AssessmentPlayer } from "@/components/assessment-player";

export const metadata: Metadata = { title: "Avaliação A1 — demonstração" };

export default function DemoAssessmentPage({ params }: { params: Promise<{ moment: string }> }) {
  return <Suspense fallback={<div className="lesson-skeleton">Preparando avaliação…</div>}><AssessmentContent params={params} /></Suspense>;
}

async function AssessmentContent({ params }: { params: Promise<{ moment: string }> }) {
  const { moment } = await params;
  if (moment !== "initial" && moment !== "final") notFound();
  return <AssessmentPlayer moment={moment} basePath="/demo" />;
}
