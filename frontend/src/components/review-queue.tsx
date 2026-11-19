"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import {
  PROGRESS_EVENT,
  emptyProgress,
  readProgress,
  reviewSchedule,
  type DemoProgress,
  type ErrorCategory,
} from "@/lib/demo-progress";
import { flattenLessons, getCourseOutline, type CourseOutline } from "@/lib/learning";

const categoryLabels: Record<ErrorCategory, string> = {
  GRAMMAR: "Estruturas e gramática",
  VOCABULARY: "Vocabulário",
  WORD_ORDER: "Ordem das palavras",
  LISTENING: "Compreensão auditiva",
  SPELLING: "Ortografia",
  COMPREHENSION: "Compreensão em contexto",
};

export function ReviewQueue({ basePath = "/app" }: { basePath?: string }) {
  const [outline, setOutline] = useState<CourseOutline | null>(null);
  const [progress, setProgress] = useState<DemoProgress>(emptyProgress);
  const [reviewNow, setReviewNow] = useState<Date | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    getCourseOutline("a1-foundations", controller.signal).then(setOutline);
    const refresh = () => {
      setProgress(readProgress());
      setReviewNow(new Date());
    };
    refresh();
    window.addEventListener(PROGRESS_EVENT, refresh);
    window.addEventListener("storage", refresh);
    return () => {
      controller.abort();
      window.removeEventListener(PROGRESS_EVENT, refresh);
      window.removeEventListener("storage", refresh);
    };
  }, []);

  const lessons = useMemo(() => flattenLessons(outline), [outline]);
  const bySlug = useMemo(
    () => new Map(lessons.map((lesson) => [lesson.slug, lesson])),
    [lessons],
  );
  const schedule = reviewNow ? reviewSchedule(progress, reviewNow) : [];
  const due = schedule.filter((item) => item.due);
  const upcoming = schedule.filter((item) => !item.due).slice(0, 5);
  const errors = Object.entries(progress.errors)
    .filter((entry): entry is [ErrorCategory, NonNullable<typeof entry[1]>] => Boolean(entry[1]))
    .sort((a, b) => b[1].count - a[1].count);

  return (
    <div className="review-page">
      <header className="review-header">
        <span className="student-kicker">Recuperação ativa</span>
        <h1>Revisar antes de esquecer.</h1>
        <p>A fila usa intervalos de 1, 3, 7 e 21 dias. Refaça a missão sem reler primeiro; consulte a teoria somente depois da tentativa.</p>
      </header>

      <section className="review-section" aria-labelledby="due-review-title">
        <div className="student-section-heading"><div><h2 id="due-review-title">Para revisar agora</h2><p>{due.length ? `${due.length} retomada(s) disponível(is)` : "Nenhuma revisão vencida"}</p></div></div>
        {due.length ? <div className="review-list">{due.map((item) => {
          const lesson = bySlug.get(item.slug);
          return <article key={item.slug}><div><span>Revisão de {item.interval} dia{item.interval === 1 ? "" : "s"}</span><h3>{lesson?.title ?? item.slug}</h3><p>{lesson?.summary}</p></div><Link className="student-primary-button" href={`${basePath}/learn/${item.slug}?course=a1-foundations`}>Revisar →</Link></article>;
        })}</div> : <div className="review-empty">Conclua uma missão para iniciar o ciclo de revisão espaçada.</div>}
      </section>

      <div className="review-grid">
        <section className="review-section">
          <div className="student-section-heading"><div><h2>Próximas revisões</h2><p>Agenda baseada na primeira conclusão</p></div></div>
          <div className="upcoming-list">{upcoming.length ? upcoming.map((item) => <div key={item.slug}><strong>{bySlug.get(item.slug)?.title ?? item.slug}</strong><span>{new Intl.DateTimeFormat("pt-BR", { day: "2-digit", month: "short" }).format(new Date(item.dueAt))} · intervalo {item.interval}d</span></div>) : <p>Nenhuma revisão agendada.</p>}</div>
        </section>

        <section className="review-section">
          <div className="student-section-heading"><div><h2>Padrões de dificuldade</h2><p>Erros registrados neste navegador</p></div></div>
          <div className="error-pattern-list">{errors.length ? errors.map(([category, summary]) => <div key={category}><span>{summary.count}</span><div><strong>{categoryLabels[category]}</strong><small>{summary.lessons.length} missão(ões)</small></div></div>) : <p>Os erros aparecerão aqui por categoria, sem punição ou ranking.</p>}</div>
        </section>
      </div>
    </div>
  );
}
