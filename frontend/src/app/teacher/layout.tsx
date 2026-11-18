import { Suspense, type ReactNode } from "react";

import { ProtectedArea } from "@/components/protected-area";
import { RoleShell } from "@/components/role-shell";

export default function TeacherLayout({ children }: { children: ReactNode }) {
  return (
    <Suspense fallback={<main className="auth-status">Verificando sua sessão…</main>}>
      <ProtectedArea allowedRoles={["TEACHER"]}>
        <RoleShell area="Área do professor" home="/teacher" links={[{ href: "/teacher", label: "Visão geral" }]}>
          {children}
        </RoleShell>
      </ProtectedArea>
    </Suspense>
  );
}
