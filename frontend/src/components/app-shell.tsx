import Image from "next/image";
import Link from "next/link";
import { Suspense, type ReactNode } from "react";

import { StudentNav } from "@/components/student-nav";

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="student-shell">
      <aside className="student-sidebar">
        <Link className="student-brand" href="/" aria-label="Voltar para a página inicial da LingoQuest">
          <Image src="/brand/logo-mark.svg" alt="" width={42} height={42} priority />
          <span>
            <strong>LingoQuest</strong>
            <small>English Academy</small>
          </span>
        </Link>

        <p className="student-nav-label">Meu aprendizado</p>
        <Suspense fallback={<div className="student-nav-skeleton" />}>
          <StudentNav />
        </Suspense>

        <div className="student-sidebar-footer">
          <Link href="/" className="sidebar-school-link">Conhecer a escola ↗</Link>
          <p>Ambiente de demonstração</p>
          <div className="demo-user"><span>A</span> Aluno visitante</div>
          <small>Preview público · progresso neste navegador</small>
        </div>
      </aside>

      <div className="student-workspace">
        <header className="student-topbar">
          <Link className="mobile-menu-button" href="/" aria-label="Voltar para a página inicial">LQ</Link>
          <div>
            <span>LingoQuest</span>
            <strong>Ambiente de aprendizado</strong>
          </div>
          <span className="demo-pill">Modo demonstração</span>
        </header>
        <main className="student-main">{children}</main>
      </div>
    </div>
  );
}
