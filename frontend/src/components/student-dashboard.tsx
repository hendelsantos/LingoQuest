"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

import {
  getEnrollments,
  getStudentLearningSummary,
  type Enrollment,
  type StudentLearningSummary,
} from "@/lib/learning";

export function StudentDashboard() {
  const [enrollments, setEnrollments] = useState<Enrollment[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [summary, setSummary] = useState<StudentLearningSummary | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    Promise.all([
      getEnrollments(controller.signal),
      getStudentLearningSummary(controller.signal),
    ])
      .then(([loadedEnrollments, loadedSummary]) => {
        setEnrollments(loadedEnrollments);
        setSummary(loadedSummary);
      })
      .catch((reason: unknown) => {
        if (!controller.signal.aborted) {
          setError(reason instanceof Error ? reason.message : "Erro inesperado.");
        }
      })
      .finally(() => {
        if (!controller.signal.aborted) setLoading(false);
      });
    return () => controller.abort();
  }, []);

  const accessible = enrollments.filter(
    (enrollment) => enrollment.status === "ACTIVE" || enrollment.status === "COMPLETED",
  );
  const active = enrollments.filter((enrollment) => enrollment.status === "ACTIVE").length;
  const completed = enrollments.filter((enrollment) => enrollment.status === "COMPLETED").length;

  return (
    <>
      <section className="student-hero">
        <div>
          <span className="student-kicker">Seu espaço de aprendizagem</span>
          <h1><span>Small steps.</span><br />Big adventures.</h1>
          <p>Sua conta mostra somente os cursos liberados pela escola e sincroniza tentativas, progresso e XP entre dispositivos.</p>
          {accessible.length ? <Link className="student-primary-button" href={`/app/learn?course=${encodeURIComponent(accessible[0].course.slug)}`}>Abrir minha trilha →</Link> : null}
        </div>
        <Image src="/characters/finn-welcome.svg" alt="Finn, o guia da sua jornada" width={360} height={330} priority />
      </section>

      <section className="student-stat-grid" aria-label="Suas matrículas">
        <article><span className="stat-icon is-green">◇</span><div><strong>{active}</strong><small>Matrículas ativas</small></div></article>
        <article><span className="stat-icon is-lavender">✓</span><div><strong>{completed}</strong><small>Cursos concluídos</small></div></article>
        <article><span className="stat-icon is-warm">⚡</span><div><strong>{summary?.xp ?? 0}</strong><small>XP confirmado</small></div></article>
        <article><span className="stat-icon is-green">◎</span><div><strong>{summary?.progressPercent ?? 0}%</strong><small>{summary?.completedLessons ?? 0} de {summary?.totalLessons ?? 0} missões</small></div></article>
      </section>

      <div className="student-section-heading">
        <div><h2>Suas trilhas</h2><p>Cursos vinculados à sua conta</p></div>
        {accessible.length ? <Link href="/app/learn">Ver currículo →</Link> : null}
      </div>

      {error ? <div className="student-error" role="alert">{error}</div> : null}
      {loading ? <div className="lesson-skeleton">Carregando suas matrículas…</div> : null}
      {!loading && !error && !enrollments.length ? <div className="review-empty">Você ainda não possui matrícula. Fale com a administração da escola.</div> : null}

      {enrollments.length ? <section className="lesson-card-grid">
        {enrollments.map((enrollment) => {
          const canOpen = enrollment.status === "ACTIVE" || enrollment.status === "COMPLETED";
          return <article className="lesson-card" key={enrollment.id}>
            <div className="lesson-card-meta"><span>{enrollment.course.level}</span><small>{statusLabel(enrollment.status)}</small></div>
            <h3>{enrollment.course.title}</h3>
            <p>{canOpen ? "Currículo publicado e disponível para estudo." : "O acesso ao currículo está temporariamente indisponível."}</p>
            <div className="lesson-card-footer"><span>{statusLabel(enrollment.status)}</span>{canOpen ? <Link href={`/app/learn?course=${encodeURIComponent(enrollment.course.slug)}`}>Abrir trilha →</Link> : null}</div>
          </article>;
        })}
      </section> : null}
    </>
  );
}

function statusLabel(status: Enrollment["status"]) {
  return {
    ACTIVE: "Matrícula ativa",
    PAUSED: "Matrícula pausada",
    COMPLETED: "Curso concluído",
    CANCELLED: "Matrícula cancelada",
  }[status];
}
