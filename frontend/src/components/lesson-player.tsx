"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import { completeLesson } from "@/lib/demo-progress";
import { checkAnswer, getLesson, type AnswerFeedback, type LessonDetail } from "@/lib/learning";

type Stage = "theory" | "quiz" | "result";

export function LessonPlayer({ slug }: { slug: string }) {
  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [stage, setStage] = useState<Stage>("theory");
  const [questionIndex, setQuestionIndex] = useState(0);
  const [selectedChoice, setSelectedChoice] = useState<number | null>(null);
  const [feedback, setFeedback] = useState<AnswerFeedback | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [checking, setChecking] = useState(false);
  const [error, setError] = useState("");
  const [audioMessage, setAudioMessage] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getLesson(slug, controller.signal).then(setLesson).catch((reason: unknown) => {
      if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Erro inesperado.");
    });
    return () => controller.abort();
  }, [slug]);

  const currentQuestion = lesson?.questions[questionIndex];
  const score = useMemo(() => lesson ? Math.round((correctCount / lesson.questions.length) * 100) : 0, [correctCount, lesson]);
  const passed = correctCount >= 2;

  function speakExample(slow = false) {
    if (!lesson) return;
    if (!("speechSynthesis" in window)) {
      setAudioMessage("Seu navegador não oferece áudio de referência.");
      return;
    }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(lesson.example);
    utterance.lang = "en-US";
    utterance.rate = slow ? 0.72 : 0.9;
    const englishVoice = window.speechSynthesis.getVoices().find((voice) => voice.lang.startsWith("en"));
    if (englishVoice) utterance.voice = englishVoice;
    utterance.onerror = () => setAudioMessage("Não foi possível reproduzir o áudio neste navegador.");
    setAudioMessage(slow ? "Reproduzindo devagar…" : "Reproduzindo exemplo…");
    window.speechSynthesis.speak(utterance);
  }

  async function submitAnswer() {
    if (!lesson || !currentQuestion || selectedChoice === null || checking) return;
    setChecking(true);
    setError("");
    try {
      const result = await checkAnswer(lesson.slug, currentQuestion.id, selectedChoice);
      setFeedback(result);
      if (result.isCorrect) setCorrectCount((count) => count + 1);
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Erro ao corrigir.");
    } finally {
      setChecking(false);
    }
  }

  function nextQuestion() {
    if (!lesson) return;
    if (questionIndex + 1 < lesson.questions.length) {
      setQuestionIndex((index) => index + 1);
      setSelectedChoice(null);
      setFeedback(null);
      setError("");
      return;
    }
    if (passed || correctCount >= 2) completeLesson(lesson.slug, Math.round(((correctCount) / lesson.questions.length) * 100));
    setStage("result");
  }

  function restart() {
    setStage("quiz");
    setQuestionIndex(0);
    setSelectedChoice(null);
    setFeedback(null);
    setCorrectCount(0);
    setError("");
  }

  if (error && !lesson) return <div className="student-error lesson-load-error" role="alert">{error}<br /><Link href="/app/learn">Voltar para a trilha</Link></div>;
  if (!lesson) return <div className="lesson-skeleton">Preparando sua missão…</div>;

  return (
    <div className="lesson-page">
      <div className="lesson-page-top">
        <Link href="/app/learn">← Voltar para a trilha</Link>
        <div className="lesson-stepper" aria-label={`Etapa ${stage === "theory" ? 1 : stage === "quiz" ? 2 : 3} de 3`}>
          <i className="is-active" /><i className={stage !== "theory" ? "is-active" : ""} /><i className={stage === "result" ? "is-active" : ""} />
        </div>
        <span>+{lesson.xpReward} XP</span>
      </div>

      {stage === "theory" ? (
        <article className="theory-card">
          <header><div><span>{lesson.unit} · {lesson.skill}</span><h1>{lesson.title}</h1><p>{lesson.summary}</p></div><small>{lesson.estimatedMinutes} minutos</small></header>
          <section className="theory-copy"><span className="lesson-section-number">01</span><div><h2>Entenda a ideia</h2><p>{lesson.theory}</p></div></section>
          <section className="example-box"><div><span>Exemplo em contexto</span><strong>{lesson.example}</strong></div><div className="audio-actions"><button type="button" onClick={() => speakExample(false)}>▶ Ouvir</button><button type="button" onClick={() => speakExample(true)}>½ Devagar</button></div></section>
          <p className="audio-message" aria-live="polite">{audioMessage}</p>
          <section className="key-points"><span className="lesson-section-number">02</span><div><h2>Guarde estes padrões</h2><ul>{lesson.keyPoints.map((point) => <li key={point}>✓ {point}</li>)}</ul></div></section>
          <footer><p>Você pode voltar à teoria durante a revisão.</p><button className="student-primary-button" type="button" onClick={() => setStage("quiz")}>Praticar agora →</button></footer>
        </article>
      ) : null}

      {stage === "quiz" && currentQuestion ? (
        <article className="quiz-card">
          <header><div><span>Desafio {questionIndex + 1} de {lesson.questions.length}</span><h1>{currentQuestion.prompt}</h1></div><strong>{correctCount} acerto{correctCount === 1 ? "" : "s"}</strong></header>
          <div className="quiz-progress"><i style={{ width: `${((questionIndex + (feedback ? 1 : 0)) / lesson.questions.length) * 100}%` }} /></div>
          <fieldset disabled={Boolean(feedback) || checking} className="choice-list">
            <legend className="sr-only">Escolha uma alternativa</legend>
            {currentQuestion.choices.map((choice, index) => {
              const state = feedback ? choice.id === feedback.correctChoiceId ? " is-correct" : choice.id === feedback.selectedChoiceId ? " is-wrong" : "" : selectedChoice === choice.id ? " is-selected" : "";
              return <label className={`choice-option${state}`} key={choice.id}><input type="radio" name="answer" value={choice.id} checked={selectedChoice === choice.id} onChange={() => setSelectedChoice(choice.id)} /><span>{String.fromCharCode(65 + index)}</span><strong>{choice.text}</strong></label>;
            })}
          </fieldset>

          {feedback ? <div className={`answer-feedback${feedback.isCorrect ? " is-correct" : " is-wrong"}`} role="status"><strong>{feedback.isCorrect ? "Nice work!" : "Quase lá — veja o padrão."}</strong><p>{feedback.explanation}</p></div> : null}
          {error ? <p className="inline-error" role="alert">{error}</p> : null}
          <footer><button className="lesson-secondary-button" type="button" onClick={() => setStage("theory")}>Rever teoria</button>{feedback ? <button className="student-primary-button" type="button" onClick={nextQuestion}>{questionIndex + 1 === lesson.questions.length ? "Ver resultado" : "Próxima pergunta"} →</button> : <button className="student-primary-button" type="button" disabled={selectedChoice === null || checking} onClick={submitAnswer}>{checking ? "Corrigindo…" : "Confirmar resposta"}</button>}</footer>
        </article>
      ) : null}

      {stage === "result" ? (
        <article className={`result-card${passed ? " is-passed" : ""}`}>
          <span className="result-symbol">{passed ? "✓" : "↻"}</span><p className="student-kicker">{passed ? "Mission complete" : "Vamos tentar mais uma vez"}</p><h1>{passed ? "Você concluiu a missão!" : "A prática faz parte da jornada."}</h1><p>{passed ? `Você acertou ${correctCount} de ${lesson.questions.length} e conquistou ${lesson.xpReward} XP neste modo demonstrativo.` : `Você acertou ${correctCount} de ${lesson.questions.length}. São necessários 2 acertos para concluir.`}</p>
          <div className="result-score"><div><strong>{score}%</strong><span>Seu resultado</span></div><div><strong>{correctCount}/{lesson.questions.length}</strong><span>Respostas corretas</span></div><div><strong>{passed ? `+${lesson.xpReward}` : "0"}</strong><span>XP</span></div></div>
          <div className="result-actions">{!passed ? <button className="lesson-secondary-button" type="button" onClick={restart}>Tentar novamente</button> : <Link className="lesson-secondary-button" href="/app/learn">Ver trilha</Link>}<Link className="student-primary-button" href="/app">Voltar ao painel →</Link></div>
        </article>
      ) : null}
    </div>
  );
}
