import Link from "next/link";
import { PruneButton } from "@/components/PruneButton";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function PrunePage() {
  const data = await gql<{ pruneCandidates: Note[] }>(
    `query { pruneCandidates(limit: 20) { id title distilled type weight status } }`,
  );
  return (
    <main>
      <Scene src={ART.prune} kicker="Homeostasis · never silent-delete" title="Prune noise. Keep the signal.">
        <p className="lede">
          Unused inbox notes and weak edges are candidates. Permanent claims with fires stay. Restore is always allowed.
        </p>
      </Scene>
      <div className="well">
        {data.pruneCandidates.length === 0 ? (
          <p className="lede">No prune candidates in this snapshot. Retrieve notes so idle edges can decay honestly.</p>
        ) : (
          <div className="stack">
            {data.pruneCandidates.map((n) => (
              <article key={n.id} className="card">
                <Link href={`/note/${n.id}`}>
                  <h3>{n.title}</h3>
                </Link>
                <p>{n.distilled}</p>
                <div className="meta">
                  <span>
                    {n.type} · w {n.weight.toFixed(2)}
                  </span>
                  <PruneButton id={n.id} />
                </div>
              </article>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
