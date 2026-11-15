"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import { emptyProgress, progressStats, readProgress, type DemoProgress } from "@/lib/demo-progress";
import { flattenLessons, getCourseOutline, type CourseOutline } from "@/lib/learning";

export function DashboardDemo() {
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getCourseOutline(controller.signal).then(setOutline).catch((reason: unknown) => {
      if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Erro inesperado.");
    });
    const refreshProgress = () => setProgress(readProgress());
    refreshProgress();
    window.addEventListener("lingoquest-progress", refreshProgress);
    window.addEventListener("storage", refreshProgress);
    return () => {
      controller.abort();
      window.removeEventListener("lingoquest-progress", refreshProgress);
      window.removeEventListener("storage", refreshProgress);
    };
  }, []);

  const lessons = useMemo(() => flattenLessons(outline), [outline]);
  const stats = progressStats(progress, outline?.lessonCount ?? 8);
  const nextLesson = lessons.find((lesson) => !progress.completed[lesson.slug]) ?? lessons[0];

  return (
    <>
      <section className="student-hero">
        <div>
          <span className="student-kicker">Sua jornada começa aqui</span>
          <h1><span>Small steps.</span><br />Big adventures.</h1>
          <p>Aprenda inglês um desafio de cada vez. Finn está pronto para a próxima missão!</p>
          <Link className="student-primary-button" href={nextLesson ? `/app/learn/${nextLesson.slug}` : "/app/learn"}>
            {stats.completedCount ? "Continuar aprendendo" : "Começar primeira missão"} →
          </Link>
        </div>
        <Image src="/characters/finn-welcome.svg" alt="Finn, o guia da sua jornada" width={360} height={330} priority />
      </section>

      <section className="student-stat-grid" aria-label="Seu progresso">
        <article><span className="stat-icon is-warm">⚡</span><div><strong>{stats.xp}</strong><small>Pontos de experiência</small></div></article>
        <article><span className="stat-icon is-green">◇</span><div><strong>{stats.completedCount}/{outline?.lessonCount ?? 8}</strong><small>Missões concluídas</small></div></article>
        <article><span className="stat-icon is-lavender">◎</span><div><strong>{stats.percent}%</strong><small>Progresso A1</small></div></article>
      </section>

      <div className="student-section-heading">
        <div><h2>Your learning path</h2><p>Onde você está agora</p></div>
        <Link href="/app/learn">Ver trilha →</Link>
      </div>

      {error ? <div className="student-error" role="alert">{error} <button onClick={() => window.location.reload()}>Tentar novamente</button></div> : null}

      <section className="dashboard-grid">
        <article className="learning-path-card">
          <div className="course-card-topline"><span>A1 · Foundations</span><strong>{stats.percent}%</strong></div>
          <div className="course-progress"><i style={{ width: `${stats.percent}%` }} /></div>
          <small>{stats.percent}% concluído · {outline?.lessonCount ?? 8} missões</small>
          <div className="compact-lesson-list">
            {lessons.slice(0, 4).map((lesson, index) => {
              const done = Boolean(progress.completed[lesson.slug]);
              return (
                <div className="compact-lesson" key={lesson.slug}>
                  <span className={done ? "is-done" : ""}>{done ? "✓" : String(index + 1).padStart(2, "0")}</span>
                  <div><strong>{lesson.title}</strong><small>{lesson.summary} · {lesson.skill}</small></div>
                  <Link href={`/app/learn/${lesson.slug}`}>{done ? "Revisar" : "Jogar"}</Link>
                </div>
              );
            })}
            {!outline && !error ? <p className="loading-copy">Carregando suas missões…</p> : null}
          </div>
        </article>

        <aside className="dashboard-aside">
          <article className="live-card"><span>• Aulas ao vivo</span><h3>Live classroom</h3><p>Teste câmera, microfone e uma atividade dentro da sala demonstrativa.</p><Link href="/app/live">Ver sala de aula →</Link></article>
          <article className="mini-card"><span>✳</span><div><h3>Mini challenge</h3><p>Conclua uma missão e desbloqueie 60 XP.</p></div></article>
          <article className="mini-card"><span>✎</span><div><h3>Seu caderno digital</h3><p>Guarde expressões e revise vocabulário.</p><button disabled>Abrir em breve</button></div></article>
        </aside>
      </section>
    </>
  );
}
