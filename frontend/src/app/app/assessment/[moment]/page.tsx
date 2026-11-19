import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";

export const metadata: Metadata = { title: "Avaliação A1" };

export default function AssessmentPage({ params }: { params: Promise<{ moment: string }> }) {
  return <AssessmentContent params={params} />;
}

async function AssessmentContent({ params }: { params: Promise<{ moment: string }> }) {
  const { moment } = await params;
  if (moment !== "initial" && moment !== "final") notFound();
  return <section className="role-hero">
    <span className="auth-eyebrow">Avaliação da conta</span>
    <h1>Resultados persistidos chegam na Fase 2B.</h1>
    <p>Para não confundir dados deste navegador com seu histórico real, a avaliação autenticada será liberada junto com tentativas e progresso persistidos.</p>
    <Link className="student-primary-button" href={`/demo/assessment/${moment}`}>Abrir demonstração →</Link>
  </section>;
}
