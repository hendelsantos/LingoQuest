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
  type CourseOutline,
  type CourseSummary,
} from "@/lib/learning";

const DEFAULT_COURSE = "a1-foundations";

export function LearningPath({ basePath = "/app" }: { basePath?: string }) {
  const [courses, setCourses] = useState<CourseSummary[]>([]);
  const [selectedSlug, setSelectedSlug] = useState(DEFAULT_COURSE);
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getCourses(controller.signal).then((availableCourses) => {
      setCourses(availableCourses);
      const requestedCourse = new URLSearchParams(window.location.search).get("course");
      if (
        requestedCourse
        && requestedCourse !== DEFAULT_COURSE
        && availableCourses.some((course) => course.slug === requestedCourse)
      ) {
        setOutline(null);
        setSelectedSlug(requestedCourse);
      }
    }).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : "Erro inesperado.");
      }
    });
    const refreshProgress = () => setProgress(readProgress());
    refreshProgress();
    window.addEventListener(PROGRESS_EVENT, refreshProgress);
    window.addEventListener("storage", refreshProgress);
    return () => {
      controller.abort();
      window.removeEventListener(PROGRESS_EVENT, refreshProgress);
      window.removeEventListener("storage", refreshProgress);
    };
  }, []);

  useEffect(() => {
    const controller = new AbortController();
    getCourseOutline(selectedSlug, controller.signal).then(setOutline).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : "Erro inesperado.");
      }
    });
    return () => controller.abort();
  }, [selectedSlug]);

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
          <h1>{outline?.title ?? courses.find((course) => course.slug === selectedSlug)?.title ?? "Carregando…"}</h1>
          <p>{outline?.description ?? "Escolha um nível e avance missão por missão."}</p>
        </div>
        <div className="learn-progress-summary">
          <strong>{stats.percent}%</strong>
          <span>{stats.completedCount} de {outline?.lessonCount ?? 0} missões</span>
        </div>
      </header>

      {error ? <div className="student-error" role="alert">{error}</div> : null}
      {!outline && !error ? <div className="lesson-skeleton">Preparando a trilha…</div> : null}

      <div className="unit-list">
        {outline?.units.map((unit) => (
          <section className="unit-section" key={unit.title}>
            <div className="unit-heading">
              <span>Unidade {unit.position}</span>
              <div><h2>{unit.title}</h2><p>{unit.description}</p></div>
            </div>
            <div className="lesson-card-grid">
              {unit.lessons.map((lesson) => {
                const completed = courseProgress.completed[lesson.slug];
                return (
                  <article className={`lesson-card${completed ? " is-completed" : ""}`} key={lesson.slug}>
                    <div className="lesson-card-meta"><span>{lesson.skill}</span><small>{lesson.estimatedMinutes} min · +{lesson.xpReward} XP</small></div>
                    <h3>{lesson.title}</h3><p>{lesson.summary}</p>
                    <div className="lesson-card-footer"><span>{completed ? `✓ Concluída · ${completed.score}%` : "Pronta para começar"}</span><Link href={`${basePath}/learn/${lesson.slug}?course=${encodeURIComponent(selectedSlug)}`}>{completed ? "Revisar" : "Começar"} →</Link></div>
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
