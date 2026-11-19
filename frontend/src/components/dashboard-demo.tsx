"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import {
  PROGRESS_EVENT,
  emptyProgress,
  progressForSlugs,
  progressStats,
  readProgress,
  reviewSchedule,
  type DemoProgress,
} from "@/lib/demo-progress";
import { flattenLessons, getCourseOutline, type CourseOutline } from "@/lib/learning";

export function DashboardDemo({ basePath = "/app" }: { basePath?: string }) {
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [reviewNow, setReviewNow] = useState<Date | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getCourseOutline("a1-foundations", controller.signal).then(setOutline).catch((reason: unknown) => {
      if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Erro inesperado.");
    });
    const refreshProgress = () => {
      setProgress(readProgress());
      setReviewNow(new Date());
    };
    refreshProgress();
    window.addEventListener(PROGRESS_EVENT, refreshProgress);
    window.addEventListener("storage", refreshProgress);
    return () => {
      controller.abort();
      window.removeEventListener(PROGRESS_EVENT, refreshProgress);
      window.removeEventListener("storage", refreshProgress);
    };
  }, []);

  const lessons = useMemo(() => flattenLessons(outline), [outline]);
  const courseProgress = useMemo(
    () => progressForSlugs(progress, lessons.map((lesson) => lesson.slug)),
    [lessons, progress],
  );
  const stats = progressStats(courseProgress, outline?.lessonCount ?? 23);
  const courseComplete = Boolean(outline && stats.completedCount >= outline.lessonCount);
  const nextLesson = lessons.find((lesson) => !courseProgress.completed[lesson.slug]) ?? lessons[0];
  const dueReviews = reviewNow
    ? reviewSchedule(courseProgress, reviewNow).filter((item) => item.due).length
    : 0;

  return (
    <>
      <section className="student-hero">
        <div>
          <span className="student-kicker">Sua jornada começa aqui</span>
          <h1><span>Small steps.</span><br />Big adventures.</h1>
          <p>Aprenda inglês um desafio de cada vez. Finn está pronto para a próxima missão!</p>
          <Link className="student-primary-button" href={nextLesson ? `${basePath}/learn/${nextLesson.slug}` : `${basePath}/learn`}>
            {stats.completedCount ? "Continuar aprendendo" : "Começar primeira missão"} →
          </Link>
        </div>
        <Image src="/characters/finn-welcome.svg" alt="Finn, o guia da sua jornada" width={360} height={330} priority />
      </section>

      <section className="student-stat-grid" aria-label="Seu progresso">
        <article><span className="stat-icon is-warm">⚡</span><div><strong>{stats.xp}</strong><small>Pontos de experiência</small></div></article>
        <article><span className="stat-icon is-green">◇</span><div><strong>{stats.completedCount}/{outline?.lessonCount ?? 23}</strong><small>Missões concluídas</small></div></article>
        <article><span className="stat-icon is-lavender">◎</span><div><strong>{stats.percent}%</strong><small>Progresso A1</small></div></article>
        <article><span className="stat-icon is-green">↻</span><div><strong>{dueReviews}</strong><small>Revisões para hoje</small></div></article>
      </section>

      <div className="student-section-heading">
        <div><h2>Your learning path</h2><p>Onde você está agora</p></div>
        <Link href={`${basePath}/learn`}>Ver trilha →</Link>
      </div>

      {error ? <div className="student-error" role="alert">{error} <button onClick={() => window.location.reload()}>Tentar novamente</button></div> : null}

      <section className="dashboard-grid">
        <article className="learning-path-card">
          <div className="course-card-topline"><span>A1 · Foundations</span><strong>{stats.percent}%</strong></div>
          <div className="course-progress"><i style={{ width: `${stats.percent}%` }} /></div>
          <small>{stats.percent}% concluído · {outline?.lessonCount ?? 23} missões</small>
          <div className="compact-lesson-list">
            {lessons.slice(0, 4).map((lesson, index) => {
              const done = Boolean(courseProgress.completed[lesson.slug]);
              return (
                <div className="compact-lesson" key={lesson.slug}>
                  <span className={done ? "is-done" : ""}>{done ? "✓" : String(index + 1).padStart(2, "0")}</span>
                  <div><strong>{lesson.title}</strong><small>{lesson.summary} · {lesson.skill}</small></div>
                  <Link href={`${basePath}/learn/${lesson.slug}`}>{done ? "Revisar" : "Jogar"}</Link>
                </div>
              );
            })}
            {!outline && !error ? <p className="loading-copy">Carregando suas missões…</p> : null}
          </div>
        </article>

        <aside className="dashboard-aside">
          <article className="live-card"><span>• Aulas ao vivo</span><h3>Live classroom</h3><p>Teste câmera, microfone e uma atividade dentro da sala demonstrativa.</p><Link href={`${basePath}/live`}>Ver sala de aula →</Link></article>
          <article className="mini-card"><span>↻</span><div><h3>Revisão espaçada</h3><p>Retome em 1, 3, 7 e 21 dias.</p><Link href={`${basePath}/review`}>{dueReviews ? `${dueReviews} para revisar` : "Ver agenda"} →</Link></div></article>
          <article className="mini-card"><span>◫</span><div><h3>Avaliação A1</h3>{!progress.assessments.initial ? <><p>Registre seu ponto de partida.</p><Link href={`${basePath}/assessment/initial`}>Começar avaliação →</Link></> : progress.assessments.final ? <><p>Inicial: {progress.assessments.initial.score}% · final: {progress.assessments.final.score}%</p><Link href={`${basePath}/assessment/final`}>Refazer avaliação final →</Link></> : courseComplete ? <><p>Ponto inicial: {progress.assessments.initial.score}%</p><Link href={`${basePath}/assessment/final`}>Fazer avaliação final →</Link></> : <p>A avaliação final será liberada após concluir as {outline?.lessonCount ?? 23} missões A1.</p>}</div></article>
          <article className="mini-card"><span>✳</span><div><h3>Mini challenge</h3><p>Conclua uma missão e desbloqueie 60 XP.</p></div></article>
          <article className="mini-card"><span>✎</span><div><h3>Seu caderno digital</h3><p>Guarde expressões e revise vocabulário.</p><button disabled>Abrir em breve</button></div></article>
        </aside>
      </section>
    </>
  );
}
