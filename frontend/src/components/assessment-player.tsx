"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import {
  readProgress,
  recordLearningError,
  saveAssessment,
  type AssessmentMoment,
} from "@/lib/demo-progress";
import {
  checkAssessmentAnswer,
  getAssessment,
  type AssessmentDetail,
  type AssessmentFeedback,
} from "@/lib/learning";

type Stage = "intro" | "quiz" | "production" | "result";
type Confidence = "practice" | "supported" | "independent";

export function AssessmentPlayer({
  moment,
  basePath = "/app",
}: {
  moment: AssessmentMoment;
  basePath?: string;
}) {
  const [assessment, setAssessment] = useState<AssessmentDetail | null>(null);
  const [stage, setStage] = useState<Stage>("intro");
  const [questionIndex, setQuestionIndex] = useState(0);
  const [choiceIndex, setChoiceIndex] = useState<number | null>(null);
  const [textAnswer, setTextAnswer] = useState("");
  const [selectedTokens, setSelectedTokens] = useState<number[]>([]);
  const [feedback, setFeedback] = useState<AssessmentFeedback | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [writingSample, setWritingSample] = useState("");
  const [confidence, setConfidence] = useState<Confidence | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const controller = new AbortController();
    getAssessment(moment, controller.signal).then(setAssessment).catch((reason: unknown) => {
      if (!controller.signal.aborted) setError(reason instanceof Error ? reason.message : "Erro inesperado.");
    });
    return () => controller.abort();
  }, [moment]);

  const question = assessment?.questions[questionIndex];
  const tokens = question?.tokens ?? [];
  const score = useMemo(
    () => assessment ? Math.round((correctCount / assessment.questions.length) * 100) : 0,
    [assessment, correctCount],
  );
  const canSubmit = Boolean(question && (
    (question.type === "MCQ" && choiceIndex !== null)
    || (question.type === "ORDERING" && selectedTokens.length === tokens.length)
    || ((question.type === "FILL_IN" || question.type === "LISTENING") && textAnswer.trim())
  ));

  function speak(text: string) {
    if (!("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = 0.88;
    window.speechSynthesis.speak(utterance);
  }

  function resetAnswer() {
    setChoiceIndex(null);
    setTextAnswer("");
    setSelectedTokens([]);
    setFeedback(null);
  }

  async function submitAnswer() {
    if (!assessment || !question || !canSubmit || busy) return;
    setBusy(true);
    setError("");
    try {
      const result = await checkAssessmentAnswer(moment, {
        questionId: question.id,
        choiceIndex: choiceIndex ?? undefined,
        answer: textAnswer,
        order: selectedTokens.map((index) => tokens[index]),
      });
      setFeedback(result);
      if (result.isCorrect) setCorrectCount((count) => count + 1);
      else if (result.errorCategory) recordLearningError(`assessment-${moment}`, result.errorCategory);
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Erro ao corrigir.");
    } finally {
      setBusy(false);
    }
  }

  function nextQuestion() {
    if (!assessment) return;
    if (questionIndex + 1 < assessment.questions.length) {
      setQuestionIndex((index) => index + 1);
      resetAnswer();
    } else {
      setStage("production");
    }
  }

  function finishAssessment() {
    if (!assessment || !confidence || !writingSample.trim()) return;
    saveAssessment(moment, {
      score,
      correctCount,
      totalQuestions: assessment.questions.length,
      confidence,
      writingSample: writingSample.trim(),
    });
    setStage("result");
  }

  if (!assessment) return <div className="lesson-skeleton">{error || "Preparando avaliação…"}</div>;

  const initial = readProgress().assessments.initial;
  const delta = moment === "final" && initial ? score - initial.score : null;

  return (
    <div className="assessment-page">
      {stage === "intro" ? <article className="assessment-intro">
        <span className="student-kicker">Avaliação pedagógica</span>
        <h1>{assessment.title}</h1>
        <p>{assessment.description}</p>
        <div className="assessment-notice"><strong>O que este resultado significa?</strong><p>Ele compara habilidades equivalentes e ajuda a planejar o estudo. Não é prova oficial, diagnóstico clínico nem certificação CEFR.</p></div>
        <button className="student-primary-button" type="button" onClick={() => setStage("quiz")}>Começar avaliação →</button>
      </article> : null}

      {stage === "quiz" && question ? <article className="quiz-card">
        <header><div><span>Questão {questionIndex + 1} de {assessment.questions.length}</span><h1>{question.prompt}</h1></div><strong>{correctCount} acerto{correctCount === 1 ? "" : "s"}</strong></header>
        <div className="quiz-progress"><i style={{ width: `${((questionIndex + (feedback ? 1 : 0)) / assessment.questions.length) * 100}%` }} /></div>
        {question.type === "MCQ" ? <fieldset className="choice-list" disabled={Boolean(feedback) || busy}><legend className="sr-only">Escolha uma alternativa</legend>{question.choices?.map((choice, index) => {
          const state = feedback ? index === feedback.correctChoiceIndex ? " is-correct" : index === choiceIndex ? " is-wrong" : "" : index === choiceIndex ? " is-selected" : "";
          return <label className={`choice-option${state}`} key={choice}><input type="radio" checked={choiceIndex === index} onChange={() => setChoiceIndex(index)} /><span>{String.fromCharCode(65 + index)}</span><strong>{choice}</strong></label>;
        })}</fieldset> : null}
        {question.type === "FILL_IN" ? <label className="text-answer"><span>Digite a palavra ou expressão</span><input disabled={Boolean(feedback) || busy} value={textAnswer} onChange={(event) => setTextAnswer(event.target.value)} /></label> : null}
        {question.type === "LISTENING" ? <div className="listening-answer"><div className="listening-actions"><button type="button" onClick={() => speak(question.audioText ?? "")}>▶ Ouvir frase</button></div><label className="text-answer"><span>Escreva o que ouviu</span><input disabled={Boolean(feedback) || busy} value={textAnswer} onChange={(event) => setTextAnswer(event.target.value)} /></label></div> : null}
        {question.type === "ORDERING" ? <div className="ordering-answer"><div className="ordered-tokens">{selectedTokens.length ? selectedTokens.map((tokenIndex) => <button type="button" disabled={Boolean(feedback)} key={tokenIndex} onClick={() => setSelectedTokens((selected) => selected.filter((index) => index !== tokenIndex))}>{tokens[tokenIndex]}</button>) : <span>Monte a frase.</span>}</div><div className="token-bank">{tokens.map((token, index) => <button type="button" key={`${token}-${index}`} disabled={Boolean(feedback) || selectedTokens.includes(index)} onClick={() => setSelectedTokens((selected) => [...selected, index])}>{token}</button>)}</div></div> : null}
        {feedback ? <div className={`answer-feedback${feedback.isCorrect ? " is-correct" : " is-wrong"}`}><strong>{feedback.isCorrect ? "Resposta adequada" : "Veja o padrão"}</strong>{!feedback.isCorrect && feedback.correctAnswer ? <p>Resposta: <b>{feedback.correctAnswer}</b></p> : null}<p>{feedback.explanation}</p></div> : null}
        {error ? <p className="inline-error">{error}</p> : null}
        <footer>{feedback ? <button className="student-primary-button" type="button" onClick={nextQuestion}>{questionIndex + 1 === assessment.questions.length ? "Ir para produção" : "Próxima questão"} →</button> : <button className="student-primary-button" type="button" disabled={!canSubmit || busy} onClick={submitAnswer}>Confirmar resposta</button>}</footer>
      </article> : null}

      {stage === "production" ? <article className="assessment-production">
        <span className="student-kicker">Produção autoral</span><h1>Agora use o inglês sem alternativas.</h1>
        <section><h2>Fala</h2><p>{assessment.speakingTask}</p><small>Faça a tarefa em voz alta. Nesta versão, a plataforma não grava nem atribui nota automática à pronúncia.</small></section>
        <label><span>Escrita</span><p>{assessment.writingTask}</p><textarea rows={7} value={writingSample} onChange={(event) => setWritingSample(event.target.value)} /></label>
        <fieldset className="confidence-check"><legend>Quanto apoio você precisou?</legend><label><input type="radio" name="assessment-confidence" onChange={() => setConfidence("practice")} /> Ainda preciso praticar</label><label><input type="radio" name="assessment-confidence" onChange={() => setConfidence("supported")} /> Consegui com apoio</label><label><input type="radio" name="assessment-confidence" onChange={() => setConfidence("independent")} /> Consegui sozinho</label></fieldset>
        <button className="student-primary-button" type="button" disabled={!confidence || !writingSample.trim()} onClick={finishAssessment}>Finalizar avaliação →</button>
      </article> : null}

      {stage === "result" ? <article className="result-card is-passed"><span className="result-symbol">✓</span><p className="student-kicker">Avaliação concluída</p><h1>{score}% nas questões objetivas</h1><p>O texto e a fala precisam de observação humana para uma avaliação completa.</p><div className="result-score"><div><strong>{correctCount}/{assessment.questions.length}</strong><span>Respostas corretas</span></div><div><strong>{confidence === "independent" ? "Sozinho" : confidence === "supported" ? "Com apoio" : "Praticar"}</strong><span>Autoavaliação</span></div><div><strong>{delta === null ? "Base" : `${delta >= 0 ? "+" : ""}${delta}`}</strong><span>{delta === null ? "Ponto inicial" : "Variação"}</span></div></div><div className="result-actions"><Link className="student-primary-button" href={basePath}>Voltar ao painel →</Link></div></article> : null}
    </div>
  );
}
