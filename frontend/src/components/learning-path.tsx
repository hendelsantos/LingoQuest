"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

import { emptyProgress, progressStats, readProgress, type DemoProgress } from "@/lib/demo-progress";
import { getCourseOutline, type CourseOutline } from "@/lib/learning";

export function LearningPath() {
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getCourseOutline(controller.signal).then(setOutline).catch((reason: unknown) => {
      if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Erro inesperado.");
    });
    const progressTimer = window.setTimeout(() => setProgress(readProgress()), 0);
    return () => {
      controller.abort();
      window.clearTimeout(progressTimer);
    };
  }, []);

  const stats = progressStats(progress, outline?.lessonCount ?? 8);

  return (
    <div className="learn-page">
      <header className="learn-header">
        <div><span className="student-kicker">Seu curso atual</span><h1>A1 Foundations</h1><p>Construa uma base sólida para se apresentar e conversar sobre a vida cotidiana.</p></div>
        <div className="learn-progress-summary"><strong>{stats.percent}%</strong><span>{stats.completedCount} de {outline?.lessonCount ?? 8} missões</span></div>
      </header>

      {error ? <div className="student-error" role="alert">{error}</div> : null}
      {!outline && !error ? <div className="lesson-skeleton">Preparando a trilha…</div> : null}

      <div className="unit-list">
        {outline?.units.map((unit) => (
          <section className="unit-section" key={unit.title}>
            <div className="unit-heading"><span>Unidade {unit.position}</span><div><h2>{unit.title}</h2><p>{unit.description}</p></div></div>
            <div className="lesson-card-grid">
              {unit.lessons.map((lesson) => {
                const completed = progress.completed[lesson.slug];
                return (
                  <article className={`lesson-card${completed ? " is-completed" : ""}`} key={lesson.slug}>
                    <div className="lesson-card-meta"><span>{lesson.skill}</span><small>{lesson.estimatedMinutes} min · +{lesson.xpReward} XP</small></div>
                    <h3>{lesson.title}</h3><p>{lesson.summary}</p>
                    <div className="lesson-card-footer"><span>{completed ? `✓ Concluída · ${completed.score}%` : "Pronta para começar"}</span><Link href={`/app/learn/${lesson.slug}`}>{completed ? "Revisar" : "Começar"} →</Link></div>
                  </article>
                );
              })}
            </div>
          </section>
        ))}
      </div>

      <section className="planned-levels"><div><strong>A2</strong><span>Elementary</span></div><div><strong>B1</strong><span>Intermediate</span></div><div><strong>B2–C2</strong><span>Planejados</span></div></section>
    </div>
  );
}
