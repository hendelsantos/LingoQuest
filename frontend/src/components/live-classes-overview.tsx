import Link from "next/link";

export function LiveClassesOverview({ basePath = "/app" }: { basePath?: string }) {
  return (
    <div className="live-classes-page">
      <header className="live-classes-hero">
        <div>
          <span className="student-kicker">Acompanhamento humano</span>
          <h1>Aulas ao vivo</h1>
          <p>Pratique conversação, tire dúvidas e transforme os resultados das missões em um plano de estudo com seu professor.</p>
        </div>
        <div className="live-hero-stat"><strong>1h</strong><span>de encontro semanal no plano Mentor</span></div>
      </header>
      <section className="live-next-session" aria-labelledby="next-class-title">
        <div className="session-date"><strong>TESTE</strong><span>disponível agora</span></div>
        <div className="session-details">
          <span className="classroom-kicker">Sala demonstrativa</span>
          <h2 id="next-class-title">Introductions &amp; verb to be</h2>
          <p>Teste seus dispositivos e faça uma atividade dentro da sala. Nenhum professor remoto será conectado nesta demonstração.</p>
          <div><span>◷ 50 minutos</span><span>◎ Individual</span><span>◇ A1 Foundations</span></div>
        </div>
        <Link className="student-primary-button" href={`${basePath}/live/demo`}>Entrar na sala →</Link>
      </section>
      <div className="live-page-grid">
        <section className="live-how-it-works">
          <div className="student-section-heading"><div><h2>Como funciona</h2><p>Antes, durante e depois do encontro</p></div></div>
          <div className="live-feature-grid">
            <article><span>01</span><h3>Prepare-se</h3><p>A plataforma reúne suas dúvidas e os erros das missões recentes.</p></article>
            <article><span>02</span><h3>Pratique ao vivo</h3><p>Converse com o professor e resolva atividades na mesma tela.</p></article>
            <article><span>03</span><h3>Continue evoluindo</h3><p>Receba feedback, vocabulário e uma tarefa clara para a semana.</p></article>
          </div>
        </section>
        <aside className="live-readiness-card">
          <span className="classroom-kicker">Nesta versão</span>
          <h2>Laboratório da sala</h2>
          <ul>
            <li><span>✓</span> Câmera e microfone reais</li>
            <li><span>✓</span> Controles de mídia</li>
            <li><span>✓</span> Exercício interativo</li>
            <li><span>✓</span> Notas locais</li>
            <li className="is-planned"><span>→</span> Professor remoto via LiveKit</li>
          </ul>
          <p>A videoconferência entre contas será ativada após autenticação, agenda e autorização no backend.</p>
        </aside>
      </div>
    </div>
  );
}
