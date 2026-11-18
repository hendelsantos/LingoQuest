import Image from "next/image";
import Link from "next/link";
import type { ReactNode } from "react";

import { LogoutButton } from "@/components/logout-button";

export function RoleShell({
  area,
  home,
  links,
  children,
}: {
  area: string;
  home: string;
  links: { href: string; label: string }[];
  children: ReactNode;
}) {
  return (
    <div className="role-shell">
      <header className="role-header">
        <Link className="auth-brand" href={home}>
          <Image src="/brand/logo-mark.svg" alt="" width={38} height={38} />
          <span><strong>LingoQuest</strong><small>{area}</small></span>
        </Link>
        <nav aria-label={area}>
          {links.map((link) => <Link href={link.href} key={link.href}>{link.label}</Link>)}
          <LogoutButton />
        </nav>
      </header>
      <main className="role-main">{children}</main>
    </div>
  );
}
