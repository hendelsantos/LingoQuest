import type { Metadata } from "next";
import { Suspense } from "react";

import { InvitationAcceptForm } from "@/components/invitation-accept-form";

export const metadata: Metadata = { title: "Aceitar convite" };

export default function AcceptInvitationPage() {
  return <Suspense fallback={<main className="auth-status">Carregando convite…</main>}><InvitationAcceptForm /></Suspense>;
}
