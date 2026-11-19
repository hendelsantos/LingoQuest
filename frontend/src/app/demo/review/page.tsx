import type { Metadata } from "next";

import { ReviewQueue } from "@/components/review-queue";

export const metadata: Metadata = { title: "Revisões — demonstração" };

export default function DemoReviewPage() {
  return <ReviewQueue basePath="/demo" />;
}
