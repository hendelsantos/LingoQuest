import type { Metadata } from "next";
import { Suspense } from "react";

import { PasswordResetConfirmForm } from "@/components/password-reset-confirm-form";

export const metadata: Metadata = { title: "Criar nova senha" };

export default function ResetPasswordConfirmPage() {
  return <Suspense fallback={<main className="auth-status">Validando link…</main>}><PasswordResetConfirmForm /></Suspense>;
}
