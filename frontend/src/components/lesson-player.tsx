"use client";

import Link from "next/link";
import { useEffect, useMemo, useState } from "react";

import { completeLesson, readProgress, recordLearningError } from "@/lib/demo-progress";
import {
  checkAnswer,
  getLesson,
  type AnswerFeedback,
  type AnswerPayload,
  type LearningAccess,
  type LessonDetail,
} from "@/lib/learning";

type Stage = "prepare" | "theory" | "quiz" | "production" | "result";
type Confidence = "practice" | "supported" | "independent";

export function LessonPlayer({ slug, courseSlug, basePath = "/app", access = "account" }: { slug: string; courseSlug?: string; basePath?: string; access?: LearningAccess }) {
  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [stage, setStage] = useState<Stage>("theory");
  const [questionIndex, setQuestionIndex] = useState(0);
  const [selectedChoice, setSelectedChoice] = useState<number | null>(null);
  const [textAnswer, setTextAnswer] = useState("");
  const [selectedTokenIndexes, setSelectedTokenIndexes] = useState<number[]>([]);
  const [feedback, setFeedback] = useState<AnswerFeedback | null>(null);
  const [correctCount, setCorrectCount] = useState(0);
  const [xpEarned, setXpEarned] = useState(0);
  const [checking, setChecking] = useState(false);
  const [error, setError] = useState("");
  const [audioMessage, setAudioMessage] = useState("");
  const [productionDraft, setProductionDraft] = useState("");
  const [confidence, setConfidence] = useState<Confidence | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    getLesson(slug, controller.signal, access).then((loadedLesson) => {
      setLesson(loadedLesson);
      setStage(loadedLesson.pedagogy ? "prepare" : "theory");
    }).catch((reason: unknown) => {
      if (!controller.signal.aborted) {
        setError(reason instanceof Error ? reason.message : "Erro inesperado.");
      }
    });
    return () => {
      controller.abort();
      window.speechSynthesis?.cancel();
    };
  }, [access, slug]);

  const currentQuestion = lesson?.questions[questionIndex];
  const score = useMemo(
    () => lesson ? Math.round((correctCount / lesson.questions.length) * 100) : 0,
    [correctCount, lesson],
  );
  const passed = Boolean(lesson && score >= lesson.passingPercent);
  const orderedTokens = currentQuestion?.tokens ?? [];
  const stages: Stage[] = lesson?.pedagogy
    ? ["prepare", "theory", "quiz", "production", "result"]
    : ["theory", "quiz", "result"];
  const stageIndex = stages.indexOf(stage);
  const pathHref = courseSlug ? `${basePath}/learn?course=${encodeURIComponent(courseSlug)}` : `${basePath}/learn`;
  const canSubmit = Boolean(currentQuestion && (
    (currentQuestion.type === "MCQ" && selectedChoice !== null)
    || (currentQuestion.type === "ORDERING" && orderedTokens.length > 0
      && selectedTokenIndexes.length === orderedTokens.length)
    || ((currentQuestion.type === "FILL_IN" || currentQuestion.type === "LISTENING")
      && textAnswer.trim())
  ));

  function speak(text: string, slow = false) {
    if (!("speechSynthesis" in window)) {
      setAudioMessage("Seu navegador não oferece áudio de referência.");
      return;
    }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    utterance.rate = slow ? 0.72 : 0.9;
    const englishVoice = window.speechSynthesis.getVoices().find(
      (voice) => voice.lang.startsWith("en"),
    );
    if (englishVoice) utterance.voice = englishVoice;
    utterance.onerror = () => setAudioMessage("Não foi possível reproduzir o áudio neste navegador.");
    utterance.onend = () => setAudioMessage("");
    setAudioMessage(slow ? "Reproduzindo devagar…" : "Reproduzindo áudio…");
    window.speechSynthesis.speak(utterance);
  }

  function resetAnswer() {
    setSelectedChoice(null);
    setTextAnswer("");
    setSelectedTokenIndexes([]);
    setFeedback(null);
    setError("");
    setAudioMessage("");
  }

  function answerPayload(): AnswerPayload {
    if (!currentQuestion) return {};
    if (currentQuestion.type === "MCQ") return { choiceId: selectedChoice ?? undefined };
    if (currentQuestion.type === "ORDERING") {
      return { order: selectedTokenIndexes.map((index) => orderedTokens[index]) };
    }
    return { answer: textAnswer };
  }

  async function submitAnswer() {
    if (!lesson || !currentQuestion || !canSubmit || checking) return;
    setChecking(true);
    setError("");
    try {
      const result = await checkAnswer(lesson.slug, currentQuestion.id, answerPayload(), access);
      setFeedback(result);
      if (result.isCorrect) setCorrectCount((count) => count + 1);
      else if (access === "demo" && result.errorCategory) {
        recordLearningError(lesson.slug, result.errorCategory);
      }
    } catch (reason) {
      setError(reason instanceof Error ? reason.message : "Erro ao corrigir.");
    } finally {
      setChecking(false);
    }
  }

  function finishLesson() {
    if (!lesson) return;
    if (passed && access === "demo") {
      const isReview = Boolean(readProgress().completed[lesson.slug]);
      const awarded = isReview ? 0 : lesson.xpReward;
      completeLesson(lesson.slug, score, awarded);
      setXpEarned(awarded);
    }
    setStage("result");
  }

  function nextQuestion() {
    if (!lesson) return;
    if (questionIndex + 1 < lesson.questions.length) {
      setQuestionIndex((index) => index + 1);
      resetAnswer();
      return;
    }
    if (passed && lesson.pedagogy) {
      setStage("production");
      return;
    }
    finishLesson();
  }

  function restart() {
    setStage("quiz");
    setQuestionIndex(0);
    setCorrectCount(0);
    setXpEarned(0);
    resetAnswer();
  }

  if (error && !lesson) {
    return <div className="student-error lesson-load-error" role="alert">{error}<br /><Link href={pathHref}>Voltar para a trilha</Link></div>;
  }
  if (!lesson) return <div className="lesson-skeleton">Preparando sua missão…</div>;

  return (
    <div className="lesson-page">
      <div className="lesson-page-top">
        <Link href={pathHref}>← Voltar para a trilha</Link>
        <div className="lesson-stepper" style={{ gridTemplateColumns: `repeat(${stages.length}, 1fr)` }} aria-label={`Etapa ${stageIndex + 1} de ${stages.length}`}>
          {stages.map((item, index) => <i className={index <= stageIndex ? "is-active" : ""} key={item} />)}
        </div>
        <span>{access === "demo" ? `+${lesson.xpReward} XP` : "Prática sem registro"}</span>
      </div>

      {stage === "prepare" && lesson.pedagogy ? (
        <article className="prepare-card">
          <span className="student-kicker">Antes de estudar</span>
          <h1>Ative o que você já sabe.</h1>
          <p>Faça uma tentativa sem consultar a explicação. Errar agora ajuda seu cérebro a perceber o que precisa aprender.</p>
          <div className="activation-prompt"><span>Seu primeiro desafio</span><strong>{lesson.pedagogy.activationPrompt}</strong></div>
          <div className="lesson-objective"><span>Meta da missão</span><p>{lesson.pedagogy.objective}</p></div>
          <footer><small>Não vale nota. Tente em voz alta ou mentalmente.</small><button className="student-primary-button" type="button" onClick={() => setStage("theory")}>Ver explicação →</button></footer>
        </article>
      ) : null}

      {stage === "theory" ? (
        <article className="theory-card">
          <header><div><span>{lesson.unit} · {lesson.skill}</span><h1>{lesson.title}</h1><p>{lesson.summary}</p></div><small>{lesson.estimatedMinutes} minutos</small></header>
          {lesson.pedagogy ? <div className="lesson-objective"><span>Ao final, você será capaz de</span><p>{lesson.pedagogy.objective}</p></div> : null}
          <section className="theory-copy"><span className="lesson-section-number">01</span><div><h2>Entenda a ideia</h2><p>{lesson.theory}</p></div></section>
          <section className="example-box"><div><span>Exemplo em contexto</span><strong>{lesson.example}</strong></div><div className="audio-actions"><button type="button" onClick={() => speak(lesson.example)}>▶ Ouvir</button><button type="button" onClick={() => speak(lesson.example, true)}>½ Devagar</button></div></section>
          <p className="audio-message" aria-live="polite">{audioMessage}</p>
          {lesson.dialogue?.length ? (
            <section className="dialogue-section">
              <div><span className="lesson-section-number">02</span><h2>Conversa em contexto</h2></div>
              <div className="dialogue-lines">
                {lesson.dialogue.map((item, index) => (
                  <div className="dialogue-line" key={`${item.speaker}-${index}`}>
                    <strong>{item.speaker}</strong><p>{item.line}</p>
                    <button type="button" aria-label={`Ouvir fala de ${item.speaker}`} onClick={() => speak(item.line)}>▶</button>
                  </div>
                ))}
              </div>
            </section>
          ) : null}
          <section className="key-points"><span className="lesson-section-number">{lesson.dialogue?.length ? "03" : "02"}</span><div><h2>Guarde estes padrões</h2><ul>{lesson.keyPoints.map((point) => <li key={point}>✓ {point}</li>)}</ul></div></section>
          {lesson.pedagogy ? <section className="common-mistakes"><h2>Armadilhas comuns</h2><ul>{lesson.pedagogy.commonMistakes.map((mistake) => <li key={mistake}>{mistake}</li>)}</ul></section> : null}
          <footer><p>Você pode voltar à teoria durante a revisão.</p><button className="student-primary-button" type="button" onClick={() => setStage("quiz")}>Praticar agora →</button></footer>
        </article>
      ) : null}

      {stage === "production" && lesson.pedagogy ? (
        <article className="production-card">
          <span className="student-kicker">Agora use o inglês</span>
          <h1>{lesson.pedagogy.productionTask.mode === "SPEAKING" ? "Fale com suas próprias palavras." : "Escreva com suas próprias palavras."}</h1>
          <p>{lesson.pedagogy.productionTask.prompt}</p>
          <div className="production-model"><span>Modelo — consulte só se precisar</span><p>{lesson.pedagogy.productionTask.model}</p><button type="button" onClick={() => speak(lesson.pedagogy?.productionTask.model ?? "")}>▶ Ouvir modelo</button></div>
          <label className="production-draft"><span>{lesson.pedagogy.productionTask.mode === "SPEAKING" ? "Anote palavras-chave para apoiar sua fala (opcional)" : "Escreva sua resposta"}</span><textarea value={productionDraft} onChange={(event) => setProductionDraft(event.target.value)} rows={5} /></label>
          <div className="production-checklist"><strong>Confira antes de terminar</strong><ul>{lesson.pedagogy.productionTask.checklist.map((item) => <li key={item}>□ {item}</li>)}</ul></div>
          <fieldset className="confidence-check"><legend>Como você realizou a tarefa?</legend>
            <label><input type="radio" name="confidence" checked={confidence === "practice"} onChange={() => setConfidence("practice")} /> Ainda preciso praticar</label>
            <label><input type="radio" name="confidence" checked={confidence === "supported"} onChange={() => setConfidence("supported")} /> Consegui com apoio</label>
            <label><input type="radio" name="confidence" checked={confidence === "independent"} onChange={() => setConfidence("independent")} /> Consegui sozinho</label>
          </fieldset>
          <footer><button className="lesson-secondary-button" type="button" onClick={() => setStage("theory")}>Rever conteúdo</button><button className="student-primary-button" type="button" disabled={!confidence || (lesson.pedagogy.productionTask.mode === "WRITING" && !productionDraft.trim())} onClick={finishLesson}>Concluir missão →</button></footer>
        </article>
      ) : null}

      {stage === "quiz" && currentQuestion ? (
        <article className="quiz-card">
          <header><div><span>Desafio {questionIndex + 1} de {lesson.questions.length} · {questionTypeLabel(currentQuestion.type)}</span><h1>{currentQuestion.prompt}</h1></div><strong>{correctCount} acerto{correctCount === 1 ? "" : "s"}</strong></header>
          <div className="quiz-progress"><i style={{ width: `${((questionIndex + (feedback ? 1 : 0)) / lesson.questions.length) * 100}%` }} /></div>

          {currentQuestion.type === "MCQ" ? (
            <fieldset disabled={Boolean(feedback) || checking} className="choice-list">
              <legend className="sr-only">Escolha uma alternativa</legend>
              {(currentQuestion.choices ?? []).map((choice, index) => {
                const state = feedback ? choice.id === feedback.correctChoiceId ? " is-correct" : choice.id === feedback.selectedChoiceId ? " is-wrong" : "" : selectedChoice === choice.id ? " is-selected" : "";
                return <label className={`choice-option${state}`} key={choice.id}><input type="radio" name="answer" value={choice.id} checked={selectedChoice === choice.id} onChange={() => setSelectedChoice(choice.id)} /><span>{String.fromCharCode(65 + index)}</span><strong>{choice.text}</strong></label>;
              })}
            </fieldset>
          ) : null}

          {currentQuestion.type === "FILL_IN" ? (
            <label className="text-answer"><span>Digite a palavra ou expressão que completa a frase</span><input autoComplete="off" disabled={Boolean(feedback) || checking} value={textAnswer} onChange={(event) => setTextAnswer(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter") void submitAnswer(); }} /></label>
          ) : null}

          {currentQuestion.type === "LISTENING" ? (
            <div className="listening-answer">
              <div className="listening-actions"><button type="button" disabled={checking} onClick={() => speak(currentQuestion.audioText ?? "")}>▶ Ouvir frase</button><button type="button" disabled={checking} onClick={() => speak(currentQuestion.audioText ?? "", true)}>½ Mais devagar</button></div>
              <label className="text-answer"><span>Escreva exatamente o que você ouviu</span><input autoComplete="off" disabled={Boolean(feedback) || checking} value={textAnswer} onChange={(event) => setTextAnswer(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter") void submitAnswer(); }} /></label>
              <p className="audio-message" aria-live="polite">{audioMessage}</p>
            </div>
          ) : null}

          {currentQuestion.type === "ORDERING" ? (
            <div className="ordering-answer">
              <div className="ordered-tokens" aria-label="Sua frase">
                {selectedTokenIndexes.length ? selectedTokenIndexes.map((tokenIndex) => <button type="button" disabled={Boolean(feedback) || checking} key={tokenIndex} onClick={() => setSelectedTokenIndexes((indexes) => indexes.filter((index) => index !== tokenIndex))}>{orderedTokens[tokenIndex]}</button>) : <span>Toque nas palavras para montar a frase.</span>}
              </div>
              <div className="token-bank" aria-label="Palavras disponíveis">
                {orderedTokens.map((token, tokenIndex) => <button type="button" disabled={Boolean(feedback) || checking || selectedTokenIndexes.includes(tokenIndex)} key={`${token}-${tokenIndex}`} onClick={() => setSelectedTokenIndexes((indexes) => [...indexes, tokenIndex])}>{token}</button>)}
              </div>
            </div>
          ) : null}

          {feedback ? <div className={`answer-feedback${feedback.isCorrect ? " is-correct" : " is-wrong"}`} role="status"><strong>{feedback.isCorrect ? "Nice work!" : "Quase lá — veja o padrão."}</strong>{!feedback.isCorrect && feedback.correctAnswer ? <p>Resposta: <b>{feedback.correctAnswer}</b></p> : null}<p>{feedback.explanation}</p></div> : null}
          {error ? <p className="inline-error" role="alert">{error}</p> : null}
          <footer><button className="lesson-secondary-button" type="button" onClick={() => setStage("theory")}>Rever teoria</button>{feedback ? <button className="student-primary-button" type="button" onClick={nextQuestion}>{questionIndex + 1 === lesson.questions.length ? "Ver resultado" : "Próxima pergunta"} →</button> : <button className="student-primary-button" type="button" disabled={!canSubmit || checking} onClick={submitAnswer}>{checking ? "Corrigindo…" : "Confirmar resposta"}</button>}</footer>
        </article>
      ) : null}

      {stage === "result" ? (
        <article className={`result-card${passed ? " is-passed" : ""}`}>
          <span className="result-symbol">{passed ? "✓" : "↻"}</span><p className="student-kicker">{passed ? "Mission complete" : "Vamos tentar mais uma vez"}</p><h1>{passed ? "Você concluiu a prática!" : "A prática faz parte da jornada."}</h1><p>{passed ? access === "account" ? `Você acertou ${correctCount} de ${lesson.questions.length}. Tentativas e XP serão associados à conta na próxima etapa do desenvolvimento.` : xpEarned > 0 ? `Você acertou ${correctCount} de ${lesson.questions.length} e conquistou ${xpEarned} XP.` : `Você acertou ${correctCount} de ${lesson.questions.length}. Revisão concluída sem XP adicional.` : `Você acertou ${correctCount} de ${lesson.questions.length}. É preciso atingir ${lesson.passingPercent}% para concluir.`}</p>
          <div className="result-score"><div><strong>{score}%</strong><span>Seu resultado</span></div><div><strong>{correctCount}/{lesson.questions.length}</strong><span>Respostas corretas</span></div><div><strong>{access === "demo" ? `+${xpEarned}` : "—"}</strong><span>XP</span></div></div>
          {passed && lesson.pedagogy ? <section className="review-prompts"><h2>Retome depois, sem consultar</h2><p>Use estas perguntas amanhã e novamente em alguns dias.</p><ul>{lesson.pedagogy.reviewPrompts.map((prompt) => <li key={prompt}>{prompt}</li>)}</ul></section> : null}
          <div className="result-actions">{!passed ? <button className="lesson-secondary-button" type="button" onClick={restart}>Tentar novamente</button> : <Link className="lesson-secondary-button" href={pathHref}>Ver trilha</Link>}<Link className="student-primary-button" href={basePath}>Voltar ao painel →</Link></div>
        </article>
      ) : null}
    </div>
  );
}

function questionTypeLabel(type: LessonDetail["questions"][number]["type"]) {
  return {
    MCQ: "Múltipla escolha",
    FILL_IN: "Complete a lacuna",
    ORDERING: "Monte a frase",
    LISTENING: "Ditado",
  }[type];
}
