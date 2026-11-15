"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";

import { checkClassroomAnswer, demoClassroomExercise } from "@/lib/live-classroom";

type MediaStatus = "idle" | "requesting" | "ready" | "error";

export function LiveClassroomDemo() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const [mediaStatus, setMediaStatus] = useState<MediaStatus>("idle");
  const [mediaError, setMediaError] = useState("");
  const [cameraEnabled, setCameraEnabled] = useState(true);
  const [microphoneEnabled, setMicrophoneEnabled] = useState(true);
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [answerChecked, setAnswerChecked] = useState(false);
  const [notes, setNotes] = useState("");
  const [notesSaved, setNotesSaved] = useState(false);

  const answerIsCorrect = answerChecked
    ? checkClassroomAnswer(demoClassroomExercise, selectedAnswer)
    : false;

  function stopMedia() {
    streamRef.current?.getTracks().forEach((track) => track.stop());
    streamRef.current = null;
    if (videoRef.current) videoRef.current.srcObject = null;
    setMediaStatus("idle");
    setCameraEnabled(true);
    setMicrophoneEnabled(true);
  }

  useEffect(() => {
    return () => streamRef.current?.getTracks().forEach((track) => track.stop());
  }, []);

  async function startMedia() {
    if (!navigator.mediaDevices?.getUserMedia) {
      setMediaError("Este navegador não oferece acesso seguro à câmera e ao microfone.");
      setMediaStatus("error");
      return;
    }

    setMediaStatus("requesting");
    setMediaError("");

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      streamRef.current = stream;
      if (videoRef.current) videoRef.current.srcObject = stream;
      setCameraEnabled(stream.getVideoTracks().some((track) => track.enabled));
      setMicrophoneEnabled(stream.getAudioTracks().some((track) => track.enabled));
      setMediaStatus("ready");
    } catch (reason: unknown) {
      const denied = reason instanceof DOMException && reason.name === "NotAllowedError";
      setMediaError(
        denied
          ? "Permissão negada. Libere câmera e microfone nas configurações do navegador para testar a sala."
          : "Não foi possível iniciar seus dispositivos. Verifique se outra aplicação está usando a câmera.",
      );
      setMediaStatus("error");
    }
  }

  function toggleTrack(kind: "audio" | "video") {
    const tracks = kind === "audio"
      ? streamRef.current?.getAudioTracks()
      : streamRef.current?.getVideoTracks();
    if (!tracks?.length) return;
    const enabled = !tracks[0].enabled;
    tracks.forEach((track) => { track.enabled = enabled; });
    if (kind === "audio") setMicrophoneEnabled(enabled);
    else setCameraEnabled(enabled);
  }

  function checkAnswer() {
    if (!selectedAnswer) return;
    setAnswerChecked(true);
  }

  function saveNotes() {
    if (!notes.trim()) return;
    window.localStorage.setItem("lingoquest:classroom-demo-notes", notes);
    setNotesSaved(true);
    window.setTimeout(() => setNotesSaved(false), 2200);
  }

  return (
    <div className="classroom-page">
      <header className="classroom-header">
        <div>
          <Link href="/app/live">← Voltar para aulas</Link>
          <span className="classroom-kicker">Sala de demonstração</span>
          <h1>Introductions &amp; verb to be</h1>
        </div>
        <div className="classroom-session-meta">
          <span><i /> Laboratório disponível</span>
          <strong>50 minutos</strong>
          <small>Professor ainda não conectado</small>
        </div>
      </header>

      <div className="classroom-notice" role="status">
        <strong>Teste de experiência:</strong> sua câmera é real e permanece no navegador. A conexão
        com outro participante será habilitada com contas autenticadas e LiveKit.
      </div>

      <section className="classroom-layout">
        <div className="classroom-video-column">
          <div className="video-stage">
            <article className={`video-tile local-video${mediaStatus === "ready" && !cameraEnabled ? " is-camera-off" : ""}`}>
              <video ref={videoRef} autoPlay muted playsInline aria-label="Prévia da sua câmera" />
              {mediaStatus !== "ready" || !cameraEnabled ? (
                <div className="video-placeholder">
                  <span>AV</span>
                  <strong>{mediaStatus === "requesting" ? "Iniciando dispositivos…" : "Aluno visitante"}</strong>
                  <small>{cameraEnabled ? "Câmera ainda não ativada" : "Câmera desligada"}</small>
                </div>
              ) : null}
              <span className="participant-label">Você · aluno</span>
            </article>

            <article className="video-tile remote-video">
              <div className="video-placeholder">
                <span>PR</span>
                <strong>Aguardando professor</strong>
                <small>Nenhum participante remoto conectado</small>
              </div>
              <span className="participant-label">Professor</span>
            </article>
          </div>

          {mediaError ? <p className="classroom-media-error" role="alert">{mediaError}</p> : null}

          <div className="classroom-controls" aria-label="Controles da sala">
            {mediaStatus !== "ready" ? (
              <button className="classroom-enter-button" disabled={mediaStatus === "requesting"} onClick={startMedia}>
                {mediaStatus === "requesting" ? "Solicitando permissão…" : "Ativar câmera e microfone"}
              </button>
            ) : (
              <>
                <button
                  aria-pressed={!microphoneEnabled}
                  className={!microphoneEnabled ? "is-off" : ""}
                  onClick={() => toggleTrack("audio")}
                >
                  {microphoneEnabled ? "◉ Microfone ligado" : "○ Microfone desligado"}
                </button>
                <button
                  aria-pressed={!cameraEnabled}
                  className={!cameraEnabled ? "is-off" : ""}
                  onClick={() => toggleTrack("video")}
                >
                  {cameraEnabled ? "▣ Câmera ligada" : "□ Câmera desligada"}
                </button>
                <button className="leave-class-button" onClick={stopMedia}>Encerrar teste</button>
              </>
            )}
          </div>

          <div className="classroom-agenda-card">
            <div>
              <span className="classroom-kicker">Plano da aula</span>
              <h2>Apresentar-se com confiança</h2>
            </div>
            <ol>
              <li><span>01</span><div><strong>Warm-up</strong><small>Nome, cidade e profissão · 10 min</small></div></li>
              <li className="is-current"><span>02</span><div><strong>Verb to be</strong><small>Frases essenciais · 15 min</small></div></li>
              <li><span>03</span><div><strong>Guided conversation</strong><small>Prática com perguntas · 20 min</small></div></li>
              <li><span>04</span><div><strong>Feedback</strong><small>Próximos passos · 5 min</small></div></li>
            </ol>
          </div>
        </div>

        <aside className="classroom-workspace-panel">
          <div className="workspace-panel-heading">
            <div>
              <span className="classroom-kicker">Atividade compartilhada</span>
              <h2>Check-in rápido</h2>
            </div>
            <span className="demo-tag">Demonstração</span>
          </div>

          <div className="classroom-exercise">
            <p>{demoClassroomExercise.instruction}</p>
            <strong>{demoClassroomExercise.prompt}</strong>
            <fieldset disabled={answerChecked}>
              <legend className="sr-only">Escolha a palavra correta</legend>
              {demoClassroomExercise.options.map((option) => (
                <label className={selectedAnswer === option ? "is-selected" : ""} key={option}>
                  <input
                    checked={selectedAnswer === option}
                    name="classroom-answer"
                    onChange={() => setSelectedAnswer(option)}
                    type="radio"
                    value={option}
                  />
                  <span>{option}</span>
                </label>
              ))}
            </fieldset>

            {answerChecked ? (
              <div className={`classroom-answer-feedback ${answerIsCorrect ? "is-correct" : "is-wrong"}`} role="status">
                <strong>{answerIsCorrect ? "Resposta correta" : "Vamos revisar"}</strong>
                <p>{demoClassroomExercise.explanation}</p>
                <button onClick={() => { setAnswerChecked(false); setSelectedAnswer(""); }}>Tentar novamente</button>
              </div>
            ) : (
              <button className="student-primary-button" disabled={!selectedAnswer} onClick={checkAnswer}>
                Conferir resposta
              </button>
            )}
          </div>

          <div className="classroom-notes">
            <div>
              <span className="classroom-kicker">Minhas notas</span>
              <small>Privadas neste navegador</small>
            </div>
            <label htmlFor="class-notes">Anote uma palavra ou dúvida da aula</label>
            <textarea
              id="class-notes"
              onChange={(event) => { setNotes(event.target.value); setNotesSaved(false); }}
              placeholder="Ex.: I am from Brazil. / Quando usar are?"
              rows={4}
              value={notes}
            />
            <button disabled={!notes.trim()} onClick={saveNotes}>{notesSaved ? "Nota salva ✓" : "Salvar neste navegador"}</button>
          </div>
        </aside>
      </section>
    </div>
  );
}
