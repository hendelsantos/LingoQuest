import Image from "next/image";
import Link from "next/link";

import { site } from "@/lib/site";

const pillars = [
  {
    number: "01",
    title: "Aprenda em missões",
    description:
      "Teoria curta, exemplos claros e prática com feedback imediato — no seu ritmo.",
  },
  {
    number: "02",
    title: "Pratique com propósito",
    description:
      "Cada desafio prepara você para situações reais de conversa, trabalho e viagem.",
  },
  {
    number: "03",
    title: "Evolua com um professor",
    description:
      "Uma aula semanal transforma seus dados de progresso em orientação humana.",
  },
];

export default function Home() {
  return (
    <main>
      <header className="site-header">
        <Link className="brand" href="/" aria-label="LingoQuest — início">
          <Image src="/brand/logo-mark.svg" alt="" width={38} height={38} priority />
          <span>
            <strong>LingoQuest</strong>
            <small>English Academy</small>
          </span>
        </Link>

        <nav aria-label="Navegação principal">
          <a href="#metodo">Como funciona</a>
          <a href="#planos">Planos</a>
          <a className="button button-ghost" href="#planos">
            Primeira turma
          </a>
        </nav>
      </header>

      <section className="hero">
        <div className="hero-copy">
          <span className="eyebrow">Inglês para a vida real</span>
          <h1>
            Pequenos passos.
            <br />
            <em>Grandes aventuras.</em>
          </h1>
          <p>
            Aprenda inglês com missões que fazem sentido e uma hora por semana
            com um professor que acompanha de verdade a sua evolução.
          </p>
          <div className="hero-actions">
            <a className="button button-primary" href="#planos">
              Quero começar
            </a>
            <a className="text-link" href="#metodo">
              Conhecer o método <span aria-hidden="true">↓</span>
            </a>
          </div>
          <div className="trust-row" aria-label="Características do programa">
            <span>✓ Aulas ao vivo</span>
            <span>✓ Progresso real</span>
            <span>✓ Sem infantilização</span>
          </div>
        </div>

        <div className="hero-visual" aria-label="Finn, o guia digital da LingoQuest">
          <div className="mission-card mission-card-top">
            <span>Próxima missão</span>
            <strong>The Verb To Be</strong>
            <small>8 min · +60 XP</small>
          </div>
          <Image
            src="/characters/finn-welcome.svg"
            alt="Finn, um pequeno explorador digital verde, acenando"
            width={420}
            height={430}
            priority
          />
          <div className="mission-card mission-card-bottom">
            <span>Seu progresso</span>
            <strong>Keep going!</strong>
            <div className="progress-track" aria-label="Progresso de exemplo: 37%">
              <i style={{ width: "37%" }} />
            </div>
          </div>
        </div>
      </section>

      <section className="method" id="metodo" aria-labelledby="method-title">
        <div className="section-heading">
          <span className="eyebrow">Um ciclo que funciona</span>
          <h2 id="method-title">Tecnologia para praticar. Gente para orientar.</h2>
          <p>
            A plataforma organiza a rotina; o professor usa o progresso para
            tornar cada encontro mais útil.
          </p>
        </div>
        <div className="pillar-grid">
          {pillars.map((pillar) => (
            <article key={pillar.number}>
              <span>{pillar.number}</span>
              <h3>{pillar.title}</h3>
              <p>{pillar.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="early-access" id="planos">
        <div>
          <span className="eyebrow">Primeira turma</span>
          <h2>Estamos construindo a experiência {site.name}.</h2>
          <p>
            Os planos comerciais ainda serão validados no piloto. Entre em
            contato para participar da primeira turma, sem promessas artificiais
            ou cobrança antes da hora.
          </p>
        </div>
        <span className="button button-light" aria-label="Inscrições ainda não abertas">
          Inscrições em breve
        </span>
      </section>

      <footer>
        <div className="brand brand-footer">
          <Image src="/brand/logo-mark.svg" alt="" width={32} height={32} />
          <span>
            <strong>LingoQuest</strong>
            <small>{site.tagline}</small>
          </span>
        </div>
        <p>© 2026 MH Software. Produto em desenvolvimento.</p>
      </footer>
    </main>
  );
}
