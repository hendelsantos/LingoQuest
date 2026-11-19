export const PROGRESS_STORAGE_KEY = "lingoquest.demo.progress.v1";
export const PROGRESS_EVENT = "lingoquest-progress";

export type CompletedLesson = {
  score: number;
  completedAt: string;
  xpAwarded: number;
  reviewedIntervals: number[];
  lastReviewedAt: string | null;
};

export type ErrorCategory =
  | "GRAMMAR"
  | "VOCABULARY"
  | "WORD_ORDER"
  | "LISTENING"
  | "SPELLING"
  | "COMPREHENSION";

export type ErrorSummary = {
  count: number;
  lastAt: string;
  lessons: string[];
};

export type AssessmentMoment = "initial" | "final";

export type AssessmentResult = {
  score: number;
  correctCount: number;
  totalQuestions: number;
  completedAt: string;
  confidence: "practice" | "supported" | "independent";
  writingSample: string;
};

export type DemoProgress = {
  completed: Record<string, CompletedLesson>;
  errors: Partial<Record<ErrorCategory, ErrorSummary>>;
  assessments: Partial<Record<AssessmentMoment, AssessmentResult>>;
};

export const emptyProgress: DemoProgress = { completed: {}, errors: {}, assessments: {} };

export const REVIEW_INTERVALS = [1, 3, 7, 21] as const;

function normalizeRecord(record: Partial<CompletedLesson>): CompletedLesson {
  return {
    score: typeof record.score === "number" ? record.score : 0,
    completedAt: typeof record.completedAt === "string" ? record.completedAt : new Date().toISOString(),
    // Registros antigos não tinham XP explícito: assumem o padrão histórico.
    xpAwarded: typeof record.xpAwarded === "number" ? record.xpAwarded : 60,
    reviewedIntervals: Array.isArray(record.reviewedIntervals)
      ? record.reviewedIntervals.filter((value) => REVIEW_INTERVALS.includes(value as 1))
      : [],
    lastReviewedAt: typeof record.lastReviewedAt === "string" ? record.lastReviewedAt : null,
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
    const errors = parsed.errors && typeof parsed.errors === "object" ? parsed.errors : {};
    const assessments = parsed.assessments && typeof parsed.assessments === "object"
      ? parsed.assessments
      : {};
    return { completed, errors, assessments };
  } catch {
    return emptyProgress;
  }
}

/**
 * Registra a conclusão de uma missão. O XP informado é somado ao já acumulado
 * (quem chama decide o valor: 0 para revisões e o total na primeira conclusão).
 * Mantém a maior pontuação e a primeira data de conclusão.
 */
export function completeLesson(slug: string, score: number, xpAwarded: number): DemoProgress {
  const current = readProgress();
  const previous = current.completed[slug];
  const now = new Date();
  const reviewedIntervals = [...(previous?.reviewedIntervals ?? [])];
  let lastReviewedAt = previous?.lastReviewedAt ?? null;
  if (previous) {
    const baseDate = new Date(previous.lastReviewedAt ?? previous.completedAt);
    const dueInterval = REVIEW_INTERVALS.find((interval) => (
      !reviewedIntervals.includes(interval)
      && now.getTime() >= baseDate.getTime() + interval * 86_400_000
    ));
    if (dueInterval) {
      reviewedIntervals.push(dueInterval);
      lastReviewedAt = now.toISOString();
    }
  }
  const next: DemoProgress = {
    ...current,
    completed: {
      ...current.completed,
      [slug]: {
        score: Math.max(score, previous?.score ?? 0),
        completedAt: previous?.completedAt ?? now.toISOString(),
        xpAwarded: (previous?.xpAwarded ?? 0) + Math.max(0, xpAwarded),
        reviewedIntervals,
        lastReviewedAt,
      },
    },
  };
  window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event(PROGRESS_EVENT));
  return next;
}

export type ScheduledReview = {
  slug: string;
  interval: number;
  dueAt: string;
  due: boolean;
};

export function reviewSchedule(progress: DemoProgress, now: Date): ScheduledReview[] {
  return Object.entries(progress.completed).flatMap(([slug, lesson]) => {
    const interval = REVIEW_INTERVALS.find(
      (candidate) => !lesson.reviewedIntervals.includes(candidate),
    );
    if (!interval) return [];
    const baseDate = new Date(lesson.lastReviewedAt ?? lesson.completedAt);
    const due = new Date(baseDate.getTime() + interval * 86_400_000);
    return [{ slug, interval, dueAt: due.toISOString(), due: due <= now }];
  }).sort((a, b) => a.dueAt.localeCompare(b.dueAt));
}

export function recordLearningError(slug: string, category: ErrorCategory): DemoProgress {
  const current = readProgress();
  const previous = current.errors[category];
  const next: DemoProgress = {
    ...current,
    errors: {
      ...current.errors,
      [category]: {
        count: (previous?.count ?? 0) + 1,
        lastAt: new Date().toISOString(),
        lessons: [...new Set([...(previous?.lessons ?? []), slug])],
      },
    },
  };
  window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event(PROGRESS_EVENT));
  return next;
}

export function saveAssessment(
  moment: AssessmentMoment,
  result: Omit<AssessmentResult, "completedAt">,
): DemoProgress {
  const current = readProgress();
  const next: DemoProgress = {
    ...current,
    assessments: {
      ...current.assessments,
      [moment]: { ...result, completedAt: new Date().toISOString() },
    },
  };
  window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event(PROGRESS_EVENT));
  return next;
}

export function progressStats(progress: DemoProgress, lessonCount = 23) {
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
    ...progress,
    completed: Object.fromEntries(
      Object.entries(progress.completed).filter(([slug]) => allowed.has(slug)),
    ),
  };
}
