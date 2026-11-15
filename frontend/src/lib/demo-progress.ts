export const PROGRESS_STORAGE_KEY = "lingoquest.demo.progress.v1";

export type CompletedLesson = {
  score: number;
  completedAt: string;
};

export type DemoProgress = {
  completed: Record<string, CompletedLesson>;
};

export const emptyProgress: DemoProgress = { completed: {} };

export function readProgress(): DemoProgress {
  if (typeof window === "undefined") return emptyProgress;
  try {
    const stored = window.localStorage.getItem(PROGRESS_STORAGE_KEY);
    if (!stored) return emptyProgress;
    const parsed = JSON.parse(stored) as DemoProgress;
    return parsed && typeof parsed.completed === "object" ? parsed : emptyProgress;
  } catch {
    return emptyProgress;
  }
}

export function completeLesson(slug: string, score: number): DemoProgress {
  const current = readProgress();
  const previous = current.completed[slug];
  const next = {
    completed: {
      ...current.completed,
      [slug]: {
        score: Math.max(score, previous?.score ?? 0),
        completedAt: previous?.completedAt ?? new Date().toISOString(),
      },
    },
  };
  window.localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(next));
  window.dispatchEvent(new Event("lingoquest-progress"));
  return next;
}

export function progressStats(progress: DemoProgress, lessonCount = 8) {
  const completedCount = Object.keys(progress.completed).length;
  return {
    completedCount,
    xp: completedCount * 60,
    percent: lessonCount > 0 ? Math.round((completedCount / lessonCount) * 100) : 0,
  };
}
