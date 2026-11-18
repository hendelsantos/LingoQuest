"use client";

import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { type FormEvent, useState } from "react";

import { AuthFormShell } from "@/components/auth-form-shell";
import { ApiError, destinationForRole, login } from "@/lib/auth";

export function LoginForm() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setBusy(true);
    const form = new FormData(event.currentTarget);
    try {
      const result = await login(String(form.get("email")), String(form.get("password")));
      const requested = searchParams.get("next");
      const destination = requested?.startsWith("/") && !requested.startsWith("//")
        ? requested
        : destinationForRole(result.user.role);
      router.replace(destination);
      router.refresh();
    } catch (caught) {
      setError(caught instanceof ApiError ? caught.message : "Não foi possível entrar agora.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <AuthFormShell
      eyebrow="Área segura"
      title="Que bom ter você de volta."
      description="Entre com o e-mail e a senha definidos no seu convite."
    >
      <form className="auth-form" onSubmit={handleSubmit}>
        <label htmlFor="email">E-mail</label>
        <input id="email" name="email" type="email" autoComplete="email" required />
        <label htmlFor="password">Senha</label>
        <input id="password" name="password" type="password" autoComplete="current-password" required />
        {error ? <p className="form-error" role="alert">{error}</p> : null}
        <button type="submit" disabled={busy}>{busy ? "Entrando…" : "Entrar"}</button>
      </form>
      <div className="auth-links">
        <Link href="/reset-password">Esqueci minha senha</Link>
        <Link href="/demo">Conhecer o ambiente demo</Link>
      </div>
    </AuthFormShell>
  );
}
