import Link from "next/link";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function EncodePage() {
  const data = await gql<{ cluster: { notes: Note[] } }>(
    `query { cluster(id: LEARNING_ACCELERATION) { notes { id title distilled type weight } } }`,
  );
  return (
    <main>
      <Scene src={ART.encode} kicker="Sung · higher-order encoding" title="Do not reread. Build the schema.">
        <p className="lede">
          Group these claims. Compare them. Name the relationship. Only then open the body. Exposure without encoding is
          noise.
        </p>
      </Scene>
      <div className="well">
        <div className="stack">
          {data.cluster.notes.map((n) => (
            <Link key={n.id} href={`/note/${n.id}`} className="card">
              <h3>{n.title}</h3>
              <p>{n.distilled}</p>
              <div className="meta">
                <span>{n.type}</span>
                <span>w {n.weight.toFixed(2)}</span>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </main>
  );
}
