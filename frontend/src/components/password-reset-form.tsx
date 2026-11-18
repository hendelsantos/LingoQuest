"use client";

import Link from "next/link";
import { type FormEvent, useState } from "react";

import { AuthFormShell } from "@/components/auth-form-shell";
import { ApiError, apiPost } from "@/lib/auth";

export function PasswordResetForm() {
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setBusy(true);
    const form = new FormData(event.currentTarget);
    try {
      const result = await apiPost<{ detail: string }>("/api/v1/auth/password-reset/", {
        email: String(form.get("email")),
      });
      setMessage(result.detail);
    } catch (caught) {
      setError(caught instanceof ApiError ? caught.message : "Não foi possível enviar o pedido.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthFormShell
      eyebrow="Recuperar acesso"
      title="Redefina sua senha."
      description="Informe seu e-mail e enviaremos um link de uso único, caso exista uma conta ativa."
    >
      {message ? <p className="form-success" role="status">{message}</p> : (
        <form className="auth-form" onSubmit={handleSubmit}>
          <label htmlFor="reset-email">E-mail</label>
          <input id="reset-email" name="email" type="email" autoComplete="email" required />
          {error ? <p className="form-error" role="alert">{error}</p> : null}
          <button type="submit" disabled={busy}>{busy ? "Enviando…" : "Enviar instruções"}</button>
        </form>
      )}
      <div className="auth-links"><Link href="/login">Voltar para o login</Link></div>
    </AuthFormShell>
  );
}
