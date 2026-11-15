export type LessonSummary = {
  slug: string;
  title: string;
  skill: string;
  summary: string;
  estimatedMinutes: number;
  xpReward: number;
  position: number;
};

export type CourseUnit = {
  title: string;
  description: string;
  position: number;
  lessons: LessonSummary[];
};

export type CourseOutline = {
  slug: string;
  title: string;
  description: string;
  level: string;
  lessonCount: number;
  units: CourseUnit[];
};

export type LessonChoice = {
  id: number;
  text: string;
  position: number;
};

export type LessonQuestion = {
  id: number;
  prompt: string;
  position: number;
  choices: LessonChoice[];
};

export type LessonDetail = LessonSummary & {
  unit: string;
  theory: string;
  example: string;
  keyPoints: string[];
  passingPercent: number;
  questions: LessonQuestion[];
};

export type AnswerFeedback = {
  isCorrect: boolean;
  selectedChoiceId: number;
  correctChoiceId: number;
  explanation: string;
};

export function flattenLessons(outline: CourseOutline | null): LessonSummary[] {
  return outline?.units.flatMap((unit) => unit.lessons) ?? [];
}

export async function getCourseOutline(signal?: AbortSignal): Promise<CourseOutline> {
  const response = await fetch("/api/v1/demo/courses/a1-foundations/outline/", { signal });
  if (!response.ok) {
    throw new Error("Não foi possível carregar a trilha.");
  }
  return response.json() as Promise<CourseOutline>;
}

export async function getLesson(slug: string, signal?: AbortSignal): Promise<LessonDetail> {
  const response = await fetch(`/api/v1/demo/lessons/${encodeURIComponent(slug)}/`, { signal });
  if (!response.ok) {
    throw new Error("Não foi possível carregar esta missão.");
  }
  return response.json() as Promise<LessonDetail>;
}

export async function checkAnswer(
  slug: string,
  questionId: number,
  choiceId: number,
): Promise<AnswerFeedback> {
  const response = await fetch(`/api/v1/demo/lessons/${encodeURIComponent(slug)}/answer/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ questionId, choiceId }),
  });
  if (!response.ok) {
    throw new Error("Não foi possível corrigir sua resposta.");
  }
  return response.json() as Promise<AnswerFeedback>;
}
