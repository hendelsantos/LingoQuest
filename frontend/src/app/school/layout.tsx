import { Suspense, type ReactNode } from "react";

import { ProtectedArea } from "@/components/protected-area";
import { RoleShell } from "@/components/role-shell";

export default function SchoolLayout({ children }: { children: ReactNode }) {
  return (
    <Suspense fallback={<main className="auth-status">Verificando sua sessão…</main>}>
      <ProtectedArea allowedRoles={["ADMIN"]}>
        <RoleShell
          area="Gestão da escola"
          home="/school"
          links={[
            { href: "/school", label: "Visão geral" },
            { href: "/school/invitations", label: "Convites" },
          ]}
        >
          {children}
        </RoleShell>
      </ProtectedArea>
    </Suspense>
  );
}
