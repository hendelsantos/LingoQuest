import type { Metadata } from "next";

import { PasswordResetForm } from "@/components/password-reset-form";

export const metadata: Metadata = { title: "Redefinir senha" };

export default function ResetPasswordPage() {
  return <PasswordResetForm />;
}
