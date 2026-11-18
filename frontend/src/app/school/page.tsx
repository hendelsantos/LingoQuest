import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = { title: "Gestão da escola" };

export default function SchoolPage() {
  return (
    <section className="role-hero">
      <span className="auth-eyebrow">Administração</span>
      <h1>Comece pelas pessoas.</h1>
      <p>Convide alunos e professores sem compartilhar senhas. Cada pessoa define o próprio acesso em um link de uso único.</p>
      <Link className="student-primary-button" href="/school/invitations">Criar convite →</Link>
    </section>
  );
}
