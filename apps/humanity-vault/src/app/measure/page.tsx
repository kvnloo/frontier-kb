import Link from "next/link";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note, ProtocolStep } from "@/lib/cycle";

export default async function MeasurePage() {
  const data = await gql<{
    brain: { neurons: number; synapses: number; meanWeight: number; pruneCandidates: number };
    dueRetrievals: Note[];
    cycle: { protocol: ProtocolStep[] };
  }>(
    `query {
      brain { neurons synapses meanWeight pruneCandidates }
      dueRetrievals(limit: 4) { id title }
      cycle { protocol { id source title why durationMinutes } }
    }`,
  );
  return (
    <main>
      <Scene src={ART.measure} kicker="Johnson · measure the loop" title="Effort is not a biomarker.">
        <p className="lede">Hit-rate, synapse weight, idle-days, prune rate. Time-on-page is vanity. Sleep still wins.</p>
      </Scene>
      <div className="well">
        <div className="instrument">
          <div>
            <b>{data.brain.neurons}</b>
            neurons
          </div>
          <div>
            <b>{data.brain.meanWeight.toFixed(2)}</b>
            mean w
          </div>
          <div>
            <b>{data.dueRetrievals.length}</b>
            due
          </div>
        </div>
        <div className="stack">
          {data.cycle.protocol.map((step) => (
            <article key={step.id} className="card">
              <h3>
                {step.title} · {step.source}
              </h3>
              <p>{step.why}</p>
              <div className="meta">
                <span>{step.durationMinutes} min</span>
                <span>protocol</span>
              </div>
            </article>
          ))}
        </div>
        <Link className="more" href="/prune">
          Review prune candidates →
        </Link>
      </div>
    </main>
  );
}
