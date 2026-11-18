export type QuestionType = "MCQ" | "FILL_IN" | "ORDERING" | "LISTENING";

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

export type CourseSummary = {
  slug: string;
  title: string;
  description: string;
  level: string;
  unitCount: number;
  lessonCount: number;
};

export type LessonChoice = {
  id: number;
  text: string;
  position: number;
};

export type LessonQuestion = {
  id: number;
  type: QuestionType;
  prompt: string;
  position: number;
  choices?: LessonChoice[];
  tokens?: string[];
  audioText?: string;
};

export type DialogueLine = {
  speaker: string;
  line: string;
};

export type ProductionTask = {
  mode: "SPEAKING" | "WRITING";
  prompt: string;
  model: string;
  checklist: string[];
};

export type LessonPedagogy = {
  objective: string;
  activationPrompt: string;
  commonMistakes: string[];
  productionTask: ProductionTask;
  reviewPrompts: string[];
};

export type LessonDetail = LessonSummary & {
  unit: string;
  theory: string;
  example: string;
  keyPoints: string[];
  dialogue?: DialogueLine[];
  pedagogy?: LessonPedagogy;
  passingPercent: number;
  questions: LessonQuestion[];
};

export type AnswerFeedback = {
  isCorrect: boolean;
  explanation: string;
  selectedChoiceId?: number;
  correctChoiceId?: number;
  correctAnswer?: string;
};

export type AnswerPayload = {
  choiceId?: number;
  answer?: string;
  order?: string[];
};

export function flattenLessons(outline: CourseOutline | null): LessonSummary[] {
  return outline?.units.flatMap((unit) => unit.lessons) ?? [];
}

async function fetchJson<T>(url: string, errorMessage: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, init);
  if (!response.ok) {
    throw new Error(errorMessage);
  }
  return response.json() as Promise<T>;
}

export async function getCourses(signal?: AbortSignal): Promise<CourseSummary[]> {
  return fetchJson("/api/v1/demo/courses/", "Não foi possível carregar os cursos.", { signal });
}

export async function getCourseOutline(slug: string, signal?: AbortSignal): Promise<CourseOutline> {
  return fetchJson(
    `/api/v1/demo/courses/${encodeURIComponent(slug)}/outline/`,
    "Não foi possível carregar a trilha.",
    { signal },
  );
}

export async function getLesson(slug: string, signal?: AbortSignal): Promise<LessonDetail> {
  return fetchJson(
    `/api/v1/demo/lessons/${encodeURIComponent(slug)}/`,
    "Não foi possível carregar esta missão.",
    { signal },
  );
}

export async function checkAnswer(
  slug: string,
  questionId: number,
  payload: AnswerPayload,
): Promise<AnswerFeedback> {
  const response = await fetch(`/api/v1/demo/lessons/${encodeURIComponent(slug)}/answer/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ questionId, ...payload }),
  });
  if (!response.ok) {
    throw new Error("Não foi possível corrigir sua resposta.");
  }
  return response.json() as Promise<AnswerFeedback>;
}
