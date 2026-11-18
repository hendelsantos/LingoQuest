import Image from "next/image";
import Link from "next/link";
import type { ReactNode } from "react";

export function AuthFormShell({
  eyebrow,
  title,
  description,
  children,
}: {
  eyebrow: string;
  title: string;
  description: string;
  children: ReactNode;
}) {
  return (
    <main className="auth-page">
      <section className="auth-card">
        <Link className="auth-brand" href="/" aria-label="LingoQuest — início">
          <Image src="/brand/logo-mark.svg" alt="" width={44} height={44} priority />
          <span><strong>LingoQuest</strong><small>English Academy</small></span>
        </Link>
        <span className="auth-eyebrow">{eyebrow}</span>
        <h1>{title}</h1>
        <p>{description}</p>
        {children}
      </section>
    </main>
  );
}
