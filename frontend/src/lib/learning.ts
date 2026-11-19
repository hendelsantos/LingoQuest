import { getCsrfToken } from "./auth";

export type QuestionType = "MCQ" | "FILL_IN" | "ORDERING" | "LISTENING";

export type LessonSummary = {
  slug: string;
  title: string;
  skill: string;
  summary: string;
  estimatedMinutes: number;
  xpReward: number;
  position: number;
  completed?: boolean;
  bestScore?: number;
  inProgress?: boolean;
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

export type EnrollmentStatus = "ACTIVE" | "PAUSED" | "COMPLETED" | "CANCELLED";

export type Enrollment = {
  id: string;
  student: { id: string; name: string; email: string };
  course: { slug: string; title: string; level: string };
  status: EnrollmentStatus;
  enrolledAt: string;
  endedAt: string | null;
};

export type LearningAccess = "demo" | "account";

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
  errorCategory?: import("./demo-progress").ErrorCategory;
};

export type AnswerPayload = {
  choiceId?: number;
  answer?: string;
  order?: string[];
};

export type AttemptAnswer = AnswerFeedback & AnswerPayload & {
  questionId: number;
  answeredAt: string;
};

export type LessonAttempt = {
  id: string;
  lessonSlug: string;
  status: "IN_PROGRESS" | "SUBMITTED" | "ABANDONED";
  startedAt: string;
  submittedAt: string | null;
  answeredCount: number;
  correctCount: number;
  totalQuestions: number;
  scorePercent: number;
  passed: boolean;
  xpAwarded: number;
  answers: AttemptAnswer[];
};

export type StudentLearningSummary = {
  xp: number;
  completedLessons: number;
  totalLessons: number;
  progressPercent: number;
};

export type AssessmentMoment = "initial" | "final";

export type AssessmentQuestion = {
  id: string;
  type: QuestionType;
  prompt: string;
  choices?: string[];
  tokens?: string[];
  audioText?: string;
};

export type AssessmentDetail = {
  moment: AssessmentMoment;
  title: string;
  description: string;
  questions: AssessmentQuestion[];
  speakingTask: string;
  writingTask: string;
};

export type AssessmentFeedback = {
  isCorrect: boolean;
  explanation: string;
  correctChoiceIndex?: number;
  correctAnswer?: string;
  errorCategory?: import("./demo-progress").ErrorCategory;
};

export function flattenLessons(outline: CourseOutline | null): LessonSummary[] {
  return outline?.units.flatMap((unit) => unit.lessons) ?? [];
}

async function fetchJson<T>(url: string, errorMessage: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    credentials: "same-origin",
    cache: "no-store",
    ...init,
  });
  if (!response.ok) {
    throw new Error(errorMessage);
  }
  return response.json() as Promise<T>;
}

export async function getCourses(signal?: AbortSignal): Promise<CourseSummary[]> {
  return fetchJson("/api/v1/demo/courses/", "Não foi possível carregar os cursos.", { signal });
}

export async function getEnrollments(signal?: AbortSignal): Promise<Enrollment[]> {
  return fetchJson(
    "/api/v1/me/enrollments/",
    "Não foi possível carregar suas matrículas.",
    { signal },
  );
}

export async function getCourseOutline(
  slug: string,
  signal?: AbortSignal,
  access: LearningAccess = "demo",
): Promise<CourseOutline> {
  const prefix = access === "demo" ? "/api/v1/demo" : "/api/v1";
  return fetchJson(
    `${prefix}/courses/${encodeURIComponent(slug)}/outline/`,
    "Não foi possível carregar a trilha.",
    { signal },
  );
}

export async function getLesson(
  slug: string,
  signal?: AbortSignal,
  access: LearningAccess = "demo",
): Promise<LessonDetail> {
  const prefix = access === "demo" ? "/api/v1/demo" : "/api/v1";
  return fetchJson(
    `${prefix}/lessons/${encodeURIComponent(slug)}/`,
    "Não foi possível carregar esta missão.",
    { signal },
  );
}

export async function checkAnswer(
  slug: string,
  questionId: number,
  payload: AnswerPayload,
  access: LearningAccess = "demo",
): Promise<AnswerFeedback> {
  const prefix = access === "demo" ? "/api/v1/demo" : "/api/v1";
  const csrfToken = access === "account" ? await getCsrfToken() : null;
  const response = await fetch(`${prefix}/lessons/${encodeURIComponent(slug)}/answer/`, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      ...(csrfToken ? { "X-CSRFToken": csrfToken } : {}),
    },
    body: JSON.stringify({ questionId, ...payload }),
  });
  if (!response.ok) {
    throw new Error("Não foi possível corrigir sua resposta.");
  }
  return response.json() as Promise<AnswerFeedback>;
}

async function postAccountJson<T>(url: string, body?: unknown): Promise<T> {
  const csrfToken = await getCsrfToken();
  const response = await fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
  if (!response.ok) {
    const payload = await response.json().catch(() => null) as { detail?: string } | null;
    throw new Error(payload?.detail ?? "Não foi possível salvar seu progresso.");
  }
  return response.json() as Promise<T>;
}

export async function startLessonAttempt(slug: string): Promise<LessonAttempt> {
  return postAccountJson(
    `/api/v1/lessons/${encodeURIComponent(slug)}/attempts/`,
  );
}

export async function submitAttemptAnswer(
  attemptId: string,
  questionId: number,
  payload: AnswerPayload,
): Promise<AttemptAnswer> {
  return postAccountJson(
    `/api/v1/attempts/${encodeURIComponent(attemptId)}/answers/`,
    { questionId, ...payload },
  );
}

export async function finishLessonAttempt(attemptId: string): Promise<LessonAttempt> {
  return postAccountJson(
    `/api/v1/attempts/${encodeURIComponent(attemptId)}/finish/`,
  );
}

export async function getStudentLearningSummary(
  signal?: AbortSignal,
): Promise<StudentLearningSummary> {
  return fetchJson(
    "/api/v1/me/dashboard/",
    "Não foi possível carregar seu progresso.",
    { signal },
  );
}

export async function getAssessment(
  moment: AssessmentMoment,
  signal?: AbortSignal,
): Promise<AssessmentDetail> {
  return fetchJson(
    `/api/v1/demo/assessments/a1/${moment}/`,
    "Não foi possível carregar a avaliação.",
    { signal },
  );
}

export async function checkAssessmentAnswer(
  moment: AssessmentMoment,
  payload: {
    questionId: string;
    choiceIndex?: number;
    answer?: string;
    order?: string[];
  },
): Promise<AssessmentFeedback> {
  return fetchJson(
    `/api/v1/demo/assessments/a1/${moment}/answer/`,
    "Não foi possível corrigir a resposta.",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    },
  );
}
