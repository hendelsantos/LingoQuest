"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import {
  PROGRESS_EVENT,
  emptyProgress,
  progressForSlugs,
  progressStats,
  readProgress,
  type DemoProgress,
} from "@/lib/demo-progress";
import {
  flattenLessons,
  getCourseOutline,
  getCourses,
  getEnrollments,
  type CourseOutline,
  type CourseSummary,
  type LearningAccess,
} from "@/lib/learning";

const DEFAULT_COURSE = "a1-foundations";

export function LearningPath({ basePath = "/app", access = "account" }: { basePath?: string; access?: LearningAccess }) {
  const [courses, setCourses] = useState<CourseSummary[]>([]);
  const [selectedSlug, setSelectedSlug] = useState(access === "demo" ? DEFAULT_COURSE : "");
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [error, setError] = useState("");
  const [emptyMessage, setEmptyMessage] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    const coursesPromise = access === "demo"
      ? getCourses(controller.signal)
      : getEnrollments(controller.signal).then((enrollments) => enrollments
          .filter((enrollment) => enrollment.status === "ACTIVE" || enrollment.status === "COMPLETED")
          .map((enrollment) => ({
            ...enrollment.course,
            description: "Curso vinculado à sua conta.",
            unitCount: 0,
            lessonCount: 0,
          })));
    coursesPromise.then((availableCourses) => {
      setCourses(availableCourses);
      const requestedCourse = new URLSearchParams(window.location.search).get("course");
      const requestedIsAvailable = requestedCourse
        && availableCourses.some((course) => course.slug === requestedCourse);
      const nextSlug = requestedIsAvailable
        ? requestedCourse
        : availableCourses[0]?.slug ?? "";
      setOutline(null);
      setSelectedSlug(nextSlug);
      if (!nextSlug && access === "account") {
        setEmptyMessage("Você ainda não possui uma matrícula ativa. Fale com a administração da escola.");
      }
    }).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : "Erro inesperado.");
      }
    });
    const refreshProgress = () => setProgress(access === "demo" ? readProgress() : emptyProgress);
    refreshProgress();
    if (access === "demo") {
      window.addEventListener(PROGRESS_EVENT, refreshProgress);
      window.addEventListener("storage", refreshProgress);
    }
    return () => {
      controller.abort();
      window.removeEventListener(PROGRESS_EVENT, refreshProgress);
      window.removeEventListener("storage", refreshProgress);
    };
  }, [access]);

  useEffect(() => {
    const controller = new AbortController();
    if (!selectedSlug) return () => controller.abort();
    getCourseOutline(selectedSlug, controller.signal, access).then(setOutline).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : "Erro inesperado.");
      }
    });
    return () => controller.abort();
  }, [access, selectedSlug]);

  function chooseCourse(slug: string) {
    if (slug === selectedSlug) return;
    setOutline(null);
    setError("");
    setSelectedSlug(slug);
    window.history.replaceState(null, "", `${basePath}/learn?course=${encodeURIComponent(slug)}`);
  }

  const lessons = useMemo(() => flattenLessons(outline), [outline]);
  const courseProgress = useMemo(
    () => progressForSlugs(progress, lessons.map((lesson) => lesson.slug)),
    [lessons, progress],
  );
  const stats = progressStats(courseProgress, outline?.lessonCount ?? 0);
  const accountCompletedCount = lessons.filter((lesson) => lesson.completed).length;
  const accountPercent = outline?.lessonCount
    ? Math.round((accountCompletedCount / outline.lessonCount) * 100)
    : 0;

  return (
    <div className="learn-page">
      <nav className="course-switcher" aria-label="Escolha seu nível de inglês">
        {courses.map((course) => (
          <button
            className={course.slug === selectedSlug ? "is-active" : ""}
            key={course.slug}
            type="button"
            onClick={() => chooseCourse(course.slug)}
          >
            <strong>{course.level}</strong>
            <span>{course.title.replace(`${course.level} `, "")}</span>
          </button>
        ))}
      </nav>

      <header className="learn-header">
        <div>
          <span className="student-kicker">Sua trilha atual</span>
          <h1>{outline?.title ?? courses.find((course) => course.slug === selectedSlug)?.title ?? (emptyMessage ? "Nenhuma trilha liberada" : "Carregando…")}</h1>
          <p>{outline?.description ?? "Escolha um nível e avance missão por missão."}</p>
        </div>
        <div className="learn-progress-summary">
          <strong>{access === "demo" ? `${stats.percent}%` : `${accountPercent}%`}</strong>
          <span>{access === "demo" ? stats.completedCount : accountCompletedCount} de {outline?.lessonCount ?? 0} missões</span>
        </div>
      </header>

      {error ? <div className="student-error" role="alert">{error}</div> : null}
      {emptyMessage ? <div className="student-error" role="status">{emptyMessage}</div> : null}
      {!outline && !error && !emptyMessage ? <div className="lesson-skeleton">Preparando a trilha…</div> : null}

      <div className="unit-list">
        {outline?.units.map((unit) => (
          <section className="unit-section" key={unit.title}>
            <div className="unit-heading">
              <span>Unidade {unit.position}</span>
              <div><h2>{unit.title}</h2><p>{unit.description}</p></div>
            </div>
            <div className="lesson-card-grid">
              {unit.lessons.map((lesson) => {
                const demoCompletion = access === "demo" ? courseProgress.completed[lesson.slug] : undefined;
                const completed = Boolean(demoCompletion || lesson.completed);
                const bestScore = demoCompletion?.score ?? lesson.bestScore;
                return (
                  <article className={`lesson-card${completed ? " is-completed" : ""}`} key={lesson.slug}>
                    <div className="lesson-card-meta"><span>{lesson.skill}</span><small>{lesson.estimatedMinutes} min · {access === "demo" ? `+${lesson.xpReward} XP` : "progresso sincronizado"}</small></div>
                    <h3>{lesson.title}</h3><p>{lesson.summary}</p>
                    <div className="lesson-card-footer"><span>{completed ? `✓ Concluída · ${bestScore}%` : lesson.inProgress ? "Tentativa em andamento" : "Pronta para começar"}</span><Link href={`${basePath}/learn/${lesson.slug}?course=${encodeURIComponent(selectedSlug)}`}>{completed ? "Revisar" : lesson.inProgress ? "Continuar" : "Começar"} →</Link></div>
                  </article>
                );
              })}
            </div>
          </section>
        ))}
      </div>
    </div>
  );
}
