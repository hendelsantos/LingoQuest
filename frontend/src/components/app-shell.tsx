import Image from "next/image";
import Link from "next/link";
import { Suspense, type ReactNode } from "react";

import { StudentNav } from "@/components/student-nav";
import { LogoutButton } from "@/components/logout-button";

export function AppShell({
  children,
  mode = "demo",
  basePath = "/app",
}: {
  children: ReactNode;
  mode?: "demo" | "account";
  basePath?: string;
}) {
  const isDemo = mode === "demo";
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
          <StudentNav basePath={basePath} />
        </Suspense>

        <div className="student-sidebar-footer">
          <Link href="/" className="sidebar-school-link">Conhecer a escola ↗</Link>
          <p>{isDemo ? "Ambiente de demonstração" : "Conta do aluno"}</p>
          <div className="demo-user"><span>A</span> {isDemo ? "Aluno visitante" : "Área pessoal"}</div>
          {isDemo ? <small>Preview público · progresso neste navegador</small> : <LogoutButton />}
        </div>
      </aside>

      <div className="student-workspace">
        <header className="student-topbar">
          <Link className="mobile-menu-button" href="/" aria-label="Voltar para a página inicial">LQ</Link>
          <div>
            <span>LingoQuest</span>
            <strong>Ambiente de aprendizado</strong>
          </div>
          <span className="demo-pill">{isDemo ? "Modo demonstração" : "Sessão segura"}</span>
        </header>
        <main className="student-main">{children}</main>
      </div>
    </div>
  );
}
