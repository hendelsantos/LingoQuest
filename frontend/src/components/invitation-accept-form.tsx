"use client";

import { useRouter, useSearchParams } from "next/navigation";
import { type FormEvent, useState } from "react";

import { AuthFormShell } from "@/components/auth-form-shell";
import { ApiError, apiPost, destinationForRole, type AuthUser } from "@/lib/auth";

export function InvitationAcceptForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const token = searchParams.get("token") ?? "";
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setBusy(true);
    const form = new FormData(event.currentTarget);
    const password = String(form.get("password"));
    if (password !== String(form.get("passwordConfirm"))) {
      setError("As senhas precisam ser iguais.");
      setBusy(false);
      return;
    }
    try {
      const result = await apiPost<{ user: AuthUser }>("/api/v1/auth/invitations/accept/", {
        token,
        name: String(form.get("name")),
        password,
      });
      router.replace(destinationForRole(result.user.role));
      router.refresh();
    } catch (caught) {
      setError(caught instanceof ApiError ? caught.message : "Não foi possível aceitar o convite.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthFormShell
      eyebrow="Seu convite"
      title="Crie seu acesso."
      description="Escolha uma senha pessoal. O link de convite funciona somente uma vez."
    >
      {!token ? <p className="form-error" role="alert">O link de convite está incompleto.</p> : (
        <form className="auth-form" onSubmit={handleSubmit}>
          <label htmlFor="name">Como devemos chamar você?</label>
          <input id="name" name="name" autoComplete="name" maxLength={150} required />
          <label htmlFor="new-password">Senha</label>
          <input id="new-password" name="password" type="password" autoComplete="new-password" minLength={8} required />
          <small>Use uma senha longa e diferente das suas informações pessoais.</small>
          <label htmlFor="password-confirm">Confirme a senha</label>
          <input id="password-confirm" name="passwordConfirm" type="password" autoComplete="new-password" required />
          {error ? <p className="form-error" role="alert">{error}</p> : null}
          <button type="submit" disabled={busy}>{busy ? "Criando acesso…" : "Criar meu acesso"}</button>
        </form>
      )}
    </AuthFormShell>
  );
}
