import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = { title: "Revisões" };

export default function ReviewPage() {
  return <section className="role-hero">
    <span className="auth-eyebrow">Revisões da conta</span>
    <h1>Em preparação para a Fase 2B.</h1>
    <p>A fila de revisão será liberada quando tentativas e progresso passarem a ser persistidos na conta. O modo demonstrativo continua disponível sem misturar dados locais com seu perfil.</p>
    <Link className="student-primary-button" href="/demo/review">Abrir demonstração →</Link>
  </section>;
}
