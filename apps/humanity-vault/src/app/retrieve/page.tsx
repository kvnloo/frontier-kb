import Link from "next/link";
import { RetrievalActions } from "@/components/RetrievalActions";
import { Scene } from "@/components/Scene";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function RetrievePage() {
  const data = await gql<{ dueRetrievals: Note[] }>(
    `query { dueRetrievals(limit: 8) { id title distilled weight retrievalDue } }`,
  );
  return (
    <main>
      <Scene src={ART.retrieve} kicker="Retrieve · expanding interval" title="Regenerate the claim. Then look.">
        <p className="lede">
          Cover the distilled sentence. Say it. Hits potentiate; misses downscale. Familiarity is not knowledge.
        </p>
      </Scene>
      <div className="well">
        <div className="stack">
          {data.dueRetrievals.map((n) => (
            <article key={n.id} className="card">
              <Link href={`/note/${n.id}`}>
                <h3>{n.title}</h3>
              </Link>
              <p>{n.distilled}</p>
              <RetrievalActions id={n.id} />
            </article>
          ))}
        </div>
      </div>
    </main>
  );
}
