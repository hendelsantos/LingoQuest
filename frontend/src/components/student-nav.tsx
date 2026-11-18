"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function StudentNav({ basePath = "/app" }: { basePath?: string }) {
  const pathname = usePathname();
  const navigation = [
    { href: basePath, label: "Visão geral", icon: "⌂" },
    { href: `${basePath}/learn`, label: "Trilha de inglês", icon: "◇" },
    { href: `${basePath}/notebook`, label: "Meu caderno", icon: "▤", disabled: true },
    { href: `${basePath}/live`, label: "Aulas ao vivo", icon: "◉" },
    { href: `${basePath}/achievements`, label: "Conquistas", icon: "✦", disabled: true },
    { href: `${basePath}/billing`, label: "Planos", icon: "▧", disabled: true },
  ];

  return (
    <nav className="student-nav" aria-label="Ambiente do aluno">
      {navigation.map((item) => {
        const active = item.href === basePath ? pathname === item.href : pathname.startsWith(item.href);
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
