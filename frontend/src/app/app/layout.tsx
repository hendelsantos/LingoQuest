import { Suspense, type ReactNode } from "react";

import { AppShell } from "@/components/app-shell";
import { ProtectedArea } from "@/components/protected-area";

export default function StudentLayout({ children }: { children: ReactNode }) {
  return (
    <Suspense fallback={<main className="auth-status">Verificando sua sessão…</main>}>
      <ProtectedArea allowedRoles={["STUDENT"]}>
        <AppShell mode="account">{children}</AppShell>
      </ProtectedArea>
    </Suspense>
  );
}
