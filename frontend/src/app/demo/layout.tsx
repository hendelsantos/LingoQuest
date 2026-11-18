import type { ReactNode } from "react";

import { AppShell } from "@/components/app-shell";

export default function DemoLayout({ children }: { children: ReactNode }) {
  return <AppShell basePath="/demo">{children}</AppShell>;
}
