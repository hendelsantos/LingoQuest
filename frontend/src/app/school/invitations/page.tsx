import type { Metadata } from "next";

import { InvitationForm } from "@/components/invitation-form";

export const metadata: Metadata = { title: "Convites" };

export default function InvitationsPage() {
  return <InvitationForm />;
}
