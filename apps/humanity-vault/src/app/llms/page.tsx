import Link from "next/link";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function LlmsPage() {
  const data = await gql<{ llmFrontier: Note[] }>(
    `query { llmFrontier { id title distilled weight type } }`,
  );
  return (
    <main>
      <Scene src={ART.llms} kicker="LLM frontier · 2026 invariants" title="Learn the invariants. Model names are examples.">
        <p className="lede">
          Post-training in the harness. Tool shape. Specialist routing. Note-ledger vs conversation memory. Context triad.
        </p>
      </Scene>
      <div className="well">
        <div className="stack">
          {data.llmFrontier.map((n) => (
            <Link key={n.id} href={`/note/${n.id}`} className="card">
              <h3>{n.title}</h3>
              <p>{n.distilled}</p>
              <div className="meta">
                <span>{n.type}</span>
                <span>encode → retrieve</span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </main>
  );
}
