"use client";

import { usePathname, useRouter } from "next/navigation";
import { type ReactNode, useEffect, useState } from "react";

import {
  ApiError,
  destinationForRole,
  getCurrentUser,
  type AuthUser,
  type UserRole,
} from "@/lib/auth";

export function ProtectedArea({
  allowedRoles,
  children,
}: {
  allowedRoles: UserRole[];
  children: ReactNode;
}) {
  const pathname = usePathname();
  const router = useRouter();
  const [user, setUser] = useState<AuthUser | null>(null);
  const [error, setError] = useState(false);

  useEffect(() => {
    let active = true;
    getCurrentUser()
      .then((currentUser) => {
        if (!active) return;
        if (!allowedRoles.includes(currentUser.role)) {
          router.replace(destinationForRole(currentUser.role));
          return;
        }
        setUser(currentUser);
      })
      .catch((caught: unknown) => {
        if (!active) return;
        if (caught instanceof ApiError && (caught.status === 401 || caught.status === 403)) {
          router.replace(`/login?next=${encodeURIComponent(pathname)}`);
          return;
        }
        setError(true);
      });
    return () => {
      active = false;
    };
  }, [allowedRoles, pathname, router]);

  if (error) {
    return (
      <main className="auth-status" role="alert">
        <p>Não foi possível verificar sua sessão.</p>
        <button type="button" onClick={() => window.location.reload()}>Tentar novamente</button>
      </main>
    );
  }

  if (!user) {
    return <main className="auth-status"><p>Verificando sua sessão…</p></main>;
  }

  return children;
}
