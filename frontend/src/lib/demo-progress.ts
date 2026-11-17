export const PROGRESS_STORAGE_KEY = "lingoquest.demo.progress.v1";
export const PROGRESS_EVENT = "lingoquest-progress";

export type CompletedLesson = {
  score: number;
  completedAt: string;
  xpAwarded: number;
};

export type DemoProgress = {
  completed: Record<string, CompletedLesson>;
};

export const emptyProgress: DemoProgress = { completed: {} };

function normalizeRecord(record: Partial<CompletedLesson>): CompletedLesson {
  return {
    score: typeof record.score === "number" ? record.score : 0,
    completedAt: typeof record.completedAt === "string" ? record.completedAt : new Date().toISOString(),
    // Registros antigos não tinham XP explícito: assumem o padrão histórico.
    xpAwarded: typeof record.xpAwarded === "number" ? record.xpAwarded : 60,
  };
}

export function readProgress(): DemoProgress {
  if (typeof window === "undefined") return emptyProgress;
  try {
    const stored = window.localStorage.getItem(PROGRESS_STORAGE_KEY);
    if (!stored) return emptyProgress;
    const parsed = JSON.parse(stored) as DemoProgress;
    if (!parsed || typeof parsed.completed !== "object" || parsed.completed === null) {
      return emptyProgress;
    }
    const completed: Record<string, CompletedLesson> = {};
    for (const [slug, record] of Object.entries(parsed.completed)) {
      if (record && typeof record === "object") completed[slug] = normalizeRecord(record);
    }
    return { completed };
  } catch {
    return emptyProgress;
  }
}

/**
 * Registra a conclusão de uma missão. O XP informado é somado ao já acumulado
 * (quem chama decide o valor: 0 para repetições, 15 para revisões, o total na
 * primeira conclusão). Mantém a maior pontuação e a primeira data de conclusão.
 */
export function completeLesson(slug: string, score: number, xpAwarded: number): DemoProgress {
  const current = readProgress();
  const previous = current.completed[slug];
  const next: DemoProgress = {
    completed: {
      ...current.completed,
      [slug]: {
        score: Math.max(score, previous?.score ?? 0),
        completedAt: previous?.completedAt ?? new Date().toISOString(),
        xpAwarded: (previous?.xpAwarded ?? 0) + Math.max(0, xpAwarded),
      },
    },
  };
  window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event(PROGRESS_EVENT));
  return next;
}

export function progressStats(progress: DemoProgress, lessonCount = 8) {
  const completedCount = Object.keys(progress.completed).length;
  const xp = Object.values(progress.completed).reduce((total, lesson) => total + lesson.xpAwarded, 0);
  return {
    completedCount,
    xp,
    percent: lessonCount > 0 ? Math.round((completedCount / lessonCount) * 100) : 0,
  };
}

export function progressForSlugs(progress: DemoProgress, slugs: Iterable<string>): DemoProgress {
  const allowed = new Set(slugs);
  return {
    completed: Object.fromEntries(
      Object.entries(progress.completed).filter(([slug]) => allowed.has(slug)),
    ),
  };
}
