"use client";

import { type FormEvent, useState } from "react";

import { ApiError, apiPost, type UserRole } from "@/lib/auth";

type Invitation = {
  id: string;
  email: string;
  role: UserRole;
  expires_at: string;
};

export function InvitationForm() {
  const [invitation, setInvitation] = useState<Invitation | null>(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setInvitation(null);
    setBusy(true);
    const form = new FormData(event.currentTarget);
    try {
      const result = await apiPost<Invitation>("/api/v1/auth/staff/invitations/", {
        email: String(form.get("email")),
        role: String(form.get("role")),
      });
      setInvitation(result);
      event.currentTarget.reset();
    } catch (caught) {
      setError(caught instanceof ApiError ? caught.message : "Não foi possível enviar o convite.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <section className="management-card">
      <span className="auth-eyebrow">Identidade</span>
      <h1>Convidar uma pessoa</h1>
      <p>O destinatário receberá um link pessoal, válido por três dias e utilizável uma única vez.</p>
      <form className="auth-form" onSubmit={handleSubmit}>
        <label htmlFor="invite-email">E-mail</label>
        <input id="invite-email" name="email" type="email" required />
        <label htmlFor="invite-role">Papel na escola</label>
        <select id="invite-role" name="role" defaultValue="STUDENT">
          <option value="STUDENT">Aluno</option>
          <option value="TEACHER">Professor</option>
        </select>
        {error ? <p className="form-error" role="alert">{error}</p> : null}
        {invitation ? (
          <p className="form-success" role="status">
            Convite enviado para {invitation.email}. Expira em {new Intl.DateTimeFormat("pt-BR", { dateStyle: "short", timeStyle: "short" }).format(new Date(invitation.expires_at))}.
          </p>
        ) : null}
        <button type="submit" disabled={busy}>{busy ? "Enviando…" : "Enviar convite"}</button>
      </form>
    </section>
  );
}
