import type { Metadata } from "next";

export const metadata: Metadata = { title: "Área do professor" };

export default function TeacherPage() {
  return (
    <section className="role-hero">
      <span className="auth-eyebrow">Professor</span>
      <h1>Seu espaço de acompanhamento.</h1>
      <p>A identidade já está protegida. Agenda, vínculos e evidências dos alunos entram na próxima fase acadêmica.</p>
    </section>
  );
}
