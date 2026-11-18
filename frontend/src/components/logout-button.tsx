"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { apiPost } from "@/lib/auth";

export function LogoutButton() {
  const router = useRouter();
  const [busy, setBusy] = useState(false);

  async function handleLogout() {
    setBusy(true);
    try {
      await apiPost("/api/v1/auth/logout/");
      router.replace("/login");
      router.refresh();
    } finally {
      setBusy(false);
    }
  }

  return (
    <button className="logout-button" type="button" disabled={busy} onClick={handleLogout}>
      {busy ? "Saindo…" : "Sair"}
    </button>
  );
}
