"use client";

import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { type FormEvent, useState } from "react";

import { AuthFormShell } from "@/components/auth-form-shell";
import { ApiError, apiPost } from "@/lib/auth";

export function PasswordResetConfirmForm() {
  const params = useSearchParams();
  const uid = params.get("uid") ?? "";
  const token = params.get("token") ?? "";
  const [done, setDone] = useState(false);
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
      await apiPost("/api/v1/auth/password-reset/confirm/", { uid, token, password });
      setDone(true);
    } catch (caught) {
      setError(caught instanceof ApiError ? caught.message : "Não foi possível atualizar a senha.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthFormShell
      eyebrow="Nova senha"
      title="Escolha uma nova senha."
      description="Depois da alteração, o link não poderá ser usado novamente."
    >
      {!uid || !token ? <p className="form-error">O link está incompleto.</p> : done ? (
        <div className="form-success" role="status">Senha atualizada. <Link href="/login">Entrar agora</Link>.</div>
      ) : (
        <form className="auth-form" onSubmit={handleSubmit}>
          <label htmlFor="reset-password">Nova senha</label>
          <input id="reset-password" name="password" type="password" autoComplete="new-password" minLength={8} required />
          <label htmlFor="reset-password-confirm">Confirme a nova senha</label>
          <input id="reset-password-confirm" name="passwordConfirm" type="password" autoComplete="new-password" required />
          {error ? <p className="form-error" role="alert">{error}</p> : null}
          <button type="submit" disabled={busy}>{busy ? "Atualizando…" : "Atualizar senha"}</button>
        </form>
      )}
    </AuthFormShell>
  );
}
