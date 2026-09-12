import Link from "next/link";
import { PhaseBar } from "@/components/PhaseBar";
import { Ultradian } from "@/components/Ultradian";
import { gql, HOME_QUERY } from "@/lib/gql";
import { ART, asset } from "@/lib/art";
import type { CyclePhase, Note, ProtocolStep } from "@/lib/cycle";

type HomeData = {
  cycle: { phase: CyclePhase; ultradianMinutes: number; nextRestInMinutes: number; protocol: ProtocolStep[] };
  cluster: { title: string; notes: Note[] };
  llmFrontier: Note[];
  dueRetrievals: Note[];
  brain: { neurons: number; synapses: number; meanWeight: number; pruneCandidates: number };
};

const PLATES = [
  { href: "/encode", src: ART.encode, kicker: "Sung", title: "Encode" },
  { href: "/retrieve", src: ART.retrieve, kicker: "Recall", title: "Retrieve" },
  { href: "/brain", src: ART.synapses, kicker: "Hebb", title: "Brain" },
  { href: "/measure", src: ART.measure, kicker: "Johnson", title: "Measure" },
  { href: "/prune", src: ART.prune, kicker: "Homeostasis", title: "Prune" },
  { href: "/llms", src: ART.llms, kicker: "Frontier", title: "LLMs" },
] as const;

export default async function HomePage() {
  const data = await gql<HomeData>(HOME_QUERY);
  const encodeNotes = data.cluster.notes.filter((n) => n.type === "permanent").slice(0, 3);
  return (
    <main>
      <section className="hero">
        <picture>
          <source media="(min-width: 720px)" srcSet={asset(ART.heroWide)} />
          <img src={asset(ART.heroPortrait)} alt="Subterranean vault of gold axons" />
        </picture>
        <div className="hero-copy">
          <p className="kicker">{data.cycle.phase.toLowerCase()} · living vault</p>
          <h1 className="claim">Learn the frontier like a brain, not a feed.</h1>
          <p className="lede">
            Encode a schema. Retrieve it. Rest. Prune what does not fire. Agents write. Humans adjudicate.
          </p>
        </div>
      </section>

      <div className="well">
        <section className="cycle">
          <Ultradian phase={data.cycle.phase} />
          <div>
            <p className="kicker">90-minute bout</p>
            <p className="lede" style={{ margin: 0 }}>
              Rest in {data.cycle.nextRestInMinutes ?? 0} min. Plasticity needs alertness, then consolidation.
            </p>
            <PhaseBar phase={data.cycle.phase} />
          </div>
        </section>

        <div className="instrument" aria-label="Brain metrics">
          <div>
            <b>{data.brain.neurons}</b>
            neurons
          </div>
          <div>
            <b>{data.brain.synapses}</b>
            synapses
          </div>
          <div>
            <b>{data.brain.meanWeight.toFixed(2)}</b>
            mean w
          </div>
        </div>

        <p className="kicker">The cycle</p>
        <div className="gallery">
          {PLATES.map((p) => (
            <Link key={p.title} href={p.href} className="plate">
              <img src={asset(p.src)} alt="" />
              <span>
                <small>{p.kicker}</small>
                {p.title}
              </span>
            </Link>
          ))}
          <div className="plate">
            <img src={asset(ART.rest)} alt="" />
            <span>
              <small>Huberman</small>
              Rest
            </span>
          </div>
        </div>

        <p className="kicker">Encode next</p>
        <div className="stack">
          {encodeNotes.map((n) => (
            <Link key={n.id} href={`/note/${n.id}`} className="card">
              <h3>{n.title}</h3>
              <p>{n.distilled}</p>
              <div className="meta">
                <span>weight {n.weight.toFixed(2)}</span>
                <span>encode</span>
              </div>
            </Link>
          ))}
        </div>

        <p className="kicker" style={{ marginTop: "1.6rem" }}>
          LLM invariants
        </p>
        <div className="stack">
          {data.llmFrontier.slice(0, 3).map((n) => (
            <Link key={n.id} href={`/note/${n.id}`} className="card">
              <h3>{n.title}</h3>
              <p>{n.distilled}</p>
            </Link>
          ))}
        </div>
        <Link className="more" href="/llms">
          Full teaching track →
        </Link>
      </div>
    </main>
  );
}
