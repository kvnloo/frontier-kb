import { Scene } from "@/components/Scene";
import { NoteStack } from "@/components/NoteStack";
import { gql } from "@/lib/gql";
import { ART } from "@/lib/art";
import type { Note } from "@/lib/cycle";

export default async function AodlPage() {
  const data = await gql<{ cluster: { notes: Note[] } }>(
    `query { cluster(id: AODL_THESIS) { notes { id title distilled type weight } } }`,
  );
  return (
    <main>
      <Scene src={ART.aodl} kicker="AODL · contract on residual" title="Name d(I, O_t). Do not let the decoder fill holes.">
        <p className="lede">
          Fail-closed. Codec, compile, run. Kardashev changes budgets, not kinds. Inbox notes wait for CoS to promote.
        </p>
      </Scene>
      <div className="well">
        <NoteStack notes={data.cluster.notes} />
      </div>
    </main>
  );
}
