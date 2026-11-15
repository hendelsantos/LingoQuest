"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navigation = [
  { href: "/app", label: "Visão geral", icon: "⌂" },
  { href: "/app/learn", label: "Trilha de inglês", icon: "◇" },
  { href: "/app/notebook", label: "Meu caderno", icon: "▤", disabled: true },
  { href: "/app/live", label: "Aulas ao vivo", icon: "◉", disabled: true },
  { href: "/app/achievements", label: "Conquistas", icon: "✦", disabled: true },
  { href: "/app/billing", label: "Planos", icon: "▧", disabled: true },
];

export function StudentNav() {
  const pathname = usePathname();

  return (
    <nav className="student-nav" aria-label="Ambiente do aluno">
      {navigation.map((item) => {
        const active = item.href === "/app" ? pathname === item.href : pathname.startsWith(item.href);
        if (item.disabled) {
          return (
            <span className="student-nav-item is-disabled" key={item.href} title="Em breve">
              <i aria-hidden="true">{item.icon}</i>
              {item.label}
              <small>em breve</small>
            </span>
          );
        }
        return (
          <Link
            aria-current={active ? "page" : undefined}
            className={`student-nav-item${active ? " is-active" : ""}`}
            href={item.href}
            key={item.href}
          >
            <i aria-hidden="true">{item.icon}</i>
            {item.label}
          </Link>
        );
      })}
    </nav>
  );
}
